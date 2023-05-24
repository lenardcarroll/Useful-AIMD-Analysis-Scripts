To increase the unit cell from ```1$\times$1$\times$1``` to (e.g.) 3$\times$3$\times$1 of a simulation box with dimensions [10,0,0],[0,10,0],[0,0,10] for atoms 1-120, we use:
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

If you want to make a charge plot, use:

```

```
