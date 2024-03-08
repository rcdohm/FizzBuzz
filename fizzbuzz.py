def main():
    for i in range(1,101): #iterate from 1 to 100
        if i % 3 == 0 and i % 5 ==0: #check to see if number is evenly divisable by 3 or 5, if so print FizzBuzz
            print("FizzBuzz")
        elif i % 3 == 0: #check to see if number is evenly divisable by 3, if so print Fizz
            print("Fizz")
        elif i % 5 == 0: #check to see if number is evenly divisable by 5, if so print Buzz
            print("Buzz")
        else: #if number is not divisable by 3,5, or both, then just print the number
            print(i)
main()