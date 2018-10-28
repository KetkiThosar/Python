for num in range(1,35):
    string = ""
    if num % 3 == 0 and num % 5 == 0:
        string = "FizzBuzz"
    elif num % 3 == 0:
        string =string + "Fizz"
    elif num % 5 == 0:
        string =string +"Buzz"
    elif num % 5 != 0 and num % 3 != 0:
         string =string + str(num)
    print(string)