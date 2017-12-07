from flask import Flask
from git import Repo
from flask import request
import shutil
import os

app = Flask(__name__)


def create_file_list(file_list, dir, filenames):
    for filename in filenames:
        if filename.endswith('.py'):
            file_list.append(str(os.path.join(dir, filename).encode('ascii', 'ignore')))


@app.route('/calculateComplexity')
def calc_complexity():
    file_list = []
    url = request.args.get('url')
    name = (url.split('/')[-1]).split('.')[0]
    print name
    path = "/repos/" + name
    Repo.clone_from(url, path)
    if os.path.isdir(path + "/.git"):
        shutil.rmtree(path + "/.git")
    path = os.path.expanduser(path)
    if os.path.isdir(path):
        os.path.walk(path, create_file_list, file_list)
    return "success"


if __name__ == '__main__':
    app.run()
