import numpy as np
# import matplotlib.pyplot as plt
import open3d as o3d

# Load data from text file
rawData = np.loadtxt('farmer.txt')

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

'''
# Plotting the point cloud
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(x, y, z, c='b', marker='.')
plt.show()
'''
point_data = np.column_stack((x.flatten(), y.flatten(), z.flatten()))

geom = o3d.geometry.PointCloud()
geom.points = o3d.utility.Vector3dVector(point_data)
o3d.visualization.draw_geometries([geom])