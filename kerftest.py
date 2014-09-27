#!/usr/bin/python

#
#Juha Kivekas
#15th Sep 2014
#juha.kivekas@wippies.fi
#
#This is a simple python script that is used to make designfiles for mesuring 
#the kerf of a lasercutter. The experiment is described in detail in the 
#README.txt file that should have come with this file.
#

import sys
import math

#-------Make sure that the program is used right

if len(sys.argv) != 5 :
	print "Usage:"
	print "   python kerftest [material thickness] [min kerf] [max kerf] [number of pieces]"
	print "   For a more detailed description, take a look at README.txt\n"
	quit()

#-------read arguments
MATERIAL = float(sys.argv[1])
MIN_KERF = float(sys.argv[2])
MAX_KERF = float(sys.argv[3])
NSTEPS   = int(math.floor(float(sys.argv[4])))

KERF_STEP = (MAX_KERF - MIN_KERF) / NSTEPS
WIDTH = 11*MATERIAL
HEIGHT = (2*NSTEPS+2)*MATERIAL

print ""
print "Material thickness: ", MATERIAL
print "Minimum kerf:       ", MIN_KERF
print "Maximum kerf:       ", MAX_KERF
print "Number of steps:    ", NSTEPS
print ""

#------- check for wierd values

if MIN_KERF < 0 :
	print "ERROR: minimum kerf must be positive."
	quit()

if MAX_KERF < MIN_KERF :
	print "ERROR: max kerf is smaller than min kerf."
	quit()

if MAX_KERF > 1 or MIN_KERF > 1:
	print "WARNING: Kerf values are awfully large, is this right?"
	
if NSTEPS > 20 :
	print "WARNING: Number of steps is more than 20, is this right?"

if NSTEPS < 1 :
	print "ERROR: Number of steps has to be larger than 0."
	quit()

#------- inform the user
print "The output file should be scaled be printed correctly."
print "Width:               " + str(WIDTH) + " mm"
print "Height:              " + str(HEIGHT) + " mm"

#------- open file and write SVG header
svg = open("kerftest.svg", "w")

svg.write("<?xml version=\"1.0\" standalone=\"no\"?>\n")
svg.write("<!DOCTYPE svg PUBLIC \"-//W3C//DTD SVG 1.1//EN\"\n")
svg.write("\"http://www.w3.org/Grapihics/SVG/1.1/DTD/svg11.dtd\">\n")
svg.write("<svg xmlns=\"http://www.w3.org/2000/svg\" version=\"1.1\" ")
svg.write("width=\"%.2f\" height=\"%.2f\">\n" % (11*MATERIAL, (2*NSTEPS+2)*MATERIAL));

#======= draw the actual graphics ========

base = MATERIAL *1.5
kerf = MIN_KERF
outset = 0;
inset  = 0;
for i in range(0, NSTEPS) :
	outset = MATERIAL + kerf
	inset  = MATERIAL - kerf

	#text for the square hole
	svg.write("\t<text x=\"%.2f\" y=\"%.2f\" font-size=\"%.2f\"> %.3f </text>\n" % (MATERIAL/2, base + MATERIAL*0.8, MATERIAL*0.8, kerf))
	#drawing the square hole
	svg.write("\t<path style=\"fill:none; stroke:black; stroke-width:0.1;\" d=\"")
	svg.write("M %.2f %.2f " % (3*MATERIAL     , base   ))
	svg.write("l %f %f " % (outset , 0      ))
	svg.write("l %f %f " % (0      , outset ))
	svg.write("l %f %f " % (-outset, 0      ))
	svg.write("l %f %f " % (0      , -outset))
	svg.write("z \"/>\n")


	#make the key (facing right or left)
	svg.write("\t<path style=\"fill:none; stroke:black; stroke-width:0.1;\" d=\"")
	if i%2 == 0 :
		#shape
		svg.write("M %.2f %.2f" % (5*MATERIAL , base))
		svg.write("l %f %f " % (3*MATERIAL , 0             ))
		svg.write("l %f %f " % (0          , -MATERIAL/2   ))
		svg.write("l %f %f " % (2*MATERIAL , 0             ))
		svg.write("l %f %f " % (0          , MATERIAL+inset))
		svg.write("l %f %f " % (-2*MATERIAL, 0             ))
		svg.write("l %f %f " % (0          , -MATERIAL/2   ))
		svg.write("l %f %f " % (-3*MATERIAL, 0             ))
		svg.write("z \"/>\n")
		#text
		svg.write("\t<text x=\"%.2f\" y=\"%.2f\" font-size=\"%.2f\"> %.3f </text>\n" % (8*MATERIAL, base + MATERIAL*0.8, MATERIAL*0.8, kerf))
	else :
		svg.write("M %.2f %.2f" % (5*MATERIAL, base - MATERIAL/2))
		svg.write("l %f %f " % (2*MATERIAL , 0         ))
		svg.write("l %f %f " % (0          , MATERIAL/2))
		svg.write("l %f %f " % (3*MATERIAL , 0         ))
		svg.write("l %f %f " % (0          , inset     ))
		svg.write("l %f %f " % (-3*MATERIAL, 0         ))
		svg.write("l %f %f " % (0          , MATERIAL/2))
		svg.write("l %f %f " % (-2*MATERIAL, 0         ))
		svg.write("z \"/>\n")
		svg.write("\t<text x=\"%.2f\" y=\"%.2f\" font-size=\"%.2f\"> %.3f </text>\n" % (5*MATERIAL, base + MATERIAL*0.8, MATERIAL*0.8, kerf))
	
	kerf += KERF_STEP
	base += 2*MATERIAL

#-------- finish the SVG and close the file
svg.write("</svg>")
svg.close()
