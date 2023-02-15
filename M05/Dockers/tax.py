# Drashaun Morrow
# M05 Dockers - tax.py
# This program will take a given gross pay and calculate federal and state tax.


import emoji
from emoji import emojize






#initialize standard tax
Statetax = 0.0323
SocialMedicare = 0.0765

    

grossPay = float(input("Enter gross pay: "))


#Calculate tax bracket

if grossPay <= 11000:
    federalTax = .10
elif grossPay <= 44725:
    federalTax = .12
elif grossPay <= 95375:
    federalTax = .22
elif grossPay <= 182100:
    federalTax = .24
elif grossPay <= 231250:
    federalTax = .32
else:
    federalTax = .35
    
    
combinedTax = federalTax + Statetax + SocialMedicare
    
totalTax = grossPay * combinedTax

netPay = grossPay - totalTax
    

print("Your net pay is $" + str(netPay))
print(emojize(":thumbs_up:"))

