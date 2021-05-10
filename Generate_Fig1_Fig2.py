import matplotlib.pyplot as plt

data1 = [[3.14, 6.5, 8.71, 17.79, 20.83, 113.61, 313.77, 0, 0, 11.13, 17.8, 27.35, 67.17, 61.17, 266.54, 1953.96, 0, 0, 18.12, 31.51, 49.85, 118.9, 109.23, 442.75, 2801.82]]  
data2 = [[5.16, 8.5, 13.75, 31.81, 36.31, 138.71, 872.85, 0, 0, 12.32, 20.18, 31.72, 79.13, 74.86, 286.86, 2413.44, 0, 0, 20.15, 34.19, 55.16, 132.66, 125.03, 472.11, 3369.54]]  


X = np.arange(25)


fig, (ax1) = plt.subplots(1,1, figsize=(5, 4))
plt.subplots_adjust(left=None, bottom=None, right=None, top=None, wspace=0.1, hspace=None)

fig, (ax2) = plt.subplots(1,1, figsize=(5, 4))
plt.subplots_adjust(left=None, bottom=None, right=None, top=None, wspace=0.1, hspace=None)


ax1.bar(X + 0.00, data1[0], color = ['C9', 'C1', 'C2', 'C8', 'C5', 'C0', 'C7', 'C8','C9'], width = 0.75)
ax2.bar(X + 0.00, data2[0], color = ['C9', 'C1', 'C2', 'C8', 'C5', 'C0', 'C7', 'C8','C9'], width = 0.75)



ax1.grid(color ='grey', linestyle='-', linewidth = 0.30, alpha = 0.5)
ax2.grid(color ='grey', linestyle='-', linewidth = 0.30, alpha = 0.5)
ax1.set_yscale('log')   
ax2.set_yscale('log')


plt.show()