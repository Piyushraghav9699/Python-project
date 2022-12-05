print("Hello Sir/Mam ,Welcome")
d=input("Enter your Name--  ")
print("Hello {} please enter the Current- Date/Month/Year".format(d))
# cdate means current date and cmonth means current month and c year means current year
cdate1=int(input("Current Date--"))
cmonth=int(input("Current Month--"))
cyear=int(input("Current  Year--"))
print("Now {} please enter the your [Date Of Birth]- Date/Month/Year".format(d))
# date means date---- [ of  means =month]------{birth=year}
date=int(input("Date--"))
of=int(input("Month--"))
birth=int(input("Year--"))
age=cdate1-date
print("Hello {},Now you become".format(d))
if cdate1>31 or date>31:
    print("Invalid Date [Date should be between 1 to 31] ")
elif cdate1>date:
    print('{} days'.format(age))
elif date>cdate1:
    if cmonth==1:
        print(cdate1+31-date,'Days')
    elif cmonth==2:
        if cyear%4==0:
            print(cdate1+29-date,'Days')
        else:
            print(cdate1+28-date,'Days')
    elif cmonth%2==0:
            print(cdate1+30-date,'Days')
    else:   
        print(cdate1+31-date,'Days')
if cdate1<date:
    cmonth=cmonth-1
else:
    cmonth=cmonth
if cmonth<of:
    y=cmonth+12
    cyear=cyear-1
else:
    y=cmonth
    cyear=cyear
age2=y-of    
age3=cyear-birth
if cmonth>12 or of>12:
    print("Invalid month [Month should be between 1 to 12] ")
else:
    print('{} Months'.format(age2))
if cyear<birth:
    print("Invalid")
else:
    print('{} Years'.format(age3))

