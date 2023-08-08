# Importing necessary libraries
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
#import codecademylib3 # A library used for Codecademy projects.

# Read in the dataset from a csv file.
population = pd.read_csv("salmon_population.csv")
# Extract the 'Salmon_Weight' column and convert it to a numpy array
population = np.array(population.Salmon_Weight)
# Calculate the mean of the population and round it to 3 decimal places.
pop_mean = round(np.mean(population),3)

## Plotting the Population Distribution
# Create a histogram of the population data with seaborn.
sns.histplot(population, stat='density')
# Add a vertical line at the mean value (red dashed line).
plt.axvline(pop_mean,color='r',linestyle='dashed')
# Set the title of the plot.
plt.title(f"Population Mean: {pop_mean}")
# Set the x-axis label of the plot.
plt.xlabel("Weight (lbs)")
# Display the plot.
plt.show()
# Clear the current figure for new plots.
plt.clf()

# Set the sample size.
samp_size = 10
# Generate a random sample of size samp_size from the population without replacement.
sample = np.random.choice(np.array(population), samp_size, replace = False)

# Calculate the mean of the sample.
sample_mean = np.mean(sample)
print(f"This is the mean of sample {sample_mean}")

# Uncomment the lines below to plot the sample data:
# Create a histogram of the sample data with seaborn.
sns.histplot(sample, stat='density')
# Add a vertical line at the sample mean value (red dashed line).
plt.axvline(sample_mean,color='r',linestyle='dashed')
# Set the title of the plot.
plt.title(f"Sample Mean: {sample_mean}")
# Set the x-axis label of the plot.
plt.xlabel("Weight (lbs)")
# Display the plot.
plt.show()









# To explain replace in np.random.choice()

# # Generar una muestra con reemplazo (un elemento puede ser seleccionado más de una vez)
# sample_with_replacement = np.random.choice(array, size=10, replace=True)
# print("Muestra con reemplazo:", sample_with_replacement)

# # Generar una muestra sin reemplazo (un elemento solo puede ser seleccionado una vez)
# # Nota: el tamaño de la muestra debe ser menor o igual al tamaño del array
# sample_without_replacement = np.random.choice(array, size=5, replace=False)
# print("Muestra sin reemplazo:", sample_without_replacement)