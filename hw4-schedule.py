import schedule
import time

def job():
  print('早安')

schedule.every().monday.at('08:00').do(job)
schedule.every().tuesday.at('08:00').do(job)
schedule.every().wednesday.at('08:00').do(job)
schedule.every().thursday.at('08:00').do(job)
schedule.every().friday.at('08:00').do(job)

while True:
  schedule.run_pending()
  time.sleep(1)