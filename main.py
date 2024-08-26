from flask import Flask , jsonify, request
from sympy.logic.inference import valid
from sympy.polys.polyoptions import Method
import derivada, sympy as smp, functions

app = Flask(__name__)

@app.route("/plano", methods = ["GET"])
def plano_tangente():
  try :
    function = request.args.get('function')
    point_parameter = request.args.get('vector')
    point = functions.str_to_float(point_parameter)
    
    if 'function' not in request.args:
      result = "No have function"
    if 'vector' not in request.args:
      result = "No have vector"
      return jsonify(result)
    if functions.verify_vector(smp.sympify(function), point) == False:
      result = "Value of vector is not valid"
      return jsonify(result)
    else:
      result = {"plano_tangente": derivada.exibe_plano_tangente(point)}
      return jsonify(result)
  except Exception as e:
    result = {"Error": str(e)}
    return jsonify(result)

if __name__ == "__main__":
  app.run (host = "0.0.0.0")