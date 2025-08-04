



def counter(alist):
    #alist = [10,20,30,5]
    count = 0
    for item in alist:
        count += 1
    return count

print(counter([10,20,30]))
print(len([10,20,30]))

print(counter("hi Mom"))
print(len("hi Mom"))