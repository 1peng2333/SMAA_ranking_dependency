import os
from chimerax.core.commands import run
import numpy as np

Dir_name = open(f"/content/Dirname.txt").read()
Dir_name = Dir_name.replace("\n", "")
Dir_name_s = Dir_name.split("/")[0]

radius = open(f"/content/radius.txt").read()
anglex = open(f"/content/anglex.txt").read()
angley = open(f"/content/angley.txt").read()
anglez = open(f"/content/anglez.txt").read()
scalev = open(f"/content/scalev.txt").read()
shifty = open(f"/content/shifty.txt").read()
Centerx = open(f"/content/Centerx.txt").read()
Centery = open(f"/content/Centery.txt").read()
Centerz = open(f"/content/Centerz.txt").read()

command0 = f"windowsize 1200 1200"
run(session, command0)

command1 = f"set bg white"
run(session, command1)

command2 = f"open /content/{Dir_name}/top10_ab_test_MDS.pdb; open /content/{Dir_name}/IWS_ab_test_MDS.pdb; open /content/{Dir_name}/IBS_ab_test_MDS.pdb; open /content/{Dir_name}/all_ab_test_MDS.pdb; open /content/{Dir_name}/box6nn_MDS.bild;"
run(session, command2)

command3 = f"show atoms; ~ribbon; ~bond; setattr g display false"
run(session, command3)

command4 = f"sel #4; color sel blue"
run(session, command4)

command5 = f"sel #1; color sel red; sel #2; color sel green; sel #3; color sel cyan"
run(session, command5)

command10= f"shape sphere center {Centerx},{Centery},{Centerz} radius {radius} color 1,1,1,0.5 mesh true;"
run(session, command10)

command11= f"~sel;view; turn x {anglex}; turn y {angley}; turn z {anglez}; view; move y {shifty};~sel; clip off;"
run(session, command11)

#command14 = f"save /content/{Dir_name_s}/result/07_visualize_MDS.png;"
#run(session, command14)

command15 = f"save /content/{Dir_name_s}/result/07_visualize_MDS.cxs;"
run(session, command15)