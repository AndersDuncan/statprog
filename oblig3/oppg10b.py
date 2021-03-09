from scipy.stats import norm
import numpy as np
import matplotlib.pyplot as plt

weight = float(input("Please enter the weight you wish to compare to our bread in grams: "))

result = norm.cdf(weight,760,10)

print(f'There is a {result:.3f} chance that {weight:.2f} is heavier than our average bread weighting in at 760 grams!')

