from scipy.stats import binom
import numpy as np
import matplotlib.pyplot as plt

n = int(input("How many attempts should I run? "))
p = float(input("What is the probability of your experiment? "))
if p > 1:
	p = p/100
k = np.arange(n+1)


#plt.plot(binom.cdf(k,n,p), marker = ".", label="F(x) = P(X <= x)")
plt.plot(binom.pmf(k,n,p), marker = ".", label="P(X = x)")
plt.legend()
plt.show()