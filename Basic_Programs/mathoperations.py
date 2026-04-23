from MyPack.Basicshapes import areaofsquare, areaofrect, perimeterofsquare
from MyPack.circle import areaofcircle, perimeter



radius=int(input('enter a radius'))

print('area :',areaofcircle(rad=radius))
print('peri :',perimeter(rad=radius))

si=int(input('Enter side of sq'))
print('Area : ',areaofsquare(side=si))
print('peri :',perimeterofsquare(side=si))

l=int(input('Enter length'))
b=int(input('enter breadth'))
print('area : ',areaofrect(l,b))