# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from datetime import datetime

modTs="2020-10-22T23:27:14.966+02:00"
date_object=datetime.strptime(modTs[0:19],"%Y-%m-%dT%H:%M:%S")
print("dt_object1 =", date_object)
date_time = date_object.strftime("%d-%m-%Y %I:%M:%S %p")
print("date and time:",date_time)