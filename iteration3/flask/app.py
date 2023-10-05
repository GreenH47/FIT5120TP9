from flask import Flask, render_template, request, Response

from api_lambda_py.know_your_area import lambda_handler as know_your_area_lambda_handler
from api_lambda_py.sort_your_trash import lambda_handler as sort_your_trash_lambda_handler
from api_lambda_py.calendar_test import check_schedule as collect_date_lambda_handler

app = Flask(__name__)

'''
Page routing 
  _____                   _____             _   _             
 |  __ \                 |  __ \           | | (_)            
 | |__) |_ _  __ _  ___  | |__) |___  _   _| |_ _ _ __   __ _ 
 |  ___/ _` |/ _` |/ _ \ |  _  // _ \| | | | __| | '_ \ / _` |
 | |  | (_| | (_| |  __/ | | \ \ (_) | |_| | |_| | | | | (_| |
 |_|   \__,_|\__, |\___| |_|  \_\___/ \__,_|\__|_|_| |_|\__, |
              __/ |                                      __/ |
             |___/                                      |___/ 

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


@app.route('/collect-date.html')
def collect_date():
    return render_template('collect-date.html')


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
Api routing
                 _   _____             _   _             
     /\         (_) |  __ \           | | (_)            
    /  \   _ __  _  | |__) |___  _   _| |_ _ _ __   __ _ 
   / /\ \ | '_ \| | |  _  // _ \| | | | __| | '_ \ / _` |
  / ____ \| |_) | | | | \ \ (_) | |_| | |_| | | | | (_| |
 /_/    \_\ .__/|_| |_|  \_\___/ \__,_|\__|_|_| |_|\__, |
          | |                                       __/ |
          |_|                                      |___/ 

'''


@app.route('/api/rest/collect-date', methods=['POST'])
def collect_date_api():
    data = request.get_json()
    response = collect_date_lambda_handler(data)
    return response



@app.route('/api/rest/know-your-area', methods=['POST'])
def know_your_area_api():
    # pass
    data = request.get_json()  # Get the request data from the client
    # print(data)
    response = know_your_area_lambda_handler(data, None)  # Call the lambda function
    # print(response)
    return response  # Return the response as JSON


@app.route('/api/rest/sort-your-trash', methods=['POST'])
def sort_your_trash_api():
    data = request.get_json()
    response = sort_your_trash_lambda_handler(data, None)
    return response


@app.route('/api/rest/find-your-recycler', methods=['POST'])
def council_api():
    pass


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
