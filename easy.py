#find the area of a triangle
#ask for base input
import time
t0 = time.time()
base = float(input("tell me the length of base: "))
#ask for the hight
hight = float(input("tell me the hight: "))
#formula to find the area
if base and hight != 0:
    area = (base * hight) / 2
    # print statement
    print("The area is:", area)
else:
    print("The base or hight cannot be 0")

print("--- %s seconds ---" % (time.time() - t0))







