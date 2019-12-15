import numpy as np
import matplotlib.pyplot as plt

filename = 'indians-diabetes.data.csv'
rawdata = open(filename, 'r')
data = np.loadtxt(rawdata, delimiter=',')
col1 = data[:, 0]
col9 = data[:, -1]
col3 = data[:, 2]
age = data[:, -2]
skin = data[:, 3]
# plt.plot(col1, col9, 'r*')
# plt.plot(col1, col3,'bD')
plt.xlabel("-------------age----------   ")
plt.ylabel("---------skin------------")
plt.plot(age, skin, 'go')
plt.show()
