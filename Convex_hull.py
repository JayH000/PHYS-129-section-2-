import numpy as np 
import matplotlib.pyplot as plt

# Path to the file
file_path = "~/Documents/mesh (1).dat"

# Load data (assuming space-separated values)
try:
    data = np.loadtxt(file_path)
    
    # Plot the data as a heatmap
    plt.imshow(data, cmap='viridis', origin='lower')
    plt.colorbar(label='Value')
    plt.title('Mesh Data Visualization')
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.show()
except Exception as e:
    print(f"Error loading file: {e}")
