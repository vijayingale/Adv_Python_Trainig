# Django or Flask Use to

# Flask

# MVC
# Http Reponce code RFC 1656
    # 1.x
    # 2.x


from flask import Flask , request

app = Flask(__name__)

# @app.route("/create/account",method = ["post"])
@app.route("/")

# Dynamic Routing
#http:127.0.0.1/onkar
#hello onkar
def index():

    return  '<h1> Hello World </h1>'


@app.route('/user/<name>')

def user(name):

    return  '<h1> Hello %s </h1>'% name


# headers

@app.route("/headers")
def headers():
    user_agent = request.headers.get('User-Agent')
    return '<p> You Browser is %s</p>' % user_agent




if __name__ == '__main__':
    app.run(debug=True)
