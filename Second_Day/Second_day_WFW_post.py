from flask import Flask,jsonify,request ,make_response

app = Flask(__name__)

# income = [
#     {"description":"salary","amount":5000}
# ]
#
#
# @app.route("/incomes", method=["post"])
# def add_income():
#     income.append(request.get_json())
#     return 'Created', 201

stock = {
    "frute":{
        "apple":100,
        "banana":45,
        "cheryy":1000
    }
}
@app.route("/stock")
def get_stock():
    res = make_response(jsonify(stock),200)
    return res

@app.route("/stock/<collection>")
def get_collection(collection):
    if collection in stock:
        res =make_response(jsonify(stock[collection]),200)
        return res
    res = make_response(jsonify({"error":"Not Found"}), 484)
    return res


@app.route("/stock/<collection>/<member>")
def get_member(collection , member):
    if collection in stock:
        member = stock[collection].get(member)
        if member:
            res = make_response(jsonify(member),200)
            return res
        res = make_response(jsonify({"Error":"Not found"}),404)
        return res
    res =make_response(jsonify({"error":"not found"}),404)
    return res

if __name__=='__main__':
    app.run(debug=True , port= 5001)