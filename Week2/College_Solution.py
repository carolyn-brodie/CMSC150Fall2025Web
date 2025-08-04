

# Write a program that asks the user
# what college they are attending and prints out a strong
# congratulations if it's Simpson, a strong condemnation if it's
# Central, a mild congratulations if it's Drake or Coe, and a neutral ' \

#'message if it's any other college.

college = input("What college do you attend: ")

if college == "simpson":
    print("Congratulations on attending Simpson College!")
elif college == "central":
    print("We do not condone your choice to attend Central College.")
elif college == "drake" or college == "coe":
    print("Congratulations on attending a fine institution!")
else:
    print("Thank you for your response.")
