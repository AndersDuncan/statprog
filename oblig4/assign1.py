import random
import matplotlib.pyplot as plt
import numpy as np

throws = int(input("How many dice throws should I do? "))
rounds = int(input("How many times should I do it? "))

throwArray = []
roundArray = []

for x in range(rounds):
    #clears the array filled with throws before every round.
    throwArray.clear()
    for y in range(throws):
        throwArray.append(random.randint(1,6))
    #Appends the mean of our throws to the round array.
    roundArray.append(np.mean(throwArray))
    
standardDeviation = np.std(roundArray, ddof = 1)
totalMean = np.mean(roundArray)
print(f"The standard deviation of the average rounds are: {standardDeviation:.2f} \nThe mean of the.. means are: {totalMean:.2f}")

#bins = 30 specifies 30 columns
plt.hist(roundArray, density = True, bins = 30)
plt.ylabel("Probability")
plt.xlabel("Average")
plt.show()