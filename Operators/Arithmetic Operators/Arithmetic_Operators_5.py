# Divisibility Check : Check whether a number is divisible by 3, 5, both, or neither

a=int(input("enter the number"))

if a%3==0 and a%5==0:
    print("the number is divisible by both 3 & 5")

elif a%3==0:
    print("the number is divible by 3")
elif a%5==0:
    print("the number is divible by 5")

else:
    print("the number is not divisble by either 3 and 5")        