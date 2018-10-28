a ,b = 0,1
while a <100:
    print(a)
    a,b=b,a+b # Here explanation is like this  first right hand side gets evaluated before assignment to the left hand side.
    # hence b and a+b are evaluated and then assigned to a and b respectively. Evaluation happens from left to right.