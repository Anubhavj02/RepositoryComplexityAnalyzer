from flask import Flask
from git import Repo
from flask import request

app = Flask(__name__)


@app.route('/calculateComplexity')
def calc_complexity():
    url = request.args.get('url')
    name = (url.split('/')[-1]).split('.')[0]
    print name
    path = "/repos/" + name
    Repo.clone_from(url, path)
    return "success"


if __name__ == '__main__':
    app.run()
