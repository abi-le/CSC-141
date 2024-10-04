cities_ = {'atlanta': {
          'country':'usa', 
          'population' : '499k',
          'fact':'was originally named Terminus'
            },

        'santorini':{
        'country':'greece', 
        'population': '16k',
        'fact': 'is 63 miles from the island of Crete'
        },
        'tokyo' : {
        'country':'japan',
        'population':'14mil',
          'fact':'is the largest city in the world'
          },
        }
for name, cities in cities_.items():
    print(f"\n{name.title()}")
    loc = f"{cities['country']}"
    pop = f"{cities ['population']}"
    fact = f"{cities['fact']}"

    print(f"{name.title()} is located in {loc.title()}.")
    print(f"The city's population is {pop.title()}.")
    print(f"A fact about the {name.title()}, is that it {fact}.")
   