from flask import Flask
from git import Repo
from flask import request
import shutil
import os

app = Flask(__name__)


@app.route('/calculateComplexity')
def calc_complexity():
    url = request.args.get('url')
    name = (url.split('/')[-1]).split('.')[0]
    print name
    path = "/repos/" + name
    Repo.clone_from(url, path)
    if os.path.isdir(path + "/.git"):
        shutil.rmtree(path + "/.git")
    return "success"


if __name__ == '__main__':
    app.run()
