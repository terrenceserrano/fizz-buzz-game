#create a program that will show the fizz buzz

#example if divisible by 3 and 5 it will return fizz buzz
# and if divisible by 3 it will return fizz
# and if divisible by 5 it will return buzz

num = int(input("Please enter number here: "))

for fizzbuzz in range(num):
    #we can also use the if fizzbuzz % 3 == 0 and fizzbuzz % 5 == 0, but for the simplicity we can use the LCD of 3 and 5
    if (fizzbuzz % 15 == 0): #we use the % 15 because thier LCD is 15 so that if this is not true we will proceed to the next condition
         print("Fizz Buzz")
    elif (fizzbuzz % 3 == 0):
        print("Fizz")
    elif (fizzbuzz % 5 == 0):
        print("Buzz")
    else:
        print("Fizz buzz")