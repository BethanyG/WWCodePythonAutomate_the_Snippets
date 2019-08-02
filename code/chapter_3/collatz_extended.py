def collatz_extended(number):
    '''This is the extended exercise from chapter 3, which adds
    error handling around the user input.'''

    if number % 2 == 0:
        number = number // 2
        return number

    elif number % 2 == 1:
        number = 3 * number + 1
        return number


while True:
    try:
        input_number = int(input("Type in a number."))
        break
    except ValueError:
        print("Ooops! That wasn't a valid number.  Please try again...")

answer = input_number

while answer != 1:
    answer = collatz_extended(answer)
    print(answer)
