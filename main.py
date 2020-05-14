import tweepy
import random
import schedule
import time
import datetime

CK = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
CS = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
AT = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
AS = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'

DIFF_JST_GST = 9

def routine(api):
  now = (datetime.datetime.now() + datetime.timedelta(hours=DIFF_JST_GST)).strftime("%H")

  if int(now) < 10:
    now = now[-1]

  msg = now + '時のﾌﾞﾘｯｗ\n'
  
  randValue = random.random()
  
  counter = 0 
  probability = 2 
  
  while randValue < 0.5:
    msg = 'うんち！ｗ\n' + msg 
    counter += 1
      
    if counter >= 20: 
      break
      
    probability *= 2
    randValue = random.random()
      
  msg = msg + '\n\n' + str(counter) + 'うんち : 確率1/' + str(probability) + '\n#うんち #ていねいな暮らし'
  print(msg)
  api.update_status(status = msg)

  
auth = tweepy.OAuthHandler(CK, CS)
auth.set_access_token(AT, AS)
api = tweepy.API(auth)

schedule.every().hour.at(":00").do(routine, api)

while True:
  schedule.run_pending()
  time.sleep(5)

