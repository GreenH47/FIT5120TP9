from flask import Flask, render_template,request, jsonify

from lambda_py.council_lambda import lambda_handler as know_your_area_lambda_handler

app = Flask(__name__)

'''
page routes
'''
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/index.html')
def index2():
    return render_template('index.html')

@app.route('/find-your-recycler.html')
def find_your_recycler():
    return render_template('find-your-recycler.html')

@app.route('/know-your-area.html')
def know_your_area():
    return render_template('know-your-area.html')






'''
api routes
'''

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

