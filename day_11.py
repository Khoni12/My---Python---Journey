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

# DataFrame for CSV File
# eg. brics.csv   (CSV - Comma Separated Values)

#### example 2

# Pre-defined lists
names = ['United States', 'Australia', 'Japan', 'India', 'Russia', 'Morocco', 'Egypt']
dr =  [True, False, False, False, True, True, True]
cpc = [809, 731, 588, 18, 200, 70, 45]

# Import pandas as pd
import pandas as pd

# Create dictionary my_dict with three key:value pairs: my_dict
my_dict = {'country':names, 'drives_right': dr, 'cars_per_cap': cpc}      ### here we dont put quotes on tha values because they represent values(recocnised vaules.)

# Build a DataFrame cars from my_dict: cars
cars = pd.DataFrame(my_dict)
print(cars)

                  ### answers
  country  drives_right  cars_per_cap
0  United States          True           809
1      Australia         False           731
2          Japan         False           588
3          India         False            18
4         Russia          True           200
5        Morocco          True            70
6          Egypt          True            45
