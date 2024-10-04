#loop sentence
rivers = {'Nile' : 'Egypt',
          'Tigris' : 'Turkey',
          'Yangtze' : 'China'}
for name,term in rivers.items():
    print (f"\nThe {name} runs through {term}\n")

#loop of river name
for river in rivers.keys():
    print(river)
print('\n')

#loop of each country
for term in rivers.values():
    print (term)
