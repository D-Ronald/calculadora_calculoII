import sympy as sp
from sympy import *
import itertools
x, y, z, t = sp.symbols("x y z t")
e = sp.E
def calcula_derivada_em_x(function):
    try:
        return sp.diff(function, x)
    except ValueError as ve:
        print(f"ValueError ao calcular a derivada em x, tente verificar a entrada de dados: {ve}")
        return None
    except Exception as e:
        print(f"Erro ao calcular a derivada em x: {e}")
        return None

def exibe_derivada_em_x(function):
    try:
        derivada = calcula_derivada_em_x(function)
        if derivada is not None:
            print(f"Derivada parcial em x: {derivada}")
    except ValueError as ve:
        print(f"ValueError ao exibir a derivada em x, tente verificar a entrada de dados: {ve}")
        return None
    except Exception as e:
        print(f"Erro ao exibir a derivada em x: {e}")

def calcula_derivada_em_y(function):
    try:
        return sp.diff(function, y)
    except ValueError as ve:
        print(f"ValueError ao calcular a derivada em y tente verificar a entrada de dados: {ve}")
        return None
    except Exception as e:
        print(f"Erro ao calcular a derivada em y: {e}")
        return None

def exibe_derivada_em_y(function):
    try:
        derivada = calcula_derivada_em_y(function)
        if derivada is not None:
            print(f"Derivada parcial em y: {derivada}")
    except ValueError as ve:
        print(f"ValueError ao exibir a derivada em y tente verificar a entrada de dados: {ve}")
        return None
    except Exception as e:
        print(f"Erro ao exibir a derivada em y: {e}")
    

def aplica_derivada_em_x_no_ponto(function, x0, y0):
    try:
        derivada = calcula_derivada_em_x(function)
        if derivada is not None:
            return derivada.subs({x: x0, y: y0})
    except Exception as e:
        print(f"Erro ao aplicar a derivada em x no ponto ({x0}, {y0}): {e}")
        return None

def aplica_derivada_em_y_no_ponto(function, x0, y0):
    try:
        derivada = calcula_derivada_em_y(function)
        if derivada is not None:
            return derivada.subs({x: x0, y: y0})
    except Exception as e:
        print(f"Erro ao aplicar a derivada em y no ponto ({x0}, {y0}): {e}")
        return None

def calcula_plano_tangente(x0, y0, f):
    try:
        df_dx = sp.diff(f, x)
        df_dy = sp.diff(f, y)
        df_dx_x0y0 = df_dx.subs({x: x0, y: y0})
        df_dy_x0y0 = df_dy.subs({x: x0, y: y0})
        f_x0y0 = f.subs({x: x0, y: y0})
        return df_dx_x0y0 * (x - x0) + df_dy_x0y0 * (y - y0) + f_x0y0
    except Exception as e:
        print(f"Erro ao calcular o plano tangente no ponto ({x0}, {y0}): {e}")
        return None

def exibe_plano_tangente(point, f):
    try:
        plano = calcula_plano_tangente(point[0], point[1], f)
        if plano is not None:
            print(f"Plano tangente: {plano}")
    except Exception as e:
        print(f"Erro ao exibir o plano tangente: {e}")

def reta_normal(x0, y0, f):
    try:
        f_x0y0 = f.subs({x: x0, y: y0})
        dx = aplica_derivada_em_x_no_ponto(f, x0, y0)
        dy = aplica_derivada_em_y_no_ponto(f, x0, y0)
        if dx is not None and dy is not None:
            vetor_1 = [x0, y0, f_x0y0]
            vetor_2 = [-dx * t, -dy * t, 1 * t]
            soma = [vetor_1[i] + vetor_2[i] for i in range(3)]
            return f"(x, y, z) = ({soma[0]}, {soma[1]}, {soma[2]})"
    except Exception as e:
        print(f"Erro ao calcular a reta normal no ponto ({x0}, {y0}): {e}")
        return None

def exibe_reta_normal(x0, y0, f):
    try:
        reta = reta_normal(x0, y0, f)
        if reta is not None:
            print(f"Reta normal: {reta}")
    except Exception as e:
        print(f"Erro ao exibir a reta normal: {e}")

