currenttime=float(input("What time is it now? (0-24)" ))
hours=float(input("How many hours are you waiting?" ))
resulttime=int(currenttime+(hours%24))
if resulttime>24:
    resulttime%24+currenttime
standardtime=resulttime%12
if standardtime>12:
    standardtime%12
if standardtime<12:
    print("Your clock will go off at", resulttime, ":00")
answer=input("Do you want this in 12-hour clock?" )
if "yes":
    print("this is also", standardtime)