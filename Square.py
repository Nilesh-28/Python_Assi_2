mylist = []
number = int(input('How many elements to put in List :- '))
for n in range(number):
    element = int(input('Enter element => '))
    mylist.append(element)
print("---------------------------------------------------------------------------")
print("The given list is : ")
print(mylist)
print("\n")
length = len(mylist)
sum = 0
for i in range(length):
    sum = sum + mylist[i] * mylist[i]
print("Sum of square of all the elements in the list is :- ", sum)