def calcular_derivadas_implicitas(equacao):
    try:
        todas_variaveis = [sp.Symbol(var) for var in ['x', 'y', 'z']]
        variaveis_presentes = [var for var in todas_variaveis if var in equacao.free_symbols]
        combinacoes = list(itertools.product(variaveis_presentes, repeat=2))
        resultados = []
        for dep, ind in combinacoes:
            resultado = derivada_implicita(equacao, dep, ind)
            resultados.append({
                "var_dependente": dep,
                "var_independente": ind,
                "resultado": resultado
            })
        return resultados
    except Exception as e:
        print(f"Erro ao calcular as derivadas implícitas: {e}")
        return []

def derivada_implicita(equacao, var_dependente, var_independente):
    try:
        independente = sp.diff(equacao, var_independente)
        dependente = sp.diff(equacao, var_dependente)
        dImplicita = -independente / dependente if dependente != 0 else "Indefinida"
        return sp.nsimplify(dImplicita)
    except Exception as e:
        print(f"Erro ao calcular a derivada implícita de {var_dependente} em relação a {var_independente}: {e}")
        return None

def exibe_derivada_implicita(equacao, dependente, independente):
    try:
        derivada = derivada_implicita(equacao, dependente, independente)
        if derivada is not None:
            print(f"Derivada de {dependente} em relação a {independente}: {derivada}")
    except Exception as e:
        print(f"Erro ao exibir a derivada implícita: {e}")

def max_min_points_2var(expression, var1, var2):
    try:
        v1, v2 = sp.symbols([var1, var2])
        f_v1 = sp.diff(expression, v1)
        f_v2 = sp.diff(expression, v2)
        critical_points = sp.solve([f_v1, f_v2], (v1, v2), dict=True)
        f_v1_v1 = sp.diff(f_v1, v1)
        f_v2_v2 = sp.diff(f_v2, v2)
        f_v1_v2 = sp.diff(f_v1, v2)
        results = []
        for point in critical_points:
            v1_val = point[v1]
            v2_val = point[v2]
            H11 = f_v1_v1.subs({v1: v1_val, v2: v2_val})
            H22 = f_v2_v2.subs({v1: v1_val, v2: v2_val})
            H12 = f_v1_v2.subs({v1: v1_val, v2: v2_val})
            det_hessian = H11 * H22 - H12**2
            if det_hessian > 0:
                if H11 > 0:
                    results.append((v1_val, v2_val, "Mínimo"))
                elif H11 < 0:
                    results.append((v1_val, v2_val, "Máximo"))
            elif det_hessian < 0:
                results.append((v1_val, v2_val, "Ponto de Sela"))
            else:
                results.append((v1_val, v2_val, "Indeterminado"))
        return results
    except Exception as e:
        print(f"Erro ao calcular os pontos de máximo e mínimo: {e}")
        return []

def exibe_maximos_minimos(equacao):
    try:
        max_min = max_min_points_2var(equacao, 'x', 'y')
        if max_min:
            print(f"Máximos e mínimos: {max_min}")
    except Exception as e:
        print(f"Erro ao exibir os pontos de máximo e mínimo: {e}")
def calcula_derivada_em_x(function):
    return sp.diff(function, x)

def exibe_derivada_em_x(function):
    return print(f"Derivada parcial em x: {calcula_derivada_em_x(function)}")

def calcula_derivada_em_y(function):
    return sp.diff(function, y)

def exibe_derivada_em_y(function):
    return print(f"Derivada parcial em y: {calcula_derivada_em_y(function)}")

def aplica_derivada_em_x_no_ponto(function, x0, y0):
    return calcula_derivada_em_x(function).subs({x: x0, y: y0})

def aplica_derivada_em_y_no_ponto(function, x0, y0):
    return calcula_derivada_em_y(function).subs({x: x0, y: y0})

def calcula_plano_tangente(x0, y0, f):
    df_dx = sp.diff(f, x)
    df_dy = sp.diff(f, y)
    df_dx_x0y0 = df_dx.subs({x: x0, y: y0})
    df_dy_x0y0 = df_dy.subs({x: x0, y: y0})
    f_x0y0 = f.subs({x: x0, y: y0})
    return df_dx_x0y0 * (x - x0) + df_dy_x0y0 * (y - y0) + f_x0y0

def exibe_plano_tangente(point, f):
    return print(f"plano tangente: {calcula_plano_tangente(point[0], point[1], f)}")

