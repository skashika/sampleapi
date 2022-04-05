# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from flask import Flask, render_template
from flask import request

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')


# @app.route('/input', methods=['POST'])
# def addOne():
    # new_quark = request.get_json()
    # print('Input from user: ', new_quark)
    # x = {"sum": new_quark["value1"] + new_quark["value2"]}
    # print('Output: ', x)
    # return x


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    app.run(debug=True)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
