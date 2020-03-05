import time

localTime = time.localtime()
transTime = time.strftime("%H:%M:%S",localTime)
print('現在時間：'+transTime)
