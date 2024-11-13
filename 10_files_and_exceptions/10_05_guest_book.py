from pathlib import Path

#write a while loop hat prompts users for their name
responses = {}
asking_active = True

while asking_active:
    name = input ("Enter name: ")

    responses[name] = name

    repeat = input("If you have submitted answer and want to continue to the next person press enter\nif you do not want to continue poll to the next person type (end):")
    if repeat == 'end':
        asking_active = False

print("\n--- Poll Results ---")
for name, response in responses.items():
    print(f"{response}")


print("\n")
print (responses)
path = Path('guest_book.txt')
path.write_text(name)