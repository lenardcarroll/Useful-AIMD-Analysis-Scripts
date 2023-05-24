import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import Normalize

#This class plots the atoms based on the charge, colouring the charge according to a colour wheel. Make sure to select the minimum and maximum charge for the colour wheel, where to read the data from, the radii values, the minimum and maximum x & y values
class chargePlot:
    def __init__(self,file,min_charge,max_charge,selections,radius,min_x,min_y,max_x,max_y):
        # Read in the file containing the atom coordinates and charges. The first three columns are the x,y,z coordinates, the fourth column belongs to the charges.
        coords_and_charges = np.loadtxt(file)

        # Extract the x and y coordinates from the file
        x = coords_and_charges[:,0]
        y = coords_and_charges[:,1]

        # Extract the charges from the file
        charges = coords_and_charges[:,3]

        # Define the color map based on your charge range
        cmap = plt.cm.get_cmap('coolwarm') # Replace 'coolwarm' with any other colormap that you prefer
        norm = plt.Normalize(min_charge, max_charge) # This sets the color range based on the min and max charges in your data.

        # Create the plot
        width=1920
        height=1440
        thickness = 6
        fontsize=58
        padding=28

        width = int(width/80)
        height = int(height/80)
        fig = plt.figure()
        fig.set_size_inches(width,height)
        ax1 = fig.add_subplot(111)
        plt.xlabel("X (Å)",fontsize=fontsize,labelpad=padding)
        plt.ylabel("Y (Å)",fontsize=fontsize,labelpad=padding)
        plt.xticks(fontsize=50)
        plt.yticks(fontsize=50)
        ax1.tick_params(width=3*thickness,length=10)
        for axis in ['top','bottom','left','right']:
            ax1.spines[axis].set_linewidth(int(1.7*thickness))
        ax1.tick_params(axis='both', which='major', pad=int(padding/1.33))

        
        for i in range(len(selections)):
            x_s = []
            y_s = []
            c_s = []
            for j in selections[i]:
                x_s.append(x[j])
                y_s.append(y[j])
                c_s.append(charges[j])
            #Insert radius. For Au I used 20,000 and for O I used 10,000
            scatter = ax1.scatter(x_s, y_s, c=c_s, cmap=cmap, norm=norm, edgecolor='black', linewidth=thickness, s=radius[i])
            if i == 0:
                # Add a color bar to the plot
                cbar = plt.colorbar(scatter, ax=ax1)
                cbar.set_label('Charges',fontsize=fontsize*5/8)

                cbar.ax.tick_params(labelsize=fontsize/2, size=20, width=thickness/2)
                
        ax1.set_xlim([min_x, max_x])
        ax1.set_ylim([min_y, max_y])

        # Show the plot
        fig.savefig('ChargePlot.png', dpi=100, bbox_inches='tight')
        plt.show()
