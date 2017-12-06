from flask import Flask

app = Flask(__name__)


@app.route('/CalculateComplexity')
def calc_complexity():
    return 'Calculating Complexity'


if __name__ == '__main__':
    app.run()
