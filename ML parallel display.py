
import matplotlib.pyplot as plt
from pandas.plotting import parallel_coordinates
plt.figure(figsize=(20,10))
parallel_coordinates(dataset.drop("Id",axis=1),"species")
plt.title('Parallel Coordinates Plot', fontsize=16,fontweight='bold')
plt.xlabel('Features',fontsize=12)
plt.ylabel('Features values',fontsize=12)
plt.legend(loc=1, prop={'size':20},frameon=True,shadow=True, facecolor="white",
           edgecolor="black")

plt.show()
