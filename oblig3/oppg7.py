from scipy.stats import poisson
import numpy as np
import matplotlib.pyplot as plt


parameter = float(input("What is your desired λt? "))
upper = float(input("What is your desired upper limit? "))

x = np.arange(0, upper, 0.5)

plt.plot(x, poisson.pmf(x,parameter), label = "P(X = x)")
plt.legend()
plt.show()