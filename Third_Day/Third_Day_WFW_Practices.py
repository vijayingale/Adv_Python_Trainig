from flask import Flask, jsonify, request, make_response

app = Flask(__name__)

International_cricketer = {
    "India" : {
        "Viarat_Kohali" : 18,
        "Rohit_Sharma" : 45,
        "Shikar_Dhavan" : 42,
        "Rushab_Pant" : 77,
        "KL_Rahul" : 34,
        "Hardik_Pandya " : 44,
        "Shreyas_iyar " : 56,
        "Ravindra_jadeja " :34,
        "Jasprit_Bhumara" : 58,
        "Uzevendra_Chahal" : 56,
        "Rahul_Chahal" :67,
        "Suryakumar_yadv":45,
        "Bhuvneshwar_kumar" : 45,
        "Muhamad_Shami" : 45,
        "muhammad_siraj" : 56
        }

}
@app.route("/International_cricketer/<collection>")
def get_collection(collection):
    if collection in International_cricketer:
        res = make_response(jsonify(International_cricketer[collection]),200)
        return res
    res = make_response(jsonify({"error":"Not Found"}),468)
    return res


@app.route("/International_cricketer/<collection>/<member>")
def get_member(collection, member):
    if collection in International_cricketer:
        member = International_cricketer[collection].get(member)
        print(member)
        if member:
            res = make_response(jsonify(member),200)
            return res
        res = make_response(jsonify({"Error" : "Not Found"}),404)
        return res


@app.route("/International_cricketer/<collection>",methods=["PUT"])
def replace_Collection(collection,):
    req = request.get_json()
    if collection in International_cricketer:
        International_cricketer[collection] = req
        res = make_response(jsonify({"msg":"Collection Updated"}), 200)
        return res
    res = make_response(jsonify({"Error": "Not Found Replace Collection "}),404)
    return res


@app.route("/International_cricketer/<collection>/<member>",methods=["PUT"])
def put_collection(collection ,member):
    req = request.get_json()
    if collection in International_cricketer:
        member = International_cricketer[collection]
        for key,value in req.items():
            if key in member:
                member[key] = value
            else :
                member[key] = value

        res = make_response(jsonify({"msg" : "Collection Update"}),200)
        return res



@app.route("/International_cricketer/<collection>",methods=["DELETE"])
def delete_collection(collection):
    if collection in International_cricketer:
        del International_cricketer[collection]
        res = make_response(jsonify({"mag":"Collection Deleted"}),200)
        return res
    res = make_response(jsonify({"Error": "Not Found"}),404)
    return res



@app.route("/International_cricketer/<collection>/<member>",methods=["DELETE"])
def delete_Single_collection(collection , member):
    if collection in International_cricketer:
        if member in International_cricketer[collection]:

            del International_cricketer[collection][member]
            res = make_response(jsonify({"mag":"Collection Deleted"}),200)
            return res
        else:
            res = make_response(jsonify({"Error": " Record Not Found"}),404)
            return res







if __name__=='__main__':
    app.run(debug=True , port= 5001)