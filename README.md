# Chapters2to4
#CHAPTER 2 Exercises

#Exercise 1
yes="all"
this= "work"
sentence="and"
makes="no"
alot="play"
of="makes"
sense="Jack"
to="a"
us="dull"
now="boy"
print(yes, this, sentence, makes, alot, of, sense, to, us, now)

#Exercise 2
print(6*1-2)
print(6*(1-2))

#Exercise 3
yes="all"
this= "work"
sentence="and"
makes="no"
alot="play"
of="makes"     #this is a comment so we can see what happens, 
sense="Jack"   #which is nothing because this is only for humans to read
to="a"
us="dull"
now="boy"
print(yes, this, sentence, makes, alot, of, sense, to, us, now)

#Exercise 4
bruce=6
print(bruce+4) #now "bruce" is a defined variable

#Exercise 5
response=input("How many years are you investing your money? ")
P=10000
n=12
r=0.08
t=float(response)
Amount=P*(1+r*(1/n))**n*t
print("Your final amount after t years will be", Amount)

#Exercise 6
7%0   #Traceback (most recent call last):
      #File "<pyshell>", line 1, in <module>
      #ZeroDivisionError: integer division or modulo by zero
#Zero division error appears with this command

#Exercise 7
#2pm + 51 hours is 5 pm. The clock will go off at 5 pm or in military time, 17:00

#Exercise 8
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

