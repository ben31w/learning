# import module_name
import pizza

# import module_name as mn
import pizza as p

# from module_name import function_name
from pizza import make_pizza

# from module_name import fucntion_name as fn
from pizza import make_pizza as mp

# from module_name import *
from pizza import *

# import * will import all functions from a module, meaning you can call any
#  function without using dot notation (i.e. instead of writing 
#  module_name.function_name., you would simply write function_name). This may 
#  sound convenient, but it's generally not recommended. If you don't need to
#  use all the module's functions, this approach eats up unnecessary memory. 
#  More importantly, it makes your code harder to read for others, since it will
#  contain undefined functions that will appear to have no connection to any 
#  module at first.