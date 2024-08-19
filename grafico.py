import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
import numexpr as ne

def grafico_funcao(function):
    function = str(function)
    a, b =  4,-4
    points = 1000
    matriz = np.linspace(a,b,points)
    x,y = np.meshgrid(matriz, matriz)
    z = ne.evaluate(function)
    grafico = plt.figure()
    eixo = grafico.add_subplot(111,projection ='3d')
    superficie = eixo.plot_surface(x,y,z, cmap=cm.coolwarm)
    grafico.colorbar(superficie,shrink = 1, aspect = 1)
    plt.show()
    