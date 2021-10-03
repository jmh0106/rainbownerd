import datetime

if datetime.datetime.now() < datetime.datetime(2021, 11, 7):
    print("서머타임중")
else:
    print("서머타임아님")