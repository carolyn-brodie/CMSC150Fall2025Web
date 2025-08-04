score = int(input("Enter a grade (0 - 100): "))


if score > 90:
    print("You received an A")

## If and else

# if score > 90:
#     print("You received an A")
# else:
#     print(f"You missed an A by {100 - score} points")



# # Ternary conditional expression

grade = "A" if score > 90 else "Not A"
# print(f"grade is {grade}")