# part 1
import pandas
from math import pow, pi

raw_height = [8,4,6,3,5]
raw_radius = [5,9,12,7,9]
raw_surface = []

heights = pandas.Series(raw_height,index=['cyl1','cyl2','cyl3','cyl4','cyl5'],  name='Heights')
radius = pandas.Series(raw_radius, index=['cyl1','cyl2','cyl3','cyl4','cyl5'], name='Radius')
# surface = pandas.Series(raw_surface, index=['cyl1','cyl2','cyl3','cyl4','cyl5'], name='Surface Area')

df = pandas.concat([heights, radius], axis=1)
dfCylinder = pandas.DataFrame(df)
dfCylinder = dfCylinder.sort_values(by='Radius')
print("DataFram:")
print(dfCylinder)
dfCylinder.plot()


# Part 2


for i in range(len(raw_height)):
    raw_surface.append((2*pi*pow(raw_radius[i],2) )+ (2*pi*raw_radius[i]*raw_height[i]))
surface = pandas.Series(raw_surface, index=['cyl1','cyl2','cyl3','cyl4','cyl5'], name='Surface Area')



df = pandas.concat([heights, radius, surface], axis=1)
dfCylinder = pandas.DataFrame(df)
dfCylinder = dfCylinder.sort_values(by='Surface Area')
print("\nUpdated DataFrame:")
print(dfCylinder)
print("\nMean:")
print(dfCylinder.mean())
print("\nMax:")
print(dfCylinder.max())
print("\nMin:")
print(dfCylinder.min())

dfCylinder.plot.bar()
