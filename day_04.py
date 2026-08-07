# We can make a list inside of a list (DAY1) - Bootcamp
fam1 = ["khoni" , 505.2 , "Dad" ,62.5 , "Ape" , 562.3 , "Mom" , 25.6]
print(fam1)
print(type(fam1))

fam2 = [["khoni" , 505.2] , ["Dad" , 62.5 ] , ["Ape" , 562.3] , ["Mom" , 25.6]]
print(fam2)
print(type(fam2))

## Ansawers
['khoni', 505.2, 'Dad', 62.5, 'Ape', 562.3, 'Mom', 25.6]
<class 'list'>
[['khoni', 505.2], ['Dad', 62.5], ['Ape', 562.3], ['Mom', 25.6]]
<class 'list'>

## Reversing the numbers (DAY 2)

fam1 = 1 , 2 , 3 , 4 , 5
fam2 = 6 , 7 , 8 , 9 , 10

full = fam1 + fam2
print(full)

full_sorted = sorted(full, reverse=False)
print(full_sorted)

full_sorted1 = sorted(full , reverse=True)
print(full_sorted1)
print(type(full))
print(type(full_sorted1))

## Answers
(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
[10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
<class 'tuple'>
<class 'list'>
