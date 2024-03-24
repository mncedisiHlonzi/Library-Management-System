#TASK 3
import pandas as pd

insurance_data = pd.read_csv("C:\\Users\\mnced\\library-management-system\\task3\\motor_insure.csv\\motor_data11-14lats.csv")

print("First 10 records:")
print(insurance_data.head(10))

filtered_data = insurance_data[(insurance_data['SEATS_NUM'] > 40)]

print("\nRecords for make and usage for SEATS_NUM > 40:")
print(filtered_data[['MAKE', 'USAGE', 'SEATS_NUM']])

import matplotlib.pyplot as plt

insurance_data['EFFECTIVE_YR'] = pd.to_numeric(insurance_data['EFFECTIVE_YR'], errors='coerce')

plt.plot(insurance_data['EFFECTIVE_YR'], insurance_data['CARRYING_CAPACITY'])
plt.ylabel('EFFECTIVE_YR')
plt.xlabel('CARRYING_CAPACITY')
plt.title('CARRYING_CAPACITY vs EFFECTIVE_YR')
plt.grid(True)
plt.show()