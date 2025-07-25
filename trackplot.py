import matplotlib.pyplot as plt

f = open("track.txt","r")

x_list = []
y_list = []

for line in f:
   var = line.split()

   t = float(var[0])
   x = float(var[1])
   y = float(var[2])
   print("t = ", t, ", x = ", x, ", y = ", y)

   x_list.append(x)
   y_list.append(y)

f.close()

plt.plot(x_list, y_list, "o")

plt.xlabel("x/m")
plt.ylabel("y/m")

plt.show()