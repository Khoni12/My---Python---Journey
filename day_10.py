###  DICTIONARIES
# WE USE CURLY BRACKETS FOR DICTIONARIES {}
            ## Exercise 
europe = { 'spain': { 'capital':'madrid', 'population':46.77 },
           'france': { 'capital':'paris', 'population':66.03 },
           'germany': { 'capital':'berlin', 'population':80.62 },
           'norway': { 'capital':'oslo', 'population':5.084 } }

# To find the population of france we use:
print(europe['france']['capital'])
# To add Ítaly with its capital named rome to the Dictionary:
data = {'capital':'rome', 'population': 90.25} ,         # we are defining our list for easy adding to the dictionary.
# To add the data list to the Dictionary:
europe['italy'] = data                                   # this will add the data to the europe dictioanry.
print(europe)
             ### ANSWER
{'spain': {'capital': 'madrid', 'population': 46.77}, 
 'france': {'capital': 'paris', 'population': 66.03}, 
 'germany': {'capital': 'berlin', 'population': 80.62}, 
 'norway': {'capital': 'oslo', 'population': 5.084}, 
 'italy': {'capital': 'rome', 'population': 90.25}}  ### Italy and its info was added to the dictionary.
