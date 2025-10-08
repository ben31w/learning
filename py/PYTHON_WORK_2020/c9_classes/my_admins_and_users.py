from user import User
from admin import Admin

user_1 = User('ben', 'wright', 18, 'leesburg')
user_2 = User('andrew', 'wright', 20)
user_3 = User('lynne', 'wright', 65, 'leesburg')
admin = Admin('michael', 'wright', 63, 'washington, d.c.')

user_1.describe_user()
user_1.greet_user()

user_2.describe_user()
user_2.greet_user()

user_3.describe_user()
user_3.greet_user()

admin.describe_user()
admin.greet_user()

print()
admin.privileges.add_privileges('can punish other users', "unable to be banned")
admin.privileges.show_privileges()