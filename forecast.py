import random
import matplotlib.pyplot as plt

# We are going to use a Monte Carlo simulation and Takt times
# to estimate the total time needed to complete a set of stories
# (let's call the set of stories an epoch).

# First, go out and collect the actual Takt times from stories
# in previous sprints. This should be real data based on real,
# completed sprints.
historical_takt_times = [1.5, 1.7, 1.9, 2.8, 3.5, 3.8, 10]

# How many stories are in the epoch?
number_of_stories = 10

# How many trials do you want to do for the Monte Carlo simulation?
# Ten thousand trials is a pretty good place to start.
number_of_trials = 10000

# The output data from the Monte Carlo simulation. We will use it
# to plot a histogram of the results.
estimated_times = []

# We are going to repeat this process equal to the number of trials.
for x in range(number_of_trials):
    # Set the total time of the epoch equal to zero.
    total_time = 0
    # For each story in number_of_stories, randomly select a historical
    # Takt time and add it to the total time.
    for y in range(number_of_stories):
        time = random.choice(historical_takt_times)
        total_time += time
    # Append the total time to the list of simulated times
    estimated_times.append(total_time)

# Plot the results
plt.hist(estimated_times, bins="auto")
plt.title("Histogram of Estimated Epoch Times")
plt.show()
