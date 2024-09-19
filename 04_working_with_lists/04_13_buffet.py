buffet_food = ('wings', 'green beans', 'rice', 'pasta', 'meatballs')
for foods in buffet_food:
    print(foods)

#Python reject change
# buffet_food[0] = 'boneless wings'

#Traceback (most recent call last):
  #File "c:\Users\leabi\Downloads\CSC 141\04_working_with_lists\04_13_buffet.py", line 5, in <module>
    #buffet_food[0] = 'boneless wings'
    #~~~~~~~~~~~^^^
#TypeError: 'tuple' object does not support item assignment

buffet_food = ('wings', 'green beans', 'rice', 'pasta', 'meatballs')
print("\nOriginal menu:")
for foods in buffet_food:
    print(foods)


buffet_foods = ('grilled chicken', 'roasted potatoes','rice', 'pasta', 'meatballs')
print("\nModified Menu:")
for foods in buffet_foods:
  print(foods)
  


