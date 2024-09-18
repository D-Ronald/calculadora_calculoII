import sympy as sp
import src.derivada as derivada
import src.grafico as grafico

# Função para validar o input numérico
def get_input(prompt, input_type=int):
    while True:
        try:
            return input_type(input(prompt))
        except ValueError:
            print(f"Por favor, insira um valor válido para {prompt.lower()}.")

# Validar função simbólica
while True:
    try:
        função = str(input('Digite aqui sua função: '))
        # Tentar "sympificar" a função para verificar se é válida
        função_simp = sp.sympify(função)
        break
    except sp.SympifyError:
        print("Por favor, insira uma função válida.")

# Validar input do ponto (x, y)
while True:
    try:
        x = get_input('Digite o valor do ponto em x: ', float)
        y = get_input('Digite o valor do ponto em y: ', float)
        ponto = (x, y)
        break
    except ValueError:
        print("Os valores de x e y devem ser números.")

# Função para input de derivada implícita
def input_implicita():
    while True:
        try:
            dependente = input('Derivada de: ').strip()
            independente = input('Em relação a: ').strip()
            # Tentar validar as variáveis
            sp.Symbol(dependente)
            sp.Symbol(independente)
            return dependente, independente
        except (ValueError, sp.SympifyError):
            print("Insira variáveis válidas para derivadas implícitas.")

# Chamadas de funções com tratamento de erros
try:
    derivada.exibe_derivada_em_x(função_simp)
except ValueError as ve:
    print(f"Erro de valor ao calcular derivada em x: {ve}")
except Exception as e:
    print(f"Erro inesperado ao calcular derivada em x: {e}")

try:
    derivada.exibe_derivada_em_y(função_simp)
except ValueError as ve:
    print(f"Erro de valor ao calcular derivada em y: {ve}")
except Exception as e:
    print(f"Erro inesperado ao calcular derivada em y: {e}")

try:
    derivada.exibe_plano_tangente(ponto, função_simp)
except ValueError as ve:
    print(f"Erro de valor ao calcular o plano tangente: {ve}")
except Exception as e:
    print(f"Erro inesperado ao calcular o plano tangente: {e}")

try:
    derivada.exibe_reta_normal(ponto[0], ponto[1], função_simp)
except ValueError as ve:
    print(f"Erro de valor ao calcular a reta normal: {ve}")
except Exception as e:
    print(f"Erro inesperado ao calcular a reta normal: {e}")

# Entrada e exibição da derivada implícita
input_implicita = input_implicita()
try:
    derivada.exibe_derivada_implicita(função_simp, dependente=input_implicita[0], independente=input_implicita[1])
except ValueError as ve:
    print(f"Erro de valor ao calcular a derivada implícita: {ve}")
except Exception as e:
    print(f"Erro inesperado ao calcular a derivada implícita: {e}")

# Exibir máximos e mínimos
try:
    derivada.exibe_maximos_minimos(função_simp)
except ValueError as ve:
    print(f"Erro de valor ao calcular máximos e mínimos: {ve}")
except Exception as e:
    print(f"Erro inesperado ao calcular máximos e mínimos: {e}")

# Exibir gráfico
try:
    grafico.grafico_funcao(função_simp)
except ValueError as ve:
    print(f"Erro ao exibir gráfico da função, verifique os pontos e a função fornecida: {ve}")
except Exception as e:
    print(f"Erro inesperado ao exibir gráfico da função, verifique os pontos e a função fornecida: {e}")