import numpy as np
import statsmodels.api as sm
import matplotlib.pyplot as plt

#dtype was needed due to the different datatypes in the file
#skip_header was added to avoid errors with the function expecting another column due to the header.
#encoding had to be set due to the irregular nature of the file.
table = np.genfromtxt("csv/katters_vekt.csv", delimiter = ",", dtype = None, skip_header = 1, encoding = None)

weight = []
heartWeight = []
for x in table:
    #Loops through the np array and appends the values I want.
    weight.append(x[2])
    heartWeight.append(x[3])
    
#My qqplots needed a shape attribute, which is easily obtained by converting my arrays to numpy arrays
npWeight = np.array(weight)
npHeartWeight = np.array(heartWeight)
while True:
    show = input("Do you wish to see a plot for cat weight or heart weight? Or simply quit? ")
    catWord = "cat"
    heartWord = "heart"
    if catWord in show:
        #line = 's' makes a line that's standardized by the standard deviation.
        sm.qqplot(npWeight, line = 's')
        plt.show()
    elif heartWord in show:
        sm.qqplot(npHeartWeight, line = 's')
        plt.show()
    elif show == "quit":
        break
    else:
        print("Please answer with cat or heart")