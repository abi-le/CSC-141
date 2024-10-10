responses = {}
polling_active = True

while polling_active:
    name = input("\nEnter name please:")
    response = input("Where is your dream place to vacation?")

    responses[name] = response

    repeat = input("If you have submitted answer and want to continue to the next person type (done)\nif you do not want to continue poll to the next person type (no):")
    if repeat == 'no':
        polling_active = False
        print(repeat)

print("\n--- Poll Results ---")
for name, response in responses.items():
    print(f"{name.title()} would like to go to {response.title()}.")