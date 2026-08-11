  #### numpy

# having a list consisting of 5000 items
np.mean(np_city[:,0])                   # eg. To find the mean of that number sequence
np.meadian(np_city[:,0])                # e.g To find the median of the number sequence 
  #[:,0] this means that python takes the full list into consideration. from 0 till 5000

### ACTIVITY
avg = np.mean(np_baseball[:,0])                              # 1
print("Average: " + str(avg))

# Print median height                                        # 2
med = np.median(np_baseball[:,0])
print("Median: " + str(med))

# Print out the standard deviation on height                 # 3
stddev = np.std(np_baseball[:,0])
print("Standard Deviation: " + str(stddev))

# Print out correlation between first and second column      # 4
corr = np.corrcoef(np_baseball[:,0], np_baseball[:,1])
print("Correlation: " + str(corr))

                        # ANSWERS
Average: 73.6896551724138                # 1
Median: 74.0                             # 2
Standard Deviation: 2.312791881046546    # 3
Correlation: [[1.         0.53153932]    # 4
 [0.53153932 1.        ]]
