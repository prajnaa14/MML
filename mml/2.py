import csv 
from statistics import mean 
import matplotlib.pyplot as plt 
 
# Lists to store height and weight data 
height = [] 
weight = [] 
 
# Read data from CSV file 
with open("C:\\Users\\PRAJNA\\Downloads\\heights.csv", newline="") as csvfile:  # Corrected file path 
    reader = csv.DictReader(csvfile) 
    for row in reader: 
        height.append(float(row['heights'])) 
        weight.append(float(row['weights'])) 
 
# Calculate mean values 
mean_height = mean(height) 
mean_weight = mean(weight) 
 
# Calculate deviations and other variables 
n = len(height) 
dev_height = sum((h - mean_height) ** 2 for h in height) 
dev_weight = sum((w - mean_weight) ** 2 for w in weight) 
prod_dev = sum((height[i] - mean_height) * (weight[i] - mean_weight) for i in 
range(n)) 
 
# Calculate slope (m) and intercept (b) for the linear regression equation 
m = prod_dev / dev_height 
b = mean_weight - (m * mean_height) 
 
# Get user input for height and calculate the corresponding weight using the linear regression model 
sample = float(input("Enter the Height: ")) 
solution = (m * sample) + b 
 
print(f"Predicted Weight for Height {sample} is approximately {solution:.2f} pounds.") 
 
# Plotting 
plt.scatter(height, weight, label='height vs weight plotting') 
plt.plot(height, [m * x + b for x in height], color='red', label='Linear Regression') 
plt.xlabel('height') 
plt.ylabel('weight') 
plt.title('Linear Regression for height and weight') 
plt.legend() 
plt.show() 