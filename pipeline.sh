#!/bin/bash

#$1 = First argument of the command. Gene sets of epigenetic signature downloaded for MSigDB. Complete list in supplementary files.
#$2 = Second argument of the command. Gene sets or genes up or down regulated after mirna transfection. Complete list in supplementary files.
#$3 = Third argument of the command. Universe set, obtained merging all the genes in the gene sets.
#$4 = Fourth argument of the command. Desired filename for the final output.

#file format specifications in README file.
#comment out the bottom line if you want to keep the mid-file. In this case, remember to change the output filename every time you run, in order to avoid overwritings.

python intersections_hypergeometric.py $1 $2 $3 | sed 's/set//g;s/ \+ /\t/g' | tr -d "'[]()" > intersections_output

Rscript benjamini.R intersections_output $4

rm intersections_output
