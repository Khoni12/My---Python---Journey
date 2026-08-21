## PANDAS
import pandas as pd
# we can use pandas to create a table , we can also build it from a dictionary.
                ### example
dict = {
    "country": ["brazil", "russia", "india", "china", "south africa"],
    "capital": ["brazilia", "moscow", "new delhi", "beijing", "pretoria"],
    "area": [8.516, 17.10, 3.286, 9.597, 1.221],
    "population": [200.4, 143.5, 1252, 1357, 52.98]}

Bricks = pd.DataFrame(dict)
print(Bricks)

                  ### ANSWERS
        country    capital    area  population
0        brazil   brazilia   8.516      200.40
1        russia     moscow  17.100      143.50
2         india  new delhi   3.286     1252.00
3         china    beijing   9.597     1357.00
4  south africa   pretoria   1.221       52.98

Bricks.index = ["BR", "RU", "IN", "CH", "SA"]              # This will change the numbers to being labeled
print(Bricks)

                  ### ANSWERS
       country    capital    area  population
 BR        brazil   brazilia   8.516      200.40
 RU        russia     moscow  17.100      143.50
 IN         india  new delhi   3.286     1252.00
 CH         china    beijing   9.597     1357.00
 SA  south africa   pretoria   1.221       52.98
