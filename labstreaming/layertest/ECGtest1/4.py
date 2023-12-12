import os

# Specify the directory path
directory_path = '/Users/stefanbao/Desktop/labstreaming/layertest/ECGtest1/'

# Specify the file names
hea_file_name = 'rec1.hea'
dat_file_name = 'rec1.dat'

# Create absolute paths
hea_file_path = os.path.join(directory_path, hea_file_name)
dat_file_path = os.path.join(directory_path, dat_file_name)

# Print the absolute paths
print(f"Hea file path: {hea_file_path}")
print(f"Dat file path: {dat_file_path}")

# Continue with the rest of your script using hea_file_path and dat_file_path
# Write your code here :-)
