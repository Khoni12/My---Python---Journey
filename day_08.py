# Using Matplotlib           # plt.plot
import matplotlib.pyplot as plt

year = [1950, 1970, 1990, 2010]
pop = [2.219, 3.692, 5.263, 6.972]
plt.plot(year,pop)          # To plot these in a line chart we use(line conected plotting)
plt.show()                  # this shows us the plotted data

                 # USING A SCTTER PLOT          # plt.scatter
import matplotlib.pyplot as plt
year = [1950, 1970, 1990, 2010]
pop = [2.219, 3.692, 5.263, 6.972]
plt.scatter(year,pop)      # this graph only shows the dots without the connetcing line
plt.show()

                 # Using the HISTOGRAM via Matplotlib     # plt.hist
import matplotlib.pyplot as plt          
## X-axis = list of values that i want to build a histogram for.
## Y-axis = how many bins the list should be divided

values = [0,0.6,1.4,1.6,2.2,2.5,2.6,3.2,3.5,3.9,4.2,6]
plt.hist(values,3)     ## the number 3 is to show how many bins(graphs) i want.
plt.show()
