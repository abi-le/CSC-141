#difficulty = 6
import random
myList = [1, 42, 3, 4, 35, 56, 27, 78, 129, 10, 'a', 'e', 'r', 't', 'z']


value1 = myList[random.randint(0, len(myList))]
value2 = myList[random.randint(0, len(myList))]
value3 = myList[random.randint(0, len(myList))]
value4 = myList[random.randint(0, len(myList))]

finalString = f"{value1},{value2},{value3},{value4}"

print (f"Anyone with a ticket matching the value {finalString} has won a prize!")

