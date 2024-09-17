import sympy as sp
import src.derivada as derivada, src.grafico as grafico

função = str(input('Digite aqui sua função: '))
função = sp.sympify(função)
x = int(input('Digite o valor do ponto em x: '))
y = int(input('Digite o valor do ponto em y: '))
ponto = (x,y)

def input_inplicita():
  dependente = input('Derivada de: ')
  independente = input('Em relação a: ')   
  return dependente, independente


derivada.exibe_derivada_em_x(função)
derivada.exibe_derivada_em_y(função)
derivada.exibe_plano_tangente(ponto, função)
derivada.exibe_reta_normal(ponto[0],ponto[1], função)
input_inplicita = input_inplicita()
derivada.exibe_derivada_implicita(função, dependente = input_inplicita[0], independente= input_inplicita[1])
derivada.exibe_maximos_minimos(função)
grafico.grafico_funcao(função)