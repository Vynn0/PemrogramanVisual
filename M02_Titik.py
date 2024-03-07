import numpy as np
import matplotlib.pyplot as plt

x1 = 100; y1 = 200 
x2 = 700; y2 = 700

lw = int(15)

hw = int(lw/2)

col = int(800)
row = int(800)
#col = int(5/7 * 1920)
#row = int(5/7 * 1080)
print('col, rpw =', col, ',', row)

Gambar = np.zeros(shape = (row, col, 3), dtype = np.uint8)
Gambar[:, :, :] = 255

Gambar[y1, x1, :] = 0
Gambar[y2, x2, :] = 0
Gambar[y1, x1, 0] = 255
Gambar[y2, x2, 0] = 255

for i in range (x1 - hw, x1 + hw):
    for j in range (y1 - hw, y1 + hw):
        if ( (i - x1) **2 + (j - y1) ** 2) < hw **2:
            Gambar[j, i, :] = 0
            Gambar[j, i, 0] = 255

for i in range(x2 - hw, x2 + hw):
    for j in range(y2 - hw, y2 + hw):
        if ( (i - x2)**2 + (j - y2) **2 ) < hw **2:
            Gambar[j, i, :] = 0
            Gambar[j, i, 0] = 0

plt.figure()
plt.imshow(Gambar)
plt.show()