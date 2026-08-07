## counting
family = ["khoni" , 25.6 , "mom" , 15.25 , "dad" , 75.5 , "ape" , 85.2]
family.index("dad") #gives the number at which "dad"is placed
family.count(85.2) #counts the times tht number appears on the list.
print(family.count(85.2))

## Answers
4
1

sister = 'liz'
sister.capitalize() #capitaizes the first letter = Liz
sister.replace("z","sa") # replaced the "z" with "sa" = lisa

family2 = ["khoni" , 25.6 , "mom" , 15.25 , "dad" , 75.5 , "ape" , 85.2]
family2.append("me") #added "me" to the list
print(family2)

## Answers
['khoni', 25.6, 'mom', 15.25, 'dad', 75.5, 'ape', 85.2, 'me']

                   #### NB!!
##.append(), that adds an element to the list it is called on, takes one at a time!
##.remove(), that removes the first element of a list that matches the input, and
##.reverse(), that reverses the order of the elements in the list it is called on.


   ## USING IMPORTS

import numpy
numpy.array([1 , 2 , 3])
import numpy as np
np.array([1 , 2 , 3])

   # Only wanting to usethe array function instead of numpy, we use...
from numpy import array
