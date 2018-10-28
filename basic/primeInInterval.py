# prints prime number in given interval

lower=int (input("Enter lower range: "))
upper=int (input("Enter upper range: "))

if lower >= upper :
    print('invalid range')

if  (lower > 1) and (lower < upper) :
  for num in range(lower,upper+1):

    for i in range (2,num):
        if (num%i) == 0:
            print('{0} not a prime number. Its divisible by {1}'.format(num,i))
            break
    else:
        print(num)