def reta_normal(x0, y0, f):
    f_x0y0 = f.subs({x: x0, y: y0})
    dx = aplica_derivada_em_x_no_ponto(f, x0, y0)
    dy = aplica_derivada_em_y_no_ponto(f, x0, y0)
    vetor_1 = [x0, y0, f_x0y0]
    vetor_2 = [-dx * t, -dy * t, 1 * t]
    soma = [vetor_1[i] + vetor_2[i] for i in range(3)]
    return f"(x, y, z) = ({soma[0]}, {soma[1]}, {soma[2]})"

def exibe_reta_normal(x0, y0, f):
    return print(f"Reta normal: {reta_normal(x0, y0, f)}")

# def vetor_unitario(i,j):
#     if i == 1 and j == 1:
#         return [i,j]
#     else:
#         return [i/(i**2+j**2)**(1/2), j/(i**2+j**2)**(1/2)]
# def derivada_direcional():
#     return (df_dx_x0y0*v[0]) + (df_dy_x0y0*v[1])


def calcular_derivadas_implicitas(equacao):
    # Variáveis padrão (x, y, z), mas filtradas pelas que estão na equação
    todas_variaveis = [sp.Symbol(var) for var in ['x', 'y', 'z']]
    variaveis_presentes = [var for var in todas_variaveis if var in equacao.free_symbols]

    # Gerar todas as combinações possíveis de variáveis presentes
    combinacoes = list(itertools.product(variaveis_presentes, repeat=2))

    resultados = []

    for dep, ind in combinacoes:
        resultado = derivada_implicita(equacao, dep, ind)
        resultados.append({
            "var_dependente": dep,
            "var_independente": ind,
            "resultado": resultado
        })

    return resultados

def derivada_implicita(equacao, var_dependente, var_independente):
    # Derivada parcial em relação à variável independente
    independente = sp.diff(equacao, var_independente)

    # Derivada parcial em relação à variável dependente
    dependente = sp.diff(equacao, var_dependente)

    # Derivada implícita
    dImplicita = -independente / dependente if dependente != 0 else "Indefinida"

    return sp.nsimplify(dImplicita)
 #para mudar parametros da função derivada implicita, utilize a logica:
 #derivada_implicita(NomeFuncao, x, y)    'parametros: implícita de x em relaçap a y'

def exibe_derivada_implicita(equacao, dependente, independente):
    return print(f"Derivada de {dependente} em relação a {independente}: {derivada_implicita(equacao, dependente, independente)}")

def max_min_points_2var(expression, var1, var2):
    # Definir as variáveis simbólicas
    v1, v2 = sp.symbols([var1, var2])

    # Calcular as derivadas parciais de primeira ordem
    f_v1 = sp.diff(expression, v1)
    f_v2 = sp.diff(expression, v2)

    # Encontrar os pontos críticos (onde as derivadas parciais são zero)
    critical_points = sp.solve([f_v1, f_v2], (v1, v2), dict=True)

    # Calcular as derivadas parciais de segunda ordem (para a matriz Hessiana)
    f_v1_v1 = sp.diff(f_v1, v1)
    f_v2_v2 = sp.diff(f_v2, v2)
    f_v1_v2 = sp.diff(f_v1, v2)  # mista

    results = []

    for point in critical_points:
        # Avaliar as coordenadas dos pontos críticos
        v1_val = point[v1]
        v2_val = point[v2]

        # Avaliar as segundas derivadas no ponto crítico
        H11 = f_v1_v1.subs({v1: v1_val, v2: v2_val})
        H22 = f_v2_v2.subs({v1: v1_val, v2: v2_val})
        H12 = f_v1_v2.subs({v1: v1_val, v2: v2_val})

        # Determinante da matriz Hessiana
        det_hessian = H11 * H22 - H12**2

        # Verificar se é máximo, mínimo ou ponto de sela
        if det_hessian > 0:
            if H11 > 0:
                results.append((v1_val, v2_val, "Mínimo"))
            elif H11 < 0:
                results.append((v1_val, v2_val, "Máximo"))
        elif det_hessian < 0:
            results.append((v1_val, v2_val, "Ponto de Sela"))
        else:
            results.append((v1_val, v2_val, "Indeterminado"))

    return results

def exibe_maximos_minimos(equação):
    return print(f"Maximos e minimos: {max_min_points_2var(equação, 'x', 'y')}")
