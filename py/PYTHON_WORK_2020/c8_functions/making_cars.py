from make_car import make_car as mc

outback = mc('subaru', 'outback', color='blue', tow_package=True)
print(outback)

andrews_car = mc('ford', 'explorer', color='grey', cause_of_destruction='fire')
print(andrews_car)