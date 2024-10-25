def make_car (manufacturer, model, color, **arguements):
    '''print car and its details/arguements'''
    arguements['manufacturer'] = manufacturer
    arguements ['model'] = model
    arguements ['color'] = color
    return arguements

car = make_car('toyota', 'corolla', 'grey', tires='michelin')

print(car)