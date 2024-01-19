import math
version = '1.0'
print(f"Welcome to delta-V calculator v1.0!\n\n")
wmass = float(input("Please enter wet mass: "))
dmass = float(input("Please enter dry mass: "))
isp = float(input("Please enter Isp: "))
g0 = 9.80665
dv = isp * g0 * math.log(wmass/dmass)
print(round(dv, 2))