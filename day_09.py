### Customisation
import matplotlib.pyplot as plt
year = [1950, 1951, 1952, 2100]
pop = [2.538, 2.57, 2.62, 10.85]
plt.plot(year, pop)
plt.show()

          ##This is the corrected to:
import matplotlib.pyplot as plt

year = [1950, 1951, 1952, 2100]
pop = [2.538, 2.57, 2.62, 10.85]

# Sort both lists by year
sorted_data = sorted(zip(year, pop))
year_sorted, pop_sorted = zip(*sorted_data)

plt.plot(year_sorted, pop_sorted)
plt.xlabel("Year")
plt.ylabel("Population (billions)")
plt.title("World Population Over Time")
plt.show()
          # lets label our graph
plt.plot(year, pop)
plt.xlabel('year')       # label and customise graph before showing the graph. (X AXIS)
                # plt.yscale('log') this gives the grapgh to be labeled on the side
plt.ylabel('population') # Y AXIS
plt.title('world population projections')   # TITLE
plt.yticks([0, 2, 4, 6, 8, 10])
plt.show()

# Scatter plot with customisations
plt.scatter(x = gdp_cap, y = life_exp, s = np.array(pop) * 2, c = col, alpha = 0.8)
c = col # for colour .this will give the graph colour
alpha = 0.8 # transparency, can be set from 0 to 1

# 1st customizations    this the the labelings of the graphs.
plt.xscale('log') 
plt.xlabel('GDP per Capita [in USD]')
plt.ylabel('Life Expectancy [in years]')
plt.title('World Development in 2007')
plt.xticks([1000,10000,100000], ['1k','10k','100k'])

# 2nd customizations 
plt.text(1550, 71, 'India')  # this names the specfic points on the graph
plt.text(5700, 80, 'China')

# Add grid() call
plt.grid(True) # this gives the graph grids
