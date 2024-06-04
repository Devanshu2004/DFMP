import numpy as np
import open3d as o3d
import plot

# Import the filename and coordinates
filename = plot.get_filename("ideal_data")
x, y, z = plot.get_plot_data(filename)

# Convert coordinates into Numpy Column Stack
point_data = np.column_stack((x.flatten(), y.flatten(), z.flatten()))

# Plot the data
geom = o3d.geometry.PointCloud()
geom.points = o3d.utility.Vector3dVector(point_data)
o3d.visualization.draw_geometries([geom])
