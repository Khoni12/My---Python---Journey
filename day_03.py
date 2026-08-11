Day_03.py
learnt about methods, sorted, reverse(False,True) , capitalize, index, replace 
EXAMPLE:
x = [1,2,3,4,5,6,7]
>>> y = [8,9,10,11,12,13,14,15]
>>> full = x + y
>>> full_sorted = sorted(full, reverse=True)
>>> print(full_sorted)
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]


fam = ["dad", 1 , 2, 3, "mom", 4]
>>> fam.index("mom")
4
>>> fam.count(4)
1

"dad".capitalize()
'Dad'
>>> "dad".replace("d", "day")
'dayaday'
>>> fam.append("me")
>>> print(fam)
['dad', 1, 2, 3, 'mom', 4, 'me']


.append(), that adds an element to the list it is called on (for it to work , dont add anything inside the parenthesis)
.remove(), that removes the first element of a list that matches the input, and
.reverse(), that reverses the order of the elements in the list it is called on.
