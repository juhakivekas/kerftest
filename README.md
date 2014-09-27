Measuring the kerf for lasercutting projects
--------------------------------------------
####Juha kivekäs
While using a lasercutter one often needs to account for the kerf, that is 
the width of the cut made by the laser. This kerf is usually between 0.1 and 
0.2 millimeters, but in the case making well-fitting boxes and connectors more 
exact values should be used. The kerf depends on several factors: cutting 
power and speed, material type and thickness, and the model of the printer. 
Guessing your way to an approximate value is tedious and doesen't necessarily 
give the best results. In order to measure the kerf i propose an experiment 
simple enough to be conducted by anyone with earlier experience with 
lasercutting. The general idea of the experiment is to try several values for the kerf 
and select the one that best suits the needs of the user.

1. Start by measuring the exact thickness of your material with a caliper. All measurements used by the software are expected to be in millimeters.

2. Choose a minimum and maximum limit for the kerf. If you don't have an earlier estimate pick 0.10 and 0.20mm.

3. Choose an appropriate amount of test pieces, around 10 to 20.

4. Run the kerftest script to get your vector file.

		python kerftest [material thickness] [min kerf] [max kerf] [number of pieces]
   
   For example like this:

		python kerftest 4.0 0.1 0.2 5

   If you are unfamiliar with the UNIX commandline, don't worry, we'll only be doing very basic stuff. Just follow the steps described in the bottom of the readme.

5. Open the file in a vector graphics editor and make adjustments if needed (scaling, simplifying, saving in a different format, etc.). The script will tell you what the final size should be.

6. Print the file on your lasercutter. The shapes should be cut and the text rasterized.

7. Try pushing corresponding pins into holes and choose the best fit for your project.

8. Read the value of the kerf on the best fit and use this in your next project. Make sure that the value marked on the pin and hole are the same.   

For those who are unfamiliar with the command line, here's how to run the script.


1. Search for an application called Treminal or Commandline and open a Terminal window.

2. Learn the basics of navigation between directories: http://www.ee.surrey.ac.uk/Teaching/Unix/unix1.html

3. Navigate to the directory that this file is contained in, probably "~/Downloads/kerftest".

4. Execute the kerftest script by running this command:

		python kerftest 4.0 0.1 0.2 10

   If an SVG file appeared in your working directory, then everything went as it should. If something wierd (or nothing) happens, ask your nerd friend for help.

5. Now just substitute the values for your own measurements and you've got the desing file.
