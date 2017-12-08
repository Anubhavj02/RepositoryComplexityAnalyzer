from flask import Flask
from git import Repo
from flask import request
import shutil
import os
import subprocess

app = Flask(__name__)


def create_file_list(file_list, dir, filenames):
    for filename in filenames:
        if filename.endswith('.py'):
            file_list.append(str(os.path.join(dir, filename).encode('ascii', 'ignore')))


def complexity_analyzer(path):
    raw_complexity = subprocess.Popen(["radon raw " + path + " -s -j"], stdout=subprocess.PIPE, shell=True,
                                      executable='/bin/bash')
    cyclomatic_complexity = subprocess.Popen(["radon cc " + path + " -s -j"], stdout=subprocess.PIPE, shell=True,
                                             executable='/bin/bash')
    (raw_complexity_output, err) = raw_complexity.communicate()
    (cyclomatic_complexity, err1) = cyclomatic_complexity.communicate()
    return raw_complexity_output + cyclomatic_complexity


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

    for path in file_list:
        print complexity_analyzer(path)

    return "success"


if __name__ == '__main__':
    app.run()
