```Python
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('test.csv')

list = ['202302220502',
        '202302220750',
        '202302181134',
        '202302132212',
        '202302080541',
        '202302121935',
        '202302240157',
        '202302052251',
        '202302270731',
        '202302131217', ]

list.sort()
df['time'] = list
x = df['time']
y = df['ratio']
plt.plot(x, y, marker='o', markersize=3)
for i, j in zip(x, y):
    plt.text(i, j, str(j))
# # Add chart title and axis labels
plt.title("Line Chart Title")
plt.xlabel("X Axis Label")
plt.ylabel("Y Axis Label")

plt.show()
```
