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

Res5 - same as 1, but with different ways of rescaling velocities upon the frustrated hops
  This is to address Reviewer's 1 concern


Res6 - the Hamiltonian with two pair-crossinngs, initialization on the top state, Figure 14

Res7 - same as Res6, but the initialization is on states 3 and 1 as a superposition, Figure 15
