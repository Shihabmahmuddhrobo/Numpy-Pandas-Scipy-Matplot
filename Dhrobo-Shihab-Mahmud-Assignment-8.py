#!/usr/bin/env python3

import mymodule
import platform
import numpy as np
import pandas as pd
import scipy.constants
import matplotlib.pyplot as plt


mymodule.greeting(mymodule.person1["name"]) #Use mymodule.py
print("Name:", mymodule.person1["name"])
print("Age:", mymodule.person1["age"])
print("Country:", mymodule.person1["country"])
print()
mymodule.greeting(mymodule.person2["name"])
print("Name:", mymodule.person2["name"])
print("Age:", mymodule.person2["age"])
print("Country:", mymodule.person2["country"])

print("\n")
print("Platform:", platform.system()) # Print platform information

print("\n")
random_number = np.random.randint(0, 1001)# Generate a random number from 0 to 1000 using NumPy
print("My random number is:", random_number)


df = pd.read_csv("visitor_statistics.csv") #Load visitor_statistics.csv into a DataFrame and display it
print("\n", df)


print("\n") #Print seconds in different time units using SciPy
print("Units in seconds:")
print("Minute:", scipy.constants.minute)
print("Hour:", scipy.constants.hour)
print("Day:", scipy.constants.day)
print("Week:", scipy.constants.week)
print("Year:", scipy.constants.year)


df.plot(x="Date", y="All visitors", legend=True)  #Plot visitor statistics
plt.show()
