import schedule
import time

def job():
  print('早安')

schedule.every().monday.at('07:00').do(job)
schedule.every().tuesday.at('07:00').do(job)
schedule.every().wednesday.at('07:00').do(job)
schedule.every().thursday.at('07:00').do(job)
schedule.every().friday.at('07:00').do(job)

while True:
  schedule.run_pending()
  time.sleep(1)