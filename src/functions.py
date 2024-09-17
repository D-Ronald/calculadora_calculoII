import sympy as smp
x,y,z,t = smp.symbols("x y z t") 

def verify_vector(function, point):
    try:
        if len(point) != 3:
            return False
        if type(point[0]) != float  or type(point[1]) != float or type(point[2])!= float:
            return False
        if function.subs({x:point[0], y:point[1]}) != point[2]:
            return True
        return True
    except Exception as e:
        return False

def clear_comma(string):
    return string.split(',')
    
def str_to_float(point):
    point = clear_comma(point)
    return [float(point[0]), float(point[1]), float(point[2])]