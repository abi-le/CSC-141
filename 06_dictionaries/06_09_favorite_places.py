favorite_places = {'david' : ['Iceland' , 'Japan'], 
                   'jessica' : ['Ireland' , 'Germany'], 
                   'eric' : ['Italy' , 'Arizona'],}
for key, value in favorite_places.items():
    print (f"\n{key.title()}'s favorite places to visit are:")
    for country in value:
        print(f"{country.title()}")