#DONT USE THIS YET, THIS IS HIGHLY SPECIFIC

from read import openStruct
coordinates = openStruct("0ps_SGP.xyz")
from multiCell import increaseCell
increaseCell(coordinates,[1.7702580000000001E+01 ,0,0],[0,1.7702580000000001E+01,0],[0,0,1.7867090000000008E+01],3,3,1,range(152),"0ps_SGP_3x3x1.xyz")
coordinates = openStruct("0ps_SGP_3x3x1.xyz")

from distanceanalysis import minDist
selection = []
for i in range(152*4+144,152*5):
    selection.append(i)        

Au_selections = []
for i in range(9):
    for j in range(152*i,152*i+144):
        Au_selections.append(j)

O_selections = []
for i in range(9):
    for j in range(152*i+144,152*i+152):
        O_selections.append(j)

minVals_AuO = []
for i in range(8):
    X = minDist(coordinates,[selection[i]],Au_selections)
    minVals_AuO.append(X.distance[0])

minVals_OO = []
for i in range(8):
    X = minDist(coordinates,[selection[i]],O_selections)
    minVals_OO.append(X.distance[0])

print(np.mean(minVals_AuO))
print(np.mean(minVals_OO))
