import numpy as np
import matplotlib.pyplot as plt

csv = np.genfromtxt ('datamat5to13.csv', delimiter=",")
nums=range(5,5+csv.shape[0])
meantime=np.mean(csv,axis=1)
plt.plot(np.power(2, nums),meantime)
plt.xlabel("Number of vertices")
plt.ylabel("Time [s]")
plt.show()
for x,y in zip(csv,nums):
    plt.hist(x, bins=20)
    plt.ylabel('Time [s]')
    plt.xlabel(f"2^{y} vertices")
    plt.show()