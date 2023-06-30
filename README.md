# QHO-Prob
Calculates probability as a function of time for measuring a particle in a given region of space in a 1D QHO potential using trapezoidal integration and SciPy. This program computes the probability function for an arbitrary two state superposition of the QHO. Parameters such as the two eigenstates comprising the superposition, and their coefficients can all be specified 

Run main.py from the command line with the optional parameters:

	-h, --help  show this help message and exit
	-xmin XMIN  x min, default = 0
	-xmax XMAX  x max, default = 10 
	-n1 N1      n1, energy level of first eigenstate in the superposition, default = 0 
	-n2 N2      n2, energy level of second eigenstate in the superposition, default = 1  
	-c1 C1      c1, probability of measuring the superposition state in n1 eigenstate, default = 0.5  
	-tmax TMAX  max time, default = 10 
	-Nt NT      number of time points, default = 100
 
Final plots will show the probability as a function of time for the two integration methods, and some snapshots of how the probability density of the state evolves in time. 
