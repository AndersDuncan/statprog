import numpy as np

data = np.genfromtxt('heights.csv', delimiter=',')
data.sort()
print(f'This is our data sorted in an ascending order: {data}')
print(f'Median = {np.median(data)}')
print(f'Mean = {np.around(np.mean(data), decimals = 2)}')
#ddof = 1 is needed as the calculation is N - ddof, default ddof is 0 and we wish to use the formula N - 1.
print(f'Variance = {np.around(np.var(data, ddof=1), decimals = 2)}')
print(f'Standard Devation = {np.around(np.std(data, ddof=1), decimals = 2)}')