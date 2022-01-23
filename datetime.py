from datetime import datetime

def datetimetimeformatter() :
    datetimestr = input('Enter the datetime in "mm/dd/yyyy hh:mm" format: ')
    objdatetime = datetime.strptime(datetimestr,"%m/%d/%Y %H:%M")
    datetuple = (objdatetime.strftime('%B'),objdatetime.strftime('%A'),objdatetime.year,objdatetime.strftime('%I:%M %p'))
    return datetuple

print(datetimetimeformatter())
#sample input - 10/23/2021 17:15