import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# load example data
tips = sns.load_dataset("tips")
iris = sns.load_dataset("iris")
flights = sns.load_dataset("flights")
planets = sns.load_dataset("planets")
titanic =  sns.load_dataset("titanic")

#
# print(tips.head())
# print(iris.head())
# print(flights.head())
# print(planets.head())
# print(titanic.head())
#
# # 1. Distribution Plots
# plt.figure(figsize=(10,15))
# plt.subplot(1, 1, 1)
# sns.histplot(tips['total_bill'], kde=True)
# plt.title('Histogram and Kde Plot')
# plt.show()
#
# plt.subplot(3, 3, 2)
# sns.kdeplot(tips['total_bill'], shade=True)
# plt.title('kde plot')
# plt.show()
#
# plt.subplot(1, 1, 1)
# sns.ecdfplot(tips['total_bill'])
# plt.title('ecdf plot')
# plt.show()
#
# # categorical plots
# plt.subplot(1, 1, 1)
# sns.boxplot(x="day", y="total_bill", data=tips)
# plt.title('box plot')
# plt.show()
#
# plt.subplot(1, 1, 1)
# sns.violinplot(x="day", y="total_bill", data=tips)
# plt.title('violin plot')
# plt.show()
#
# plt.subplot(1, 1, 1)
# sns.barplot(x="day", y="total_bill", data=tips)
# plt.title('bar plot')
# plt.show()

# Create a scatter plot with hue
plt.subplot(1, 1, 1)
sns.scatterplot(x='age', y='fare', hue='class', style='sex', size='survived', data=titanic, legend=True)
plt.show()

# modding legend
plt.subplot(1, 1, 1)
sns.scatterplot(x='age', y='fare', hue='class', data=titanic)
plt.legend(title='Passenger Class', loc='upper right', bbox_to_anchor=(1.2, 1), fontsize='large')
plt.show()

# add legends to facet grid
plt.subplot(1, 1, 1)
sns.scatterplot(x='age', y='fare', hue='class', data=titanic)
plt.legend(title='Passenger Class', loc='upper right', bbox_to_anchor=(1.2, 1), fontsize='large')
plt.show()