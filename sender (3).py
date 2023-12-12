from pylsl import StreamInfo, StreamOutlet
import time
import random

# 创建 Stream 信息
info = StreamInfo('MyStream', 'EEG', 8, 100, 'float32', 'myuid123456')

# 创建 Stream 输出对象
outlet = StreamOutlet(info)

# 模拟发送数据
while True:
    # 生成随机样本数据
    sample = [random.random() for _ in range(8)]

    # 发送数据
    outlet.push_sample(sample)

    # 等待一段时间，模拟实时数据流
    time.sleep(0.1)
# Write your code here :-)
