#this python script:translate molecule at center of (15.3406, 15.3406, 60.0) unit cell
from ase.io import read,write
import sys 
from sys import argv
atoms = read(sys.argv[1])
atoms.center(vacuum=0.0)
a=atoms.get_cell()
# Want to put molecule in center of unit cell
x=y=15.3406
z=60.0
ax=(x-a[0,0])/2.0
ay=(y-a[1,1])/2.0:
az=(z-a[2,2])/2.0
atoms.center(vacuum=ax,axis=0)
atoms.center(vacuum=ay,axis=1)
atoms.center(vacuum=az,axis=2)
#atoms.center(vacuum=None)
print atoms.get_cell()
#split string
s1,s2=sys.argv[1].split(".")
write(s1+'-POSCAR.vasp', atoms, vasp5=True)
#write('comeophe2_1-xyz.png', atoms, show_unit_cell=2)
