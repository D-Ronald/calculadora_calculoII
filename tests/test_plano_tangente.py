from derivada import x, y, z, calcula_plano_tangente
import sympy as smp

function = 'x**y + y**x'
function_symb = smp.sympify(function)    

def test_calcula_plano_tangente():
    point = (1, 1, 2)
    actual_result = calcula_plano_tangente(point[0], point[1], function_symb)
    assert actual_result == x+y