from flask import Flask,jsonify,request,make_response

app = Flask(__name__)

Domestic_cricket = {
    "IPL" : {
        "MI" : 5,
        "csk" :3,
        "SRH" :1,
        "KKR" :2,
    }
}

@app.route("/Domestic_cricket/<collection>")
def get_collection(collection):
    if collection in Domestic_cricket:
        res = make_response(jsonify(Domestic_cricket[collection]),200)
        return res
    res = make_response(jsonify({"error":"Not Found"}),468)
    return res

@app.route("/Domestic_cricket/<collection>/<member>")
def get_member(collection, member):
    if collection in Domestic_cricket:
        member = Domestic_cricket[collection].get(member)
        if member:
            res = make_response(jsonify(member),200)
            return res
        res = make_response(jsonify({"Error" : "Not Found"}),404)
        return res

@app.route("/Domestic_cricket/<collection>",methods=["put"])
def put_collection(collection):
    req = request.get_json()
    if collection in Domestic_cricket:
        Domestic_cricket[collection] = req
        res = make_response(jsonify({"msg":"Collection updated"}),200)
        return res
    # Domestic_cricket[collection] = req
    # res = make_response(jsonify({"msg":"collection create.."}),201)
    # return res
    res = make_response(jsonify({"Error": "Not Found"}), 404)
    return res

@app.route("/Domestic_cricket/<collection>/<member>",methods=["put"])
def put_collection1(collection ,member):
    req = request.get_json()
    if collection in Domestic_cricket:
        member=Domestic_cricket[collection]
        for key,value in req.items():
            if key in member:
                member[key] = value
            else :
                member[key] = value
        res = make_response(jsonify({"msg":"Collection updated"}),200)
        return res
    # Domestic_cricket[collection] = req
    # res = make_response(jsonify({"msg":"collection create.."}),201)
    # return res
    res = make_response(jsonify({"Error": "Not Found"}), 404)
    return res

@app.route("/Domestic_cricket/<collection>",methods=["DELETE"])
def delete_collection(collection):
    # req = request.get_json()
    if collection in Domestic_cricket:
        del Domestic_cricket[collection]
        res = make_response(jsonify({"msg":"Collection Deleted"}),200)
        return res
    # Domestic_cricket[collection] = req
    # res = make_response(jsonify({"msg":"collection create.."}),201)
    # return res
    res = make_response(jsonify({"Error": "Not Found"}), 404)
    return res

@app.route("/Domestic_cricket/<collection>/<member>",methods=["DELETE"])
def delete_collection1(collection , member):
    # req = request.get_json()
    if collection in Domestic_cricket:
        if member in Domestic_cricket[collection]:
            del Domestic_cricket[collection][member]
            res = make_response(jsonify({"msg": " Value IS deleteDeleted"}), 204)
            return res
        else:
            res = make_response(jsonify({"error": "record Not found"}), 404)
            return res
    res = make_response(jsonify({"Error": "Not Found"}), 404)
    return res


if __name__=='__main__':
    app.run(debug=True , port= 5001)