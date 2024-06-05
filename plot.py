import sys
import numpy as np
import matplotlib.pyplot as plt

def get_filename(required_data):
    if required_data == 'test_data':
        return "farmers1.txt"
    elif required_data == 'ideal_data':
        return "farmer.TXT"
    else:
        sys.exit("Input request invalid: Please check the input for file name fetcher function call")


def get_plot_data(filename):
    # Load data from text file
    rawData = np.loadtxt(filename)

    # Remove erroneous scans from raw data
    rawData[rawData < 0] = 0

    # Find indices of '9999' delimiter in text file, indicating end of z-height scan
    indices = np.where(rawData == 9999)[0]

    # Arrange into matrix, where each row corresponds to one z-height
    r = [rawData[0:indices[0]]]
    for i in range(1, len(indices)):
        r.append(rawData[indices[i-1] + 1:indices[i]])

    r = np.array(r)

    # Delete last row of 9999 delimiters
    r = r[:, :-1]

    # Offset scan so that distance is with respect to turntable center of rotation
    centerDistance = 10.3  # Distance from scanner to center of turntable
    r = centerDistance - r

    # Remove scan values greater than maxDistance and less than minDistance
    maxDistance = 20
    minDistance = 0
    r[(r > maxDistance) | (r < minDistance)] = np.nan

    # Remove scan values around 0
    midThreshUpper = 0.5
    midThreshLower = -midThreshUpper
    midThreshIdx = (r > midThreshLower) & (r < midThreshUpper)
    r[midThreshIdx] = np.nan

    # Create theta matrix with the same size as r -- each column in r corresponds to specific orientation
    theta = np.linspace(360, 0, r.shape[1], endpoint=False)
    theta = np.radians(theta)
    theta = np.tile(theta, (r.shape[0], 1))

    # Create z-height array where each row corresponds to one z-height
    zDelta = 0.1
    z = np.arange(0, r.shape[0] * zDelta, zDelta)
    z = np.tile(z, (r.shape[1], 1)).T

    # Convert to cartesian coordinates
    x, y, z = np.cos(theta) * r, np.sin(theta) * r, z

    return x, y, z


def align_pos(x_ideal, y_ideal, z_ideal, x_test, y_test, z_test, error_rate):
    # Calculate the number of rows to add
    num_rows_to_add = z_ideal.shape[0] - z_test.shape[0]
    
    # Allowing 30% error for checking as it is going to handle small objects
    limiting_number = round(num_rows_to_add * error_rate) if round(num_rows_to_add * error_rate) >= 1 else 1

    # Extract the last `num_rows_to_add` rows from z_ideal
    z_errored = z_ideal[-num_rows_to_add:, :]

    # Create rows of NaNs for x and y with the same shape as the added rows in z_test
    nan_row = np.full_like(x_test[0], np.nan)  # Create a row of NaNs with the same shape as a single row in x_test
    nan_matrix = np.tile(nan_row, (num_rows_to_add, 1))  # Create a matrix of NaNs with the same number of rows as added in z_test

    # Append NaN rows to x_test and y_test
    x_test_view = np.vstack((x_test, nan_matrix))
    y_test_view = np.vstack((y_test, nan_matrix))
    
    return x_test_view, y_test_view, z_errored, limiting_number

def main():
    # Get name of the files of which the defect is going to be tested upon
    ideal_data_filename = get_filename("ideal_data")
    test_data_filename = get_filename("test_data")

    # Fetching coordinates of test and ideal data
    x_ideal, y_ideal, z_ideal = get_plot_data(ideal_data_filename)
    x_test, y_test, z_test = get_plot_data(test_data_filename)
    
    x_errored = []
    y_errored = []

    if z_ideal.shape[0] > z_test.shape[0]:
        # Align the shapes of Test Object and the Ideal Object
        x_test_view, y_test_view, z_errored, limiting_number = align_pos(x_ideal, y_ideal, z_ideal, x_test, y_test, z_test, error_rate=0.3)
        
        
        for i in range(z_ideal.shape[0]):
            for j in range(z_ideal.shape[1]):
                if y_ideal[i, j] == y_test_view[i, j]:
                    print("Yes", i, j)
                    print("x_ideal:", y_ideal[i, j])
                    print("x_test:", y_test_view[i, j])
                else:
                    print("No", i, j)
                    print("x_ideal:", y_ideal[i, j])
                    print("x_test:", y_test_view[i, j])
        
    else:
        print("Large object")

    # Plotting the point cloud of ideal object so that user can identify separately
    fig = plt.figure("Ideal Object")
    plt.title("Ideal Object")
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(x_ideal, y_ideal, z_ideal, c='b', marker='.')

    # Plotting the point cloud of test object so that user can identify separately
    fig = plt.figure("Test Object")
    plt.title("Test Object")
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(x_test, y_test, z_test, c='r', marker='.')

    # Comparing both the point clouds
    fig = plt.figure("Plot Comparison")
    plt.title("Ideal Object vs Test Object")
    ax = fig.add_subplot(111, projection='3d')
    # ax.scatter(x_errored, y_errored, z_errored, c='g', marker='.')
    ax.scatter(x_ideal, y_ideal, z_ideal, c='b', marker='.')
    ax.scatter(x_test, y_test, z_test, c='r', marker='.')

    # Plotting all 3 in different windows
    plt.show()


if __name__ == "__main__":
    main()


"""
Map according to z-axis
"""
