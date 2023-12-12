from pylsl import resolve_byprop, StreamInlet

# 根据 Stream 名称查找数据流
stream = resolve_byprop('name', 'MyStream', timeout=5)

if not stream:
    print("Stream not found. Make sure the sender script is running.")
else:
    # 创建 Stream 输入对象
    inlet = StreamInlet(stream[0])

    # 读取数据
    while True:
        sample, timestamp = inlet.pull_sample()
        print("Received sample:", sample)
# Write your code here :-)
