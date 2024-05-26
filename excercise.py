a=int(input("Please enter your age:\n"))
b=input("are you student? (yes or no)\n").lower()

if b =="yes":
    if (a <= 12) or (a<=18 and a>=13):
        print("you will get discount for your movie ticket")
    else:
        print("sry your age exceed the discount citeria so no discount will be awarded")
else:
    print("you have to buy movie ticket without discount")