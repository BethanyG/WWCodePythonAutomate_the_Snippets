def collatz(number):
  '''Homework from Chapter 3:  Create a small program 
  that calculates colatz series.'''
  
    if number % 2 == 0:
        number = number // 2
        return number

    elif number % 2 == 1:
        number = 3 * number + 1
        return number

input_number = input("Type in a number.")
input_number = int(input_number)
answer = input_number

while answer != 1:
    answer = collatz(answer)
    print(answer)
