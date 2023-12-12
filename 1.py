import wfdb
import matplotlib.pyplot as plt

# 读取 .hea 文件获取元信息
hea_file = 'ecg.hea'
record = wfdb.rdheader(hea_file)

# 读取 .dat 文件获取数据
dat_file = 'ecg.dat'
signals, fields = wfdb.rdsamp(dat_file)

# 获取时间轴
time_axis = (1 / record.fs) * np.arange(record.sig_len)

# 绘制ECG波形
plt.figure(figsize=(12, 6))
for i in range(record.n_sig):
    plt.plot(time_axis, signals[:, i], label=fields['sig_name'][i])

plt.title('ECG Visualization')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.legend()
plt.show()
