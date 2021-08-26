# import datetime
#
# from Utilities.readProperties import ReadConfig
#
# File_Name = "ELIG_edi_270_BAPTISTH"
#
# from datetime import datetime
#
# current_time = datetime.now()
# date_formate = current_time.strftime('%m/%d')
# year = current_time.strftime('%y')
# date = date_formate.replace('/','')+year+""
# print(File_Name+date)
# download = ReadConfig.get_Downloads()
# date = ReadConfig.get_date()
# print(type(download+date))
# print(type(download+""+date))

row = 3
column = 1
for i in range(100):
    inchara = "//input[@type='checkbox']"+"["+str(i)+"]"
    row = row+1
    column = column+1
    print(i,inchara)