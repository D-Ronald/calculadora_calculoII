import derivada as dv
from derivada import *
import sympy as smp

function = "x**2 + y**2"
function_symb = smp.sympify(function)

def test_calcula_derivada_em_x():
    actual_result = smp.diff(function_symb,x)
    function = x**2
    expected_result = smp.diff(function)
    assert type(actual_result) == type(expected_result)
    
def test_calcula_derivada_em_y():
    actual_result = dv.calcula_derivada_em_y(function_symb)
    expected_result = 2*y
    assert actual_result == expected_result