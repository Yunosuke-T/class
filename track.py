import math

f = open("track.txt","w")

num = input(">>> ")

a = float(num)
theta = math.pi * a / 180.
print("a = ", a, ", theta = ", theta)

v0 = 10.
vx = v0 * math.cos(theta)
vy = v0 * math.sin(theta)
print("vx, vy = ", vx, ", ", vy)

x = 0.
y = 0.
g = 9.8

for i in range(0,1000,1):
   t = i * 0.01
   x = vx * t
   y = vy * t - 0.5 * g * t**2
   if y < 0:
      break
   print("t,x,y = ",t, ", ",x, ", ",y)
   f.write(str(t) + " " + str(x) + " " + str(y) + "\n")

f.close()