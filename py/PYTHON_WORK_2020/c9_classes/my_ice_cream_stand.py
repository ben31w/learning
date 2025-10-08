from ice_cream_stand import IceCreamStand as ICS

bic = ICS("ben's ice cream")

bic.describe_restaurant()

print()
bic.add_flavors('mint chocolate chip', 'vanilla', "cookies n' cream")
bic.display_flavors()