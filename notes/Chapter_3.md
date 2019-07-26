# Chapter 3 - Functions



## What is a Function

Functions are little mini programs inside of your program that runs a small amount of code. You want to write a funciton whenever you have a portion of your code that is probably going to be repeated again. This reduces the need to copy and paste the same lines over and over again. 



You "define" a function as

> def hello():



Then indent all of the code that is inside of the function. A function has a name, parentheses followed by a colon. 





## **How do I activate another portion of the code**

To call a function you just use it's name and the parentheses. 

```
hello()
```

Sometimes you put values (or arguments) inside of the parentheses if the function requires it. 

```
hello('Jane')
```



When you create a function that requires a parameter, you may see it like this: 



def hello(name):



The 'name' variable is the parameter. The actual string/value assigned to the variable is the argument. 



## **How do I pass information to other parts of the code**

Functions can return information. Essentially the result of the function. This result is passed back to the part of the program that called it to begin with. The program can use that returned information for further use later on. 





## **What is the None Value?**

In reality all functions return some value. Even the built in functions, such as print() or while() when used with the continue statement...It will return the value None. if there is not other actually value available. 



## **Local and Global Scope**

Variables created in functions only live inside  (locally) of the function as long as the program is executing in the function. As soon as the program leaves, those variables values disappear. 



Variable created outside of function are global. They can be referenced everywhere and live as long as the program is executing. 



All variables cease to exist at the end of program execution. 



Think of it like rooms in a house. You can use anything in the house, but if you enter a room you can only use the things in that room as long as you are in the room. As soon as you leave the room everything is reset.  



**Local and Global Variables with the Same Name**

You can, but should you?  Ummmm



**What if something goes wrong, what should I do??**



Error handling is your friend. Never let your program just crash. 





**When you write a program**

Good practice is to comment like crazy. 





# Question and answer time

_________________________________



Q1. Why are functions advantageous to have in your programs?

*so you can compartmentalize reusable portions of your code*

Q2. When does the code in a function execute: when the function is defined or when the function is called?

*when the function is called*

Q3. What statement creates a function?

 *def helloPeoples()*

Q4. What is the difference between a function and a function call?

function - mini program

function call - when you write code to tell the mini program to execute

Q5. How many global scopes are there in a Python program? How many local scopes?

global scopes - 1

local scopes - equal to the number of functions

Q6. What happens to variables in a local scope when the function call returns?

disappear

Q:7. What is a return value? Can a return value be part of an expression?

the value a function evaluates to and sends to the code that called it

yes

Q8. If a function does not have a return statement, what is the return value of a call to that function?

None

Q9. How can you force a variable in a function to refer to the global variable?

 `global forcedVariable`



Q:10. What is the data type of None?

NoneType

Q11. What does the import *areallyourpetsnamederic* statement do?

import the module called areallyourpetsnamederic into the code and make all the functions in there available to your program

Q12. If you had a function named bacon() in a module named spam, how would you call it after importing spam?

```
spam.bacon()
```

Q13. How can you prevent a program from crashing when it gets an error?

Use error handling like try/except

Q14. What goes in the try clause? What goes in the except clause?

The code you want to attempt to run

The code that should run if there is an error
