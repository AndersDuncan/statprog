from scipy import stats
from statsmodels.stats import proportion

n = int(input("What is your sample size? "))
x = int(input("What share answered favourably? "))
interval = float(input("Please give your confidence interval. "))
if interval > 1:
    interval = interval / 100

p = x / n
#Rule 6.12 from the course book.
if n*p*(1-p) >= 5:
    print("This checks out as a normal approximation")
else:
    print("This does not check out as a normal approximation")
    
#proportion_confint(favoured_answers, sample size, alpha)
result = proportion.proportion_confint(x, n, 1-interval)
print(f'{result}')