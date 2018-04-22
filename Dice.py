import matplotlib.pyplot as plt
import numpy as np

# Set seed for reproducibility
np.random.seed(123)
all_walks = []

# Simulate random walk 100 times
for i in range(100) :
    random_walk = [0]
    for x in range(100) :
        step = random_walk[-1]
        # The above is to set the step as the last element in random_walk
        dice = np.random.randint(1,7)
        if dice <= 2:
            step = max(0, step - 1)
            # The above is to ensure number of steps cannot be negative
        elif dice <= 5:
            step = step + 1
        else:
            step = step + np.random.randint(1,7)
        if np.random.rand() <= 0.001 :
            step = 0
            # The above is to take into account clumsiness
        random_walk.append(step)
    all_walks.append(random_walk)

# Create and plot np_aw_t
# all_walks is a list of lists, so we need to convert this into a NumPy array to make interesting plots
# Transpose is needed to permute the dimensions of the array
np_aw_t = np.transpose(np.array(all_walks))

# I want to build a histogra of the endpoint of each simulation. Select last row from np_aw_t: ends
ends = np_aw_t[-1,:]

# Plot histogram of ends, display plot
plt.hist(ends)
plt.show()

# Find the estimated chance that I will reach 60 steps in this game
print("Chances of winning the bet = " + str(np.mean(ends > 60)*100) + "%" )
