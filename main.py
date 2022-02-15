import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
x = [782.205,783.27,787.329,786.263]
y = [70.4489,72.1678,69.6524,67.9335]
plt.plot(x,y,"bo-",linewidth=2,markersize=12,label="First")
#plt.axis([640,690,775,960])
plt.legend(loc="upper left")
plt.show()