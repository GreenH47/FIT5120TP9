from flask import Flask, render_template, request, Response

# from lambda_py.council_lambda import lambda_handler as know_your_area_lambda_handler

app = Flask(__name__)

'''
page routes
'''


# Set up basic authentication
@app.before_request
def require_basic_auth():
    auth = request.authorization

    # Verify username and password
    username = 'guest'
    password = 'MRzYpG7yonPO8'

    if not auth or auth.username != username or auth.password != password:
        return Response(
            'Unauthorized', 401, {'WWW-Authenticate': 'Basic realm="Login Required"'}
        )


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/index.html')
def index2():
    return render_template('index.html')


@app.route('/glass-bottle.html')
def glass_bottle():
    return render_template('glass-bottle.html')


@app.route('/find-your-recycler.html')
def find_your_recycler():
    return render_template('find-your-recycler.html')


@app.route('/know-your-area.html')
def know_your_area():
    return render_template('know-your-area.html')


@app.route('/lamp.html')
def lamp():
    return render_template('lamp.html')


@app.route('/lantern.html')
def lantern():
    return render_template('lantern.html')


@app.route('/plastic-bottle.html')
def plastic_bottle():
    return render_template('plastic-bottle.html')


@app.route('/plastic-bottle-coin-storage.html')
def plastic_bottle_coin_storage():
    return render_template('plastic-bottle-coin-storage.html')


@app.route('/sort-your-trash.html')
def sort_your_trash():
    return render_template('sort-your-trash.html')


@app.route('/resources.html')
def resources():
    return render_template('resources.html')


'''
api routes
'''


# too slow then I gave up on run it on flask
@app.route('/api/rest/know-your-area', methods=['POST'])
def know_your_area_api():
    pass
    # data = request.get_json()  # Get the request data from the client
    # print(data)
    # response = know_your_area_lambda_handler(data, None)  # Call the lambda function
    # print(response)
    # return response  # Return the response as JSON


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
