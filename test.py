
import matplotlib.pyplot as plt
years = [1000,1500,1600,1700,1750,1800,1850,
        1900,1950,1960,1965,1970,1975,1980,
        1985,1990,1995,2000,2005,
        2010,2015]

pops = [200,400,458,580,662,791,1000,
        1262,1650,2525,2758,3018,3322,3682,
        4061,4440,4853,5310,6520,
        6930,7349]

plt.plot(years,pops)
plt.show()


import matplotlib.pyplot as plt
import numpy as np
x1 = np.arange(0, 110.0, 20)  ###X
x2 = np.arange(0, 110.0, 20)  ###
y1 = np.sin(2*np.pi*x)
y2 = np.sin(2*np.pi*x2)
lines = plt.plot(x1, y1, x2, y2)
l1, l2 = lines
plt.setp(lines, linestyle='--')      
plt.show()


import sys
print(sys.path)


# simple inquiry example
import bluetooth

nearby_devices = bluetooth.discover_devices(lookup_names=True)
print("found %d devices" % len(nearby_devices))

for addr, name in nearby_devices:
    print("  %s - %s" % (addr, name))



