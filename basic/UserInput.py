weight = input("Enter your weight: ")
type = input("(L)bs or (K)g : ")
type = type.lower()
weight_number = int(weight)
if type.__eq__('k'):
    print('Weight in Lbs is ' + str(weight_number * 2.22))
elif type.__eq__('l'):
    print('Weight in kg is ' + str(weight_number * 0.45))
else:
    print(type + 'is not identified. Please insert correct input')