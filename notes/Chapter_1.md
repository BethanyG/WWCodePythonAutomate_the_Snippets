# Automate the Boring Stuff - Python Basics Recap (Ch 1)



# **How do you start coding in Python?** 

If you want to do it a line at a time. Open the interactive wheel so you can see the results of your Python instructions. Once you have Python installed, you'll find the IDLE program in the Python folder wherever your computer stores applications. 



OR



You can put all of the instructions in a file. Just be sure you save the file with the ending **.py** You can access that file in the interactive shell. Then Run the module from the module. 





# How Do I Do Math in Python? 

From the interactive shell you can just type in the expression you'd like to calculate. For example: 



> 26 + 3

or

> 50 / 4



You can find all of the mathematical operators python supports here: https://automatetheboringstuff.com/chapter1/#calibre_link-101.  





# **What types of data can I use?**

There are three types: 

**Integers** - whole numbers (e.g. 2345 or 3, or -5 )

**Floating Point numbers** - decimals (e.g. 2.5 or .313, or -5.90 )

**Strings** - text (e.g. 'Alice' or 'There is a cat.' or 'I ate 6 tacos')

HINT: Notice that the strings are in single quotes. You *have* to use the quotes. 





# **How to Store Data** 

Using *variables* is very powerful. It allows you to keep track of a value or text that may change over time. For example, what if you have 5 dollars in your wallet yesterday. In python, you can say: 



> wallet = 5



Then you can ask how much you have in your wallet? 



> wallet



You see the value 5. But what if today someone gives you 6 more dollars.



> wallet + 6



Ask how much money you have in your wallet now! (Hint, just type wallet) 

The rules for how you can name your variables is here: https://automatetheboringstuff.com/chapter1/#calibre_link-107. 





# **Comments** 

Comments are normally used in files of code, so people can (1) remember why they wrote the code they are seeing (2) help others understand what the code does or (3) quickly take out code from running without actually removing it. 

Any text following the # symbol in a Python file is not treated as an instruction to the computer, but rather as a hint to the reader. 



# **How do I get something to show on the screen** 

Use the print() function. Anything typed inside of the parentheses (in single quotes) will show on the screen. 

> print('Hi! I'm some text showing on the screen')



# **How do I ask the user to type something?**

The input() function accepts text from the user. However, you may want to print something first so the user knows what to write...

> print('Type your Name')

> name = input()



**How do I change something into a....**

Use each of the following functions to turn X into Y. Just put X inside of the function. 

- Whole Number / Integer  - the int() function
- Decimal **-** the float() function
- String - the str() function

For example

> int(‘27’)

will turn into the integer 27 instead of the string ‘27’. Why would you want to do this? This is helpful, because any information returned by the user through the input() is a string. You can't perform math as we understand it with a string. But you can perform math with the value (for example their age) once you convert it to an integer. 



OR

> int(‘27.6’)

will turn into the floating number 27.6 instead of the integer 27 so math can be performed with it
