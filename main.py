import autograd.numpy as np
import differint.differint as df
import matplotlib.colors as colors
import matplotlib.pyplot as plt
from math import *
from autograd import grad

a = 18 # font size
l = 5 # line width
plt.rc('font', size=a)
plt.rc('axes', labelsize=a)
plt.rc('xtick', labelsize=a)
plt.rc('ytick', labelsize=a)

def computeRL(a, b, n, m, viewBox, f, showLegend=True, translucent=False, is3d=False):
     if is3d: ax = plt.figure().add_subplot(projection='3d')
     else: ax = plt.figure().add_subplot()
     prime = grad(f)
     xVals = np.array([(i/(n-1))*(b-a)+a for i in range(n)]) # x vals
     DFs = [df.RL(i/(m-1),f,a,b,n) for i in range(0, m-1)] + [[float(prime(x)) for x in xVals]]
     for i, d in enumerate(DFs):
          if translucent: alpha = 0.25 if i not in [0, m-1] else 1
          else: alpha = 0.5 if is3d else 1
          if is3d:
               ax.plot(xVals, d, color=colors.hsv_to_rgb((1-i/(2.2*(m-1)), 1, 1)), zs=i/(m-1), linewidth=l,
          alpha=alpha)
          else:
               ax.plot(xVals, d, color=colors.hsv_to_rgb((1-i/(2.2*(m-1)), 1, 1)), linewidth=l, alpha=alpha)
     if showLegend: ax.legend([f'alpha={i}/{m-1}' for i in range(m)])
     ax.set_xlim(viewBox[0][0], viewBox[1][0])
     ax.set_ylim(viewBox[0][1], viewBox[1][1])
     if is3d:
          ax.set_zlim(0,1)
          ax.set_xlabel('t')
          ax.set_ylabel('y')
          ax.set_zlabel('alpha')
     ax.grid()
     plt.show()

def computeGL(a, b, n, m, viewBox, f, showLegend, translucent=False, is3d=False):
     if is3d: ax = plt.figure().add_subplot(projection='3d')
     else: ax = plt.figure().add_subplot()
     prime = grad(f)
     xVals = np.array([(i/(n-1))*(b-a)+a for i in range(n)]) # x vals
     DFs = [df.GL(i/(m-1),f,a,b,n) for i in range(0, m-1)] + [[float(prime(x)) for x in xVals]]
     for i, d in enumerate(DFs):
          if translucent: alpha = 0.25 if i not in [0, m-1] else 1
          else: alpha = 0.5 if is3d else 1
          if is3d:
               ax.plot(xVals, d, color=colors.hsv_to_rgb((1-i/(2.2*(m-1)), 1, 1)), zs=i/(m-1), linewidth=l,
          alpha=alpha)
          else:
               ax.plot(xVals, d, color=colors.hsv_to_rgb((1-i/(2.2*(m-1)), 1, 1)), linewidth=l, alpha=alpha)
     if showLegend: ax.legend([f'alpha={i}/{m-1}' for i in range(m)])
     ax.set_xlim(viewBox[0][0], viewBox[1][0])
     ax.set_ylim(viewBox[0][1], viewBox[1][1])
     if is3d:
          ax.set_zlim(0,1)
          ax.set_xlabel('t')
          ax.set_ylabel('y')
          ax.set_zlabel('alpha')
     ax.grid()
     plt.show()

def computeC(a, b, n, m, viewBox, f, showLegend, translucent=False, is3d=False):
     if is3d: ax = plt.figure().add_subplot(projection='3d')
     else: ax = plt.figure().add_subplot()
     prime = grad(f)
     xVals = np.array([(i/(n-1))*(b-a)+a for i in range(n)]) # x vals
     DFs = [[f(x)-f(a) for x in xVals]] + [[df.CaputoL1point(i/(m-1),f,a,x,n) for x in xVals] for i in
     range(1, m-1)] + [[float(prime(x)) for x in xVals]]
     for i, d in enumerate(DFs):
          if translucent: alpha = 0.25 if i not in [0, m-1] else 1
          else: alpha = 0.5 if is3d else 1
          if is3d:
               ax.plot(xVals, d, color=colors.hsv_to_rgb((1-i/(2.2*(m-1)), 1, 1)), zs=i/(m-1), linewidth=l,
               alpha=alpha)
          else:
               ax.plot(xVals, d, color=colors.hsv_to_rgb((1-i/(2.2*(m-1)), 1, 1)), linewidth=l, alpha=alpha)
     if showLegend: ax.legend([f'alpha={i}/{m-1}' for i in range(m)])
     ax.set_xlim(viewBox[0][0], viewBox[1][0])
     ax.set_ylim(viewBox[0][1], viewBox[1][1])
     if is3d:
          ax.set_zlim(0,1)
          ax.set_xlabel('t')
          ax.set_ylabel('y')
          ax.set_zlabel('alpha')
     ax.grid()
     plt.show()

####### PARAMETERS OF COMPUTATION #######
# [a,b] : domain of computation
# n : no. of computed points in the domain
# m : no. of curves (including orders of 0 and 1)
# viewBox : viewing frame [[xMin, yMin], [xMax, yMax]]
# f : function to be differintegrated
# legend : shows legend if True
# translucent : fractional derivatives will be partially transparent
# is3d : makes a 3D visualization instead of 2D if True
# method : 0 for RL, 1 for GL and 2 for C.

a, b = [0,1]
n = 1000
m = 7
viewBox = [[0,-1], [1,4]]
showLegend = False
translucent = True
is3d = True
method = 2
def f(x):
     # Replace with function of choice
     return np.sin(x) + np.cos(x) + np.exp(x)

if method == 0 : computeRL(a, b, n, m, viewBox, f,
showLegend, translucent=translucent, is3d=is3d)
elif method == 1: computeGL(a, b, n, m, viewBox, f,
showLegend, translucent=translucent, is3d=is3d)
elif method == 2: computeC(a, b, n, m, viewBox, f,
showLegend, translucent=translucent, is3d=is3d)
