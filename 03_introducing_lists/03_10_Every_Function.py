list = ['Yosemite', 'Death Valley', 'Kings Canyon', 'Grand Teton']
print(list)

#Accessing elements in a list
print(list[0])
print('\n')

#Using individual values from a list
message = f"My first national park I went to was {list[2].title()}\n"

print(message)

#Modifying elements in a list
list[0] = 'North Cascades'
print(list)
print('\n')

#Adding elements to a list (end of a list)
list.append('Yosemite')
print(list)
print('\n')

#Inserting elements into a list
list.insert(0, 'Joshua tree')
print(list)
print('\n')

#Removing an item using the del statement
del list[1]
print(list)
print('\n')

#Removing using pop() method 
popped_list = list.pop()
print(list)
print(popped_list)
print('\n')

#Popping items from any position in a list
first_national_park = list.pop(2)
print(f"My first national park I went to was {first_national_park.title()}.\n")

#Removing an item by value
list.remove('Death Valley')
print(list)
print ('\n')

list_2 = ['Joshua tree', 'North Cascades', 'Death Valley', 'Kings Canyon', 'Grand Teton', 'Yosemite']
print (list_2)
print('\n')

#Sorting a list temporarily with the sorted() function
print ("Here is original list:")
print(list_2)

print("\n Here is the sorted list:")
print(sorted(list_2))
print('\n')

print("Here is the original list again:")
print(list_2)
print('\n')

#Printing a list in reverse order
list_2.reverse()
print(list_2)
print('\n')

#Finding the length of a list
len(list_2)
print(len(list_2))





#sorting a list permanently with the sort() method
#list_2.sort() 
#print(list_2)
#print('\n')



