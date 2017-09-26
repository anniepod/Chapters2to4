response=input("How many years are you investing your money? ")
P=10000
n=12
r=0.08
t=float(response)
Amount=P*(1+r*(1/n))**n*t
print("Your final amount after t years will be", Amount)
