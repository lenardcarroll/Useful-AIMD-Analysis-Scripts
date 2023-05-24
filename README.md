To increase the unit cell from 1x1x1 to (e.g.) 3x3x1 of a simulation box with dimensions [10,0,0],[0,10,0],[0,0,10] for atoms 1-120, we use:
```
from read import openStruct

coords = openStruct("filename")

from multiCell import increaseCell

increaseCell(coords,[10,0,0],[0,10,0],[0,0,10],3,3,1,range(120),"outputfilename")
```

To calculate the RMSD for atoms 1, 2 and 3 respectively use:

```
from read import openStruct

coords = openStruct("filename")

from rmsd import rmsd, plotRMSD

X = rmsd(coords,[0])
Y = rmsd(coords,[1])
Z = rmsd(coords,[2])

plotRMSD([X,Y,Z])
```

If you want to calculate the RMSD for atoms 1-3, then:

```
from read import openStruct

coords = openStruct("filename")

from rmsd import rmsd, plotRMSD

X = rmsd(coords,[0,1,2])

plotRMSD([X])
```

If you want to make a charge plot for atoms 1-56, using a minimum charge of -0.54, maximum charge of 0.12, radius of 20,000 for atoms 1-48 and 10,000 for atoms 49-56, while using plot dimensions of [-2,19], use:

```
from plotCharge import chargePlot

chargePlot("specialfilewithcharges",-0.54,0.12,[range(48),range(48,56)],[20000,10000],-2,-2,19,19)
```

If you want to plot the special RDF between atoms 1-48 and 49-56 over the distance [0,26] in increments of 0.1, use:

```
from rdf import intRDF, plotInt

X = rdf(coords,range(48),range(48,56), 0, 26, 0.1)

plotInt(X)
```
