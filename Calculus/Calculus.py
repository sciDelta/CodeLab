""" Calculus in SymPy """
import numpy as np, sympy 
from sympy import *
x = Symbol('x')
v = Symbol('v')

""" Define equations """
y = x**2
z = x**3 + v 

""" Differntiation """
dydx = y.diff(x)
d2ydx = dydx.diff(x)
partialDiff_zdx = diff(z, x)
partialDiff_zdv = diff(z, v)
product_zy = diff(z*y, x)

""" Intergration """
integral_y = integrate(y, x)
double_integral = integrate(integrate(z, x), v)

""" Display output """
print('Input Equations: \ny = ', y, '\nz = ', z,'\n')
print('Differentiation:\ndy/dx = ', dydx, '\nd2y/dx = ', d2ydx,'\n')
print('Partial Differentiation: \nz d/dx = ', partialDiff_zdx, '\nz d/dv = ', partialDiff_zdv,'\n')
print('Product rule: \ndzy/dx = ', product_zy,'\n')
print('Integration: \nintegral y dx = ', integral_y,'\ndouble integral z dxdv = ', double_integral)

"""Output
Input Equations: 
y =  x**2 
z =  v + x**3 

Differentiation:
dy/dx =  2*x 
d2y/dx =  2 

Partial Differentiation: 
z d/dx =  3*x**2 
z d/dv =  1 

Product rule: 
dzy/dx =  3*x**4 + 2*x*(v + x**3) 

Integration: 
integral y dx =  x**3/3 
double integral z dxdv =  v**2*x/2 + v*x**4/4
"""
