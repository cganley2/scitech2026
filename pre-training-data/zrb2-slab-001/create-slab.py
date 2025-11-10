from ase import io
from ase.build import surface, bulk, make_supercell, add_adsorbate
from ase.visualize import view

zrb2 = io.read('/home/cganley2/qe-data/zrb2/structures/ZrB2_conventional_standard_mp-1472.cif')

# Create (001) surface
surface_from_cif = surface(zrb2, (0, 0, 1), layers=3, vacuum=10.0, periodic=True)

# Create supercell
n = 4
slab = make_supercell(surface_from_cif, [[n, 0, 0], [0, n, 0], [0, 0, 1]])

# add_adsorbate(slab, 'O', height=-10, position=(4.0, 3.0))
# slab.center()

# Save as CIF
# io.write('zrb2-slab-001-before-relax.cif', slab, format='cif')
# io.write('zrb2-slab-001-before-relax.extxyz', slab, format='extxyz')

view(slab)