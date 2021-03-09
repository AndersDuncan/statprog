from scipy.stats import norm
from scipy.stats import poisson
import numpy as np
import matplotlib.pyplot as plt

#Oppgave 7
def assignment_7():
	parameter = float(input("What is your desired parameter? "))
	upper = float(input("What is your desired upper limit? "))

	x = np.arange(0, upper, 0.5)

	plt.plot(x, poisson.pmf(x,parameter), label = "P(X = x)")
	plt.legend()
	plt.show()



#Oppgave 10a
def assignment_a():
	x = np.arange(720,800,1)

	plt.plot(x,norm.pdf(x,760,10))
	plt.xlabel("x")
	plt.ylabel("f(x)")
	plt.title("Normalfordeling")
	plt.show()



#Oppgave 10b
def assignment_b():
	weight = float(input("Please enter the weight you wish to compare to our bread in grams: "))

	result = norm.cdf(760,weight,10)

	print(f'There is a {result*100:.2f}% chance that {weight:.2f} is lighter than our average bread!')


#All this is just for choosing the assignment you wish to see, just ignore.

assignment = input("Do you wish to see the solution to 7 or 10? ")

if assignment == "7":
	assignment_7()

elif assignment == "10":
	subAssignment = input("Do you wish to see the solution to a or b? ").lower()
	if subAssignment == "a":
		assignment_a()
	elif subAssignment == "b":
		assignment_b()
	else:
		print("Please input either a or b")
		exit()

else:
	print("Please input either 7 or 10")
	exit()

