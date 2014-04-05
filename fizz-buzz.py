def fizzbuzz(n):
    fizz = 3
    buzz = 5
    for i in range(n):
        if i % fizz == 0 and i % buzz == 0:
            print("FizzBuzz")
        elif i % buzz == 0:
            print("Buzz")
        elif i % fizz == 0:
            print("Fizz")
        else:
            print(i)
        
fizzbuzz(15)


