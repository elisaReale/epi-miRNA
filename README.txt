This folder contains the script for the intersections (intersections_hypergeometric.py) and for the BH pvalue adjustment (benjamini.R).

Software requirements:
-Python 3 and the following packages:
	- sys
	- argparse
	- re
	- scipy
	- tabulate

- R

Data are retrieved as described in main and in supplementary files.

Epigenetic gene sets are all concatenated in a single column file, each gene set preceded by the line >NAME_OF_SET.

miRNA gene sets underwent probe cleaning, LINC and other non-gene probes have been removed and the one with the higher fold-change have been chosen when two copies were present. For each experiment, differentially expressed genes have been chosen according to a +-0.5 threshold. Then, the probes have been translated to gene names and two files have been created, one with the up-regulated genes and one with the down. The two files are both in a single column format, each gene set being preceded by the name of the set (in the format >NAME_OF_SET).

The universe has been created merging together all the clean gene names, removing redundancies. The file is in single column format with no header.


