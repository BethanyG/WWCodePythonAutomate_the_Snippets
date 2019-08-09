# Chapter 4 - Lists



_Pop Quiz: What are the other data types we have learned thus far?_ 



# Today we learn about: 

- lists - a changeable sequence of values
- index - the location of an item in the list
- slices - a subset of a defined list (output as a smaller list)
- tuples - an unchangeable sequence of values





# Lists



## How can I store a list of my favorite foods? 

You can create a list value that tracks each item in a list. The proper syntax looks like this: 



```
[‘cake’, ‘strawberries’, ‘macaroni and cheese’]
```



Each item is contained by quotes, delimited by a comma and the list is written between two [ ]. 





## What is the list data type used for? 

The list is a value that it is used to store a sequence of other values. Since this list is a value itself it can be assigned to a variable. 



```
yummy_foods = [‘cake’, ‘strawberries’, ‘macaroni and cheese’]
```



## How do I access certain elements of the list I created? 

You refer to them by their location within the list, or their index. Items in the list start at index 0, and increase by one. For example, my favorite food cake is located at `yummy_foods[0]` and my third favorite food is located at `yummy_foods[2]`.



## Can I store multiple lists in the same variable? 

Yes you can! Remember, lists are values too. 



```
kitchen = [[‘spinach’, ‘broccoli’, ‘kale’], [‘bananas’, ‘apples’, ‘oranges’]]
```



So if you can assign one value to a variable, you can assign a list to a variable, and inside of that list it can contain other lists. 



In my kitchen, the here are my list of fruits: 



```
kitchen[1]
```



In my kitchen, the broccoli is 2nd item [0] in the first list[0]



```
kitchen[0][1]
```

##  

## How do I refer to the last item in a list? 

Since it is possible you have no idea how long the list is, you use [-1] to refer to the last item in the list, [-2] the second to last item on the list, etc. 



In my kitchen, the last fruit item I listed is: 



```
kitchen[1][-1]
```





How do I refer to a part of the list? 

You refer to just a portion, or a slice, of the list by stating which index to start with and up to be NOT include the last item mentioned. So 



`yummy_foods[1:3] `means, to start with item `yummy_foods[1]`, and then also `yummy_foods[2] `but stop when you hit `yummy_foods[3]`.



`yummy_foods[0:-1]` means, include everything in the list, except the last item. 



## List shortcuts



`yummy_foods[:]` - everything in the list

`yummy_foods[0:] `- include everything from start to end of list

`yummy_foods[1:]` - include everything from the 2nd item in the list to the end

`yummy_foods[:1] `- everything until index 1





## How many values are in the list?



```
len(yummy_foods)
```



How did I change items in my list? 

If I meant to say my favorite food was cookies instead of cake, I can say: 

```
yummy_foods[0] = 'cookies'
```



How do I delete items from the list? 

Use the `del` keyword and refer to it's index. 

```
del yummy_foods[1]
```



# Practice Questions

1. What is`[]`? An empty list
2. How would you assign the value `'hello'` as the third value in a list stored in a variable named `spam`? (Assume `spam` contains `[2, 4, 6, 8, 10]`.) spam[2] = 'hello'
3. For the following three questions, let’s say `spam` contains the list `['a', 'b', 'c', 'd']`. What does `spam[int(int('3' * 2) // 11)]` evaluate to? 'd'
4. What does`spam[-1]` evaluate to? 'd'
5. What does `spam[:2]` evaluate to?  'a', 'b'
6. For the following three questions, let’s say `bacon` contains the list `[3.14, 'cat', 11, 'cat', True]`. What does`bacon.index('cat')` evaluate to? 1
7. What does `bacon.append(99)` make the list value in `bacon` look like? `[3.14, 'cat', 11, 'cat', True, 99]`
8. What does `bacon.remove('cat')` make the list value in `bacon` look like? `[3.14, 11, 'cat', True, 99]`
9. What are the operators for list concatenation and list replication? + and *
10. What is the difference between the `append()` and `insert()` list methods? append adds it to the end, insert places it at a specific index
11. What are two ways to remove values from a list? *remove() or del*
12. Name a few ways that list values are similar to string values.
13. Both lists and strings can be passed to `len()`, have indexes and slices, be used in `for` loops, be concatenated or replicated, and be used with the `in` and `not in` operators.
14. What is the difference between lists and tuples? 
15. *Lists can be changed, appended or modified and use []. Tuples cannot be changed, but must be overwritten and use ().*
16. How do you type the tuple value that has just the integer value `42` in it? *(42,)* 
17. How can you get the tuple form of a list value? `tuple(['i', 'am', 'a', 'list']` How can you get the list form of a tuple value?` list(('i', 'am', 'a', 'list'))`
18. Variables that “contain” list values don’t actually contain lists directly. What do they contain instead? *The reference to the list*
19. What is the difference between`copy.copy()` and `copy.deepcopy()`? *copy.copy() copies the values of a list into a new list. copy.deepcopy() copies the lists of a list
