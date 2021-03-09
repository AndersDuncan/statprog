import numpy as np
import scipy.stats as st

readings = np.genfromtxt("csv/salmonella.csv", delimiter = ",")
interval = float(input("Please give your confidence interval. "))
if interval > 1:
    interval = interval / 100
    
total = 0
for x in readings:
    #Gives every element in the array an exponent of 2, for the S² formula and adds them together. Much more compact and clean.
    total += x ** 2

#int containing the length of the array.
n = readings.size
#sums all elements in the array.
my = 1 / n* np.sum(readings)   
S2 = 1 / (n- 1) * (total - n* (my ** 2))
sigmaEstimate = np.sqrt(S2)

#Both of these use (alpha/2,v)
chiSquare = st.chi2.isf((1-interval)/2,readings.size-1)
chiSquareNegative = st.chi2.ppf((1-interval)/2,readings.size-1)

lowerLimit = np.sqrt(((n-1) * S2) / chiSquare)

upperLimit = np.sqrt(((n-1) * S2) / chiSquareNegative)

print(f"The point estimate for σ = {sigmaEstimate:.1f} \nThe {interval * 100:.0f} confidence interval is [{lowerLimit:.1f}, {upperLimit:.1f}]")