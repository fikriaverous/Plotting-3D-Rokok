import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import axis3d

# =========READ CSV=========

ax = plt.subplot(111, projection='3d')
df = pd.read_csv('data_perokok.csv')

# =========PLOT 3D=========
provinsi = [prov for prov in df.iloc[:,0]]
tahun_2015 = [data_2015 for data_2015 in df.iloc[:,1]]
tahun_2016 = [data_2016 for data_2016 in df.iloc[:,2]]

x1 = np.arange(34)
x2 = x1
y1 = np.array([1] * 34)
y2 = np.array([3] * 34)
z = np.zeros(34)

dx = [0.5] * 34
dy = [0.51] * 34
dz1 = tahun_2015
dz2 = tahun_2016

ax.bar3d(x1, y1, z, dx, dy, dz1)
ax.bar3d(x2, y2, z, dx, dy, dz2)

ax.set_ylabel('Y')
ax.set_zlabel('z')
plt.xticks(x1,provinsi,rotation=90)
plt.yticks([1,3],['2015','2016'])
plt.show()