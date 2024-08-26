import sympy as smp
from sympy import *
import numpy as np
import grafico
import sympy as sp
x,y,z,t = smp.symbols("x y z t", real = True)
e = smp.E
#function = input("Digite aqui sua z=f(x,y): ")
f = -4* (16-(x**2)-(y**2))**(1/2)
x0, y0, z = (2,0,1)
v = (1,1)
df_dx = smp.diff(f, x)
df_dy = smp.diff(f, y)
df_dx_x0y0 = df_dx.subs({x:x0, y:y0})
df_dy_x0y0 = df_dy.subs({x:x0, y:y0})
f_x0y0 = f.subs({x:x0, y:y0})


def calcula_plano_tangente(x0, y0 , f_x0y0):
    return df_dx_x0y0*(x-x0) + df_dy_x0y0*(y-y0) + f_x0y0
    
def exibe_plano_tangente(point):
    return f"z = {calcula_plano_tangente(point[0], point[1], point[2]):.2f}"

def reta_normal(x0, y0, f_x0y0):
    vetor_1 = [x0, y0, f_x0y0]
    vetor_2 = [-df_dx_x0y0*t, -df_dy_x0y0*t, 1*t]
    soma  = [0 ,0 ,0 ]
    for i in range(len(vetor_1)):
       soma[i]= vetor_1[i]+vetor_2[i]
    return f"(x, y, z) = ({vetor_1[0]+vetor_2[0]}, {vetor_1[1]+vetor_2[1]}, {vetor_1[2]+vetor_2[2]})"

def vetor_unitario(i,j):
    if i == 1 and j == 1:
        return [i,j]
    else:
        return [i/(i**2+j**2)**(1/2), j/(i**2+j**2)**(1/2)]
def derivada_direcional():
    return (df_dx_x0y0*v[0]) + (df_dy_x0y0*v[1])
#derivada implicita
def derivada_implicita(equacao, var_dependente, var_independente):
    # derivada parcial relação a V independente
    independente = sp.diff(equacao, var_independente)

    # derivada parcial relação a V dependente
    dependente = sp.diff(equacao, var_dependente)

    # derivada implícita de c2
    dImplicita = -independente / dependente

    return dImplicita
#para mudar parametros da função derivada implicita, utilize a logica:
#derivada_implicita(NomeFuncao, x, y)    'parametros: implícita de x em relaçap a y'


print(f"P({x0}, {y0}, {f_x0y0})")
print(df_dx)
print(df_dy)
print(plano_tangente(x0, y0, z))
print(reta_normal(x0,y0,z))
print(vetor_unitario(v[0],v[1]))
print(derivada_direcional())
print("Derivada implícita dz/dx:", derivada_implicita(f,y,x))
grafico.grafico_funcao(f)