import wfdb
import matplotlib.pyplot as plt
import numpy as np

# Replace this with your file path
hea_file = '/Users/stefanbao/Desktop/labstreaming/layertest/ECGtest1/rec1'

# Read header file to get metadata
record = wfdb.rdheader(hea_file)

# Replace this with the corresponding .dat file path
dat_file = '/Users/stefanbao/Desktop/labstreaming/layertest/ECGtest1/rec2'

# Read .dat file to get data
signals, fields = wfdb.rdsamp(dat_file)

# Get time axis
time_axis = (1 / record.fs) * np.arange(record.sig_len)

# Plot ECG waveform
plt.figure(figsize=(12, 6))
for i in range(record.n_sig):
    plt.plot(time_axis, signals[:, i], label=fields['sig_name'][i])

plt.title('ECG Visualization')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.legend()
plt.show()
# Write your code here :-)
# Write your code here :-)
