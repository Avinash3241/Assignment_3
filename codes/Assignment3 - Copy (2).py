from scipy.stats import binom
from matplotlib import pyplot as plt
x=[i for i in range(0,6)]
y = [binom.pmf(i,5,0.1) for i in x]
plt.stem(x,y)
plt.show()
print(y[0])