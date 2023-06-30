import numpy as np
import scipy as sp
import math as math

class QHO_state:

    def __init__(self):
        pass

    def spatial_wf(self,x,n):
        n = int(n)
        hermite_poly = sp.special.hermite(n)
        return (1 / np.sqrt(math.factorial(n) * 2**n)) * (np.pi**-0.25) * np.e**(-(x**2) / 2) * hermite_poly(x)

    def time_evolution(self,t,n):
        return np.e**(-1j*(n + 0.5)*t)

    def total_wavefunction(self,x,t,n):
        return self.spatial_wf(x,n) * self.time_evolution(t,n)

    def superposition(self,x,t,n1,n2,c1):
        return np.sqrt(c1)*self.total_wavefunction(x,t,n1) + np.sqrt(1-c1)*self.total_wavefunction(x,t,n2)


    def prob_dens(self,x,t,n1,n2,c1):
        psi = self.superposition(x,t,n1,n2,c1)
        prob = np.conj(psi)*psi
        return prob
