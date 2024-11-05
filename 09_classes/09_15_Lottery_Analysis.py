#difficulty = 8
import random
myList = [1, 42, 3, 4, 35, 56, 27, 78, 129, 10, 'a', 'e', 'r', 't', 'z']


value1 = myList[random.randint(0, len(myList) - 1)]
value2 = myList[random.randint(0, len(myList) - 1)]
value3 = myList[random.randint(0, len(myList) - 1)]
value4 = myList[random.randint(0, len(myList) - 1)]

finalString = f"{value1},{value2},{value3},{value4}"

print (f"Anyone with a ticket matching the value {finalString} has won a prize!")

# my_ticket = []
ticket_string = ""
count = 0
while ticket_string != finalString:
    value1 = myList[random.randint(0, len(myList) - 1)]
    value2 = myList[random.randint(0, len(myList) - 1)]
    value3 = myList[random.randint(0, len(myList) - 1)]
    value4 = myList[random.randint(0, len(myList) - 1)]

    ticket_string = f"{value1},{value2},{value3},{value4}"

    if ticket_string != finalString:
        count = count+1
    
print (f"Your ticket matches! Amount of runs: {count}")