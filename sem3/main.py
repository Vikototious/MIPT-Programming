import numpy as np
import matplotlib.pyplot as plt
import pandas as pd



data = pd.read_csv('iris_data.csv')

print(set(data['Species']))

x_s = np.array(data.loc[data['Species'] == 'Iris-setosa', 'SepalWidthCm'])
y_s = np.array(data.loc[data['Species'] == 'Iris-setosa', 'SepalLengthCm'])

x_vi = np.array(data.loc[data['Species'] == 'Iris-virginica', 'SepalWidthCm'])
y_vi = np.array(data.loc[data['Species'] == 'Iris-virginica', 'SepalLengthCm'])

x_ve = np.array(data.loc[data['Species'] == 'Iris-versicolor', 'SepalWidthCm'])
y_ve = np.array(data.loc[data['Species'] == 'Iris-versicolor', 'SepalLengthCm'])

#{'Iris-setosa', 'Iris-virginica', 'Iris-versicolor'}


plt.scatter(x_s, y_s)
plt.scatter(x_vi, y_vi)
plt.scatter(x_ve, y_ve)

plt.show()