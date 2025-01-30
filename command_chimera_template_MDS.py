from chimera import runCommand
runCommand("windowsize 1200 1200;background solid white;open all_ab_test_MDS.pdb;open top10_ab_test_MDS.pdb;open IWS_ab_test_MDS.pdb;open IBS_ab_test_MDS.pdb; show @;open box6nn.bild;~ribbon;~bond;sel #0; color blue sel; sel #1; color red sel;  sel #0; setattr atom drawMode 1 sel;setattr atom radius 1.4 sel; sel #1; setattr atom drawMode 1 sel;  setattr atom radius 1.5 sel; sel #2; color green sel; setattr atom drawMode 1 sel; setattr atom radius 1.6 sel; sel #3; color cyan sel; setattr atom drawMode 1 sel; setattr atom radius 1.6 sel;shape sphere center Centerx,Centery,Centerz radius RadiiX color 1,1,1,1 mesh true;~sel;center;turn x anglex; turn y angley; turn z anglez;scale scalev;center;move y shifty;~sel;~focus;clip off;export format WebGL ../result/08_visualize_MDS.html5;shape sphere center Centerx,Centery,Centerz radius RadiiX color 1,1,0,0.5 mesh false; copy file ../result/07_visualize_MDS.png;save ../result/09_visualize_MDS.py;stop;")

