import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
import sympy as sp

def grafico_funcao(function):
    # Definir os símbolos para x e y
    x, y = sp.symbols('x y')
    
    # Converter a função passada para uma expressão SymPy
    function_sympy = sp.sympify(function)

    # Converter a expressão SymPy para uma função que aceita valores NumPy
    func_np = sp.lambdify((x, y), function_sympy, 'numpy')

    # Definir os limites e os pontos da malha
    a, b = 4, -4
    points = 1000
    matriz = np.linspace(a, b, points)
    x_vals, y_vals = np.meshgrid(matriz, matriz)

    # Calcular os valores da função para a malha gerada
    z_vals = func_np(x_vals, y_vals)

    # Gerar o gráfico
    grafico = plt.figure()
    eixo = grafico.add_subplot(111, projection='3d')
    superficie = eixo.plot_surface(x_vals, y_vals, z_vals, cmap=cm.coolwarm)
    grafico.colorbar(superficie, shrink=1, aspect=1)
    plt.show()