import argparse
import numpy as np
import scipy as sp
from scipy import integrate
import math as math
import matplotlib.pyplot as plt

from Trapezoid_Int import trap_int
from QHO_wavefunction import QHO_state


def main(a,b,n1,n2,c1, tmax, Nt):
    n1, n2= int(n1), int(n2)
    if n1 < 0 or n2 < 0:
        print("Please choose positive n1, n2")
        return

    if c1 < 0 or c1 > 1:
        print("Please choose c1 less than 1 and greater than 0")
        return

    t = np.linspace(0,tmax,Nt)
    P = []
    P_real = []

    plt.figure()
    x_plot = np.linspace(-10,10,100)
    QHO_plot = QHO_state()
    plt.title(f"Prob. Density for the State {np.round(np.sqrt(c1), 2)}|{n1}> + {np.round(np.sqrt(1-c1),2)}|{n2}> at different times")

    for t_ in [tmax//4 * i for i in range(5)]:
        plt.plot(x_plot, QHO_state().prob_dens(x_plot,t_,n1,n2,c1), label = f't = {t_}')

    plt.legend()
    plt.xlabel('x')
    plt.ylabel(r"$|\psi(x)|^2$")
    plt.grid()


    for time in t:
        QHO = QHO_state()
        P.append(np.real(trap_int(lambda x: QHO.prob_dens(x,time,n1,n2,c1), a, b, 2)))
        P_real.append(np.real(sp.integrate.quad(QHO.prob_dens, a, b, args=(time,n1,n2,c1)))[0])


    plt.figure()
    plt.plot(t, np.real(P_real),'ro')
    plt.plot(t, np.real(P),'b.')
    plt.legend(['Scipy Integral', "Trapezoid Integral"])
    plt.title(f'Probability of Finding the Particle between x = {np.round(a,2)} and x = {np.round(b,2)} for the state: {np.round(np.sqrt(c1), 2)}|{n1}> + {np.round(np.sqrt(1-c1),2)}|{n2}> ')
    plt.ylabel("P(t)")
    plt.xlabel("Time")
    plt.grid()


    plt.show()


if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    print("set the integral bounds (x_min, x_max) the energy level of the two states in the superposition (n1, n2) and the probability of measuring the superposition in the n1 state (c1)")
    parser.add_argument('-xmin', help='x min', type=float, default = 0.0)
    parser.add_argument('-xmax', help='x max', type=float, default = 1.0)
    parser.add_argument('-n1', help='n1, energy level of first eigenstate in the superposition', type=int, default = 0)
    parser.add_argument('-n2', help='n2, energy level of second eigenstate in the superposition', type=int, default = 1)
    parser.add_argument('-c1', help='c1, probability of measuring the superposition state in n1 eigenstate', type=float, default = 0.5)
    parser.add_argument('-tmax', help='max time', type=float, default = 10)
    parser.add_argument('-Nt', help='number of time points', type=int, default = 100)





    args = parser.parse_args()._get_kwargs()
    a = [arg[1] for arg in args if arg[0] == 'xmin'][0]
    b = [arg[1] for arg in args if arg[0] == 'xmax'][0]
    n1 = [arg[1] for arg in args if arg[0] == 'n1'][0]
    n2 = [arg[1] for arg in args if arg[0] == 'n2'][0]
    c1 = [arg[1] for arg in args if arg[0] == 'c1'][0]
    tmax = [arg[1] for arg in args if arg[0] == 'tmax'][0]
    Nt = [arg[1] for arg in args if arg[0] == 'Nt'][0]

    main(a,b,n1,n2,c1, tmax,Nt)
