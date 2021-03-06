import numpy as np
import pandas as pd

input_file = "3_floor.csv"

# comma delimited is the default
df = pd.read_csv(input_file, header = 0)

# for space delimited use:
# df = pd.read_csv(input_file, header = 0, delimiter = " ")

# for tab delimited use:
# df = pd.read_csv(input_file, header = 0, delimiter = "\t")

# put the original column names in a python list
original_headers = list(df.columns.values)

# remove the non-numeric columns
df = df._get_numeric_data()

# put the numeric column names in a python list
numeric_headers = list(df.columns.values)

# create a numpy array with the numeric values for input into scikit-learn
numpy_array = df.as_matrix()

# reverse the order of the columns
#numeric_headers.reverse()
#reverse_df = df[numeric_headers]

# throughput random forest regression
t = numpy_array[0:160, 3]
x = np.linspace(0, 159, 160)
xall = np.linspace(0, 181, 182)
xtest = np.linspace(160, 181, 22)

from sklearn.ensemble import RandomForestRegressor
#tfit = RandomForestRegressor(100).fit(x[:, None], t).predict(x[:, None])
tfit = RandomForestRegressor(100).fit(numpy_array[0:160, 0:2 ], t).predict(numpy_array[0:182, 0:2])

import matplotlib.pyplot as plt
fig, ax = plt.subplots()

ax.errorbar(x, t, 0.3, fmt='*', label="Training traffic")
ax.plot(xall, tfit, '-r', label="Predicted traffic")
ax.errorbar(xtest, numpy_array[160:182, 3], fmt='og', label="Test traffic")
ax.set_ylabel('Throughput (kbits/second)')
ax.set_xlabel('Time in hours')
ax.set_title('Taffic Prediction with Random Forest Regression on 3rd floor')
ax.legend(loc="upper left")

plt.show()

