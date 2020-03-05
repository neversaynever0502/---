import time;  # 引入time模块

localTime = time.localtime()
transTime = time.strftime("%H:%M:%S",localTime)
print('現在時間：'+transTime)
