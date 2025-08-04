
list1 = [10, 20, 30, 40]

# print(list1[0])
# print(list1[1])
# print(list1[2])
# print(list1[3])
list1 = [10, -20, 30, 40, -1, 2]
positives = 0
negatives = 0
for number in list1:
    if number >= 0:
        positives = positives + number
    else:
        negatives = negatives + number

print(positives)
print(negatives)
#print("The loop is done")