# Project_FSSH-3

The content of the included folders:

Exact - exact calculations for reference, do them first;
   the results are used together with the TSH data, when plotting the results


Res1 - the "normal" calculations for all methods, using local diabatization approach

  This makes Figure 1 and Figures 2-4 of the manuscript


Res2 - the "normal" calculations for all methods, but now using NAC-based integrator

  This makes Figures 5-7 of the manuscript

Res3 - starting with a less fortunate initial guess of the J matrix J_{i,i+1} = 1, and J_{i-1,i}=-1

  This makes Figures 8-10 of the manuscript

Res4 - same as 1, but using J that connects old and new populations

  This makes Figures 11-13 of the manuscript
