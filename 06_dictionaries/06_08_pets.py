dog = {'kind' : 'golden retriever', 'owner' : 'doug'}
cat = {'kind' : 'calico', 'owner': 'jen'}
bird = {'kind' : ' parakeet', 'owner' : 'jason'}

pets = [dog, cat, bird]
for info in pets:
    print (f"The kind of pet is a {info['kind'].title()}, and the owners name is {info['owner'].title()}.")
