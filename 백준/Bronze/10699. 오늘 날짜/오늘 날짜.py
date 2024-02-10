import datetime

seoul = datetime.datetime.now() + datetime.timedelta(hours=9)
print(seoul.strftime("%Y-%m-%d"))