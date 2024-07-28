while True:
    try:
        number = int(input("Input a number: "))
        break
    except ValueError:
        print("Invalid input. Please enter a whole number.")

def fizzbuzz(i):
    if (i % 3 == 0 ) and (i % 5 == 0) :
        return "FizzBuzz"
    if i % 3 == 0:
        return "Fizz"
    if i % 5 == 0:
        return "Buzz"
    return i

output = fizzbuzz(number)

print(output)