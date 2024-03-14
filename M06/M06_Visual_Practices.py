import matplotlib.pyplot as plt

# Data sampel
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

fig, ax = plt.subplots()
ax.plot(x, y, label='Data')

# Kondisi untuk scatter
for i in range(len(x)):
    if y[i] > 5 and x[i] > 3: 
        ax.scatter(x[i], y[i], color='red', label='Poin Y > 5 & Poin X > 3')
    else:
        ax.scatter(x[i], y[i], color='blue', label='Poin Y <= 5 & Poin X < 3')

ax.legend()
plt.show()
