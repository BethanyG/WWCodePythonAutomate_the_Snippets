A program is just a series of instructions that the computer will execute one by one in order.  For more complicated ordering & branching, Python provides an additional set of *Flow Control statements*. These statements can direct which instructions Python will execute under which conditions.



## Flow Controls fall into several different categories:



### Boolean Values

![true_and_false](../True%20and%20False.png)



----------------------------------------------------------------------




### Comparison Operators



![comparison_operators](../Comparison%20Operators.png)



_________________________________________________________________



### Boolean Operators



![boolean_operators](../Boolean%20Operators.png)


&nbsp;
&nbsp;


## The above are combined in Flow Control Statements using `if`, `elif`, & `else`:


&nbsp;
   

```python
def is_leap_year(year): 
  if year % 400 == 0
    print('leap year!')
  elif year % 100 == 0:
    print('not leap year.')
  elif year % 4 ==0:
    print('leap year!')
  else:
    print('not leap year.')
```

 
&nbsp;




![if_elif_else](If%20Elif%20Else.png)





## `While` & `For` Loops have Additional Tools:  `continue` & `break`:

&nbsp;

- `break` is used to end a loop if a certain condition is met.  It means `STOP` looping & exit.
- `continue` is used to "skip ahead" to the next cycle of the loop if a certain condition is met.

&nbsp;

Both can be used in `for` or `while` loops, but `break` is mostly used with a `while` loop to avoid *infinite loops.*


&nbsp;


```python
n = 5

while n > 0:
    n -= 1
    if n == 2:
        break
    print(n)
print('Loop ended.')   
```


&nbsp;


```python
for number in range(10):
    if number % 2 != 0:
      print(f"{number} is odd, and it's cube is: ", number**3) 
    else:
        continue
```

&nbsp;



## `For` & `while` Loops can use `range()` as a counter for the loop:
  
`range()` is an example of something that is *iterable* in Python.  That means it is a **sequence** that the Python interpreter can **step through item by item** until the sequence ends.  
Other examples of iterables in Python include `strings` ,  `lists` , `tuples` , `dictionaries` , and `sets` .


&nbsp;


```python
input_data = ['Apple', 'Pear', 'Grapes', 'Plums', 'Figs']

for fruit in input_data:
    print(f'I like to eat {fruit}')

for fruit in input_data:
    for letter in fruit:
        if letter in ['a', 'A']:
           print('I found an A!!!')
        else:
            print(letter)
```

&nbsp;
&nbsp;



## Importing Modules:



Python has a large list of **built-in functions**, including `print()`, `input()`, and `len()`.  But Python also has an extended set of modules called the **standard library** or "core" Python.  Before you can use the functions in a module, you must **import** the module with the `import` statement:



```python
import random, math
```

&nbsp;

Once a module is imported, you can use the functions of that module by calling them with **dot notation:**

&nbsp;

```python
import random

for i in range(5):
  print(random.randint(1, 10))
```

&nbsp;
&nbsp;


## Programs can be ended with `sys.exit()` (but you have to import the `sys` module first!)


_______________________________________________________________________________

________________________________________________________________________________



# Practice Questions



1. `True` and `False` are the two values of the `Boolean data type`
2. `and`, `or`, & `not` are the three Boolean operators
3.  Truth Table:       
    *  True and True >> `True`  
    *  True and False >> `False` 
    *  False and True >> `False` 
    *  False and False >> `False`   
    *  True or False >> `True` 
    *  False or True >> `True` 
    *  True or True >> `True` 
    *  False and False >> `False` 
    *  not False >> `True` 
    *  not True >> `False`



4 Expression Evaluation:
  *  (5 > 4) and (3 == 5) >> `False` 
  *  not (5 > 4) >> `False` 
  *  (5 > 4) or (3 == 5) >> `True` 
  *  not ((5 > 4) or (3 == 5)) >> `False` 
  *  (True and True) and (True == False) >> `False` 
  *  (not False) or (not True) >> `True` 



5 The comparison operators are:  
  *  `==` *(equal to)* 
  *  `>=` *(greater than or equal to)* 
  *  `<=` *(less than or equal to)*
  *  `>` *(greater than)*
  *  `<` *(less than)*
  *  `!=`  *(not equal to)* 



6 -  The `==` operator checks to see if the values on the right and the left are **equal to** one another.  
  -  The `=` operator points the **name** of a variable at the **value** it represents.



7 *Conditions are "checks", "options", or "gates" in code.  They help to enforce different paths or choices in the execution of a program.*



8 Blocks in code:

&nbsp;

```python
#block 1: outermost scope
spam = 0

#block 2:  level one scope
if spam == 10:
    print('eggs')

    #block 3: level two scope
    if spam > 5:
        print('bacon')
    else:
        print('ham')
    print('spam')

print('spam') 
    ```

&nbsp;

9  Write code that prints `Hello` if `1` is stored in `spam`, prints `Howdy` if `2` is stored in `spam`, and prints `Greetings!` if anything else is stored in `spam`.

&nbsp;

```python
spam = int(input('Pick a number between 1-5'))

if spam == 1:
    print('Hello')
elif spam == 2:
    print('Howdy')
else:
    print('Greetings!') 
```

&nbsp;

10 `CTRL-C` will manually break and endless loop. ( `CMND-C`  on some systems)

11 `break` stops looping and exits the loop block.  `continue` "fast-forwards" to the next cycle of the loop.

12 `range(10)`, `range(0, 10)`, & `range(0, 10, 1)` in a `for` loop:

​     `range(10)`, assumes `0 --> 9` ,

​     `range(0, 10)` has an explicit start of **index 0** , and an explicit end of **9** 

​      `range(0, 10, 1)` has an explicit start of **index 0** , an explicit end of **9** , and a **step** of **1** 



13 `For` and `While` 

```python
for number in range(1, 11):
    print(f'My number is: {number}!')

numbers = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

while numbers:
    number = numbers.pop()
    print(f'My number is:  {number}!')
```



14 calling `bacon` from imported module `spam` :



```python
spam.bacon()
```
