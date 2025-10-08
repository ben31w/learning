# Importing a module.
import pizza

# Importing a function inside a module
#  (you can import multiple functions if you list them with commas, or you can 
#  import all functions using an asterisk [e.g., from sandwiches import *], but 
#  it's not recommended).

# By using an as-statement, you can assign an alias to the function(s)
#  (you can also assign aliases to modules [e.g., import pizza as p]).

from sandwiches import make_sandwich as ms

pizza.make_pizza(12)
pizza.make_pizza(14, 'pepperoni',)
pizza.make_pizza(16, 'ham', 'pineapple', 'mushrooms')

ms()
ms('bologna')
ms('ham', 'salami', 'american cheese')