'''
Homework 1:  Comma Code:
   Write a function that takes a list value as an argument and returns a string 
   with all the items separated by a comma and a space, with and inserted before 
   the last item. Your function should be able to work with any list value passed to it.
'''



def items():
   # Find length of list spam
   index=len(spam)
   
   # Find the last item in the list
   number=index-1
   variable=spam[0:number]
   
   #output is a string
   output=''
   
   #first time item=0, second time item=1
   for item in range(number):
       output += variable[item] + ', '
   output += 'and ' + spam[-1]
   
   #print
   print(output)
   
# Define spam List
spam=['apples', 'bananas', 'tofu', 'cats']

#Call our function
items() (edited) 
