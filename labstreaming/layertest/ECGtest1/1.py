from pylsl import StreamInfo, StreamOutlet
import time
import random
import logging
import wfdb
import matplotlib.pyplot as plt
import numpy as np

logging.basicConfig(level=logging.DEBUG)

# Create LSL Stream
info = StreamInfo('Duo', 'EEG', 8, 100, 'float32', 'myuid123456')
outlet = StreamOutlet(info)

# File paths for ECG data
hea_file = '/Users/stefanbao/Desktop/labstreaming/layertest/ECGtest1/rec1'
dat_file = '/Users/stefanbao/Desktop/labstreaming/layertest/ECGtest1/rec1'

# Read header file to get metadata
record = wfdb.rdheader(hea_file)

# Get time axis
time_axis = (1 / record.fs) * np.arange(record.sig_len)

# Plot ECG waveform
plt.figure(figsize=(12, 6))
plt.ion()  # Turn on interactive mode for live plotting

while True:
    # Generate random EEG-like sample data
    eeg_sample = [random.random() for _ in range(8)]

    # Send EEG data via LSL
    outlet.push_sample(eeg_sample)

    # Read .dat file to get ECG data
    signals, fields = wfdb.rdsamp(dat_file)

    # Plot ECG waveform
    plt.clf()  # Clear the previous plot
    for i in range(record.n_sig):
        plt.plot(time_axis, signals[:, i], label=fields['sig_name'][i])

    plt.title('ECG Visualization')
    plt.xlabel('Time (s)')
    plt.ylabel('Amplitude')
    plt.legend()
    plt.pause(0.1)  # Add a short pause for live plotting

    # Wait a short time before sending the next EEG sample
    time.sleep(0.1)# Write your code here :-)
