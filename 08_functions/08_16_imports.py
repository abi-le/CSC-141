#import module_name
import function

function.make_sandwich ('cheese', 'bread')

#from module_name import funtion_name
from function import make_sandwich
make_sandwich ('salami', 'tomamto', 'pepperochinis')

#from module_name import function_name as fn
from function import make_sandwich as fn
fn('turkey', 'lettuce', 'bacon')

#import module_name as mn
import function as mn
mn.make_sandwich('peanut butter', 'jelly')

#from module_name import*
from function import*
make_sandwich('bacon', 'lettuce', 'tomato')
