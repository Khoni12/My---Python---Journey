 ### USING NUMPY

#the function of using Arrays is to perform calculations on lists.

height = [ 1.73 , 1.68 , 1.71 , 1.89 , 1.79 ]
import numpy as np
np_height = np.array(height)
print(np_height)
     #answer :[1.73 1.68 1.71 1.89 1.79]

weight = [ 65.4 , 59.2 , 63.6 , 88.4 , 68.7 ]
np_weight = np.array(weight)
print(np_weight)
      #answer: [65.4 59.2 63.6 88.4 68.7]

bmi = np_weight / np_height **2
print(bmi) 
# answer bmi = array([21.85171573 , 20.97505669 ,  21.75028214 , 24.7473475 , 21.44127836])

## using numpy by using booleans
bmi > 23
print(bmi > 23)
       # answer : [False False False  True False]
####### Numpys dont have an indexs!!!!!

               ## 2D arrays 
import numpy as np

baseball = [[180, 78.4],
            [215, 102.7],
            [210, 98.5],
            [188, 75.2]]

# Create a 2D numpy array from baseball: np_baseball
np_baseball = np.array(baseball)
   #answer
[[180.   78.4]
 [215.  102.7]
 [210.   98.5]
 [188.   75.2]]

# Print out the type of np_baseball
print(np_baseball.shape)
      #Answer (4, 2)
<class 'numpy.ndarray'>
