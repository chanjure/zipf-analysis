zipf analysis
=============

This repository contains code to observe whether books adhere to Zipf's law, as
done in support of the paper "Zipf analysis of 19th-century English-language books",
V. Dracula, to appear in Annals of Computational Linguistics, 2022.

To run the code, you will need the Pandas package installed.

To reproduce the figures in the publication, follow these steps:

  bash bin/run_analysis.sh

Results will be placed in a `results/` directory.

This script will automatically pull the frankenstein.txt from https://gutenberg.org/84/84-0.txt
You need a internet connection
