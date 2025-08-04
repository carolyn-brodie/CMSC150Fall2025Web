#Write a program to compute the average of numbers entered by the user.
#The number of numbers is not known ahead of time.


#option 1
total = 0
count = 0
done = False
while done == False:
    numberStr = input("Enter a number (enter Q to end): ")
    if numberStr == "Q":
        done = True
    else:
        number = float(numberStr)
        total += number
        count += 1
if count != 0:
    print("The average is", total/count)
else:
    print("The average is 0")
