from flask import Flask  # To implement rest service
from git import Repo  # Package for GIT operations
from flask import request
import shutil  # Package for operation files and directories
import os
import subprocess  # Package to get output content from input/Output/Error pipe
import time
from dask.distributed import Client  # Package to implement distributed and parallel computing
import json


app = Flask(__name__)

# Dask Client Master Server
dask_master_server = Client('127.0.0.1:8786')


def create_file_list(file_list, directory, filenames):
    """function to get the names and directory of the python files from the cloned git folder
                Args:
                    file_list: list of all the file names along with the path
                    directory: directory to be parsed
                    filenames: list of all filenames in the given directory
    """

    # Iterate through all the files in the directory
    for filename in filenames:
        # Check whether it is python file or not if yes add it to the file list
        if filename.endswith('.py'):
            # Encoding unicode to ascii and converting to string
            file_list.append(str(os.path.join(directory, filename).encode('ascii', 'ignore')))


def complexity_analyzer(path):
    """function to get complexity and raw data analysis of the file/files mentioned in the path
                Args:
                    path: path of the file/ files whose complexity is to be analyzed
    """

    # compute the cyclomatic complexity
    cyclomatic_complexity = subprocess.Popen(["radon cc \"" + path + "\" -s -j"], stdout=subprocess.PIPE, shell=True,
                                             executable='/bin/bash')

    # Get result through subprocess
    (cyclomatic_complexity, err) = cyclomatic_complexity.communicate()

    # Join both results
    return json.loads(cyclomatic_complexity)


def complexity_without_distributed(file_list):
    """function to compute complexity of the list of files in non-distributed tradition looping way
                    Args:
                        file_list: list of files to be computed
    """

    file_complexity_list = []
    # Start the timer to track time
    start_time = time.time()
    for path in file_list:
        file_complexity_list.append(complexity_analyzer(path))
    print("--- %s seconds ---" % (time.time() - start_time))
    return json.dumps(file_complexity_list)


def complexity_with_distributed(file_list):
    """function to compute complexity of the list of files in a distributed master-slave server methodology
                    Args:
                        file_list: list of files to be computed
    """

    # Start the timer to track time
    start_time = time.time()
    dask_master_server_node = dask_master_server.map(complexity_analyzer, file_list)
    complexity_result_list = dask_master_server.gather(dask_master_server_node)
    print("--- %s seconds ---" % (time.time() - start_time))
    return json.dumps(complexity_result_list)


def clone_clean_gitrepo():
    """function to clone, clean and accumulate the file list path from the given git repo
                    Args:
                        file_list: list of files to be computed
    """
    file_list = []
    # Get the url from the request
    url = request.args.get('url')
    # Split the url to get name of repository
    name = (url.split('/')[-1]).split('.')[0]
    # path to store repo
    path = "/repos/" + name
    # Clone the repo to the given path
    Repo.clone_from(url, path)
    # Delete the unwanted git folder
    if os.path.isdir(path + "/.git"):
        shutil.rmtree(path + "/.git")

    # Correct the path with the user's home directory
    path = os.path.expanduser(path)

    # check path is a valid directory
    if os.path.isdir(path):
        # Traverse through the directory
        os.path.walk(path, create_file_list, file_list)

    return file_list, path


@app.route('/calculateComplexityDistributed')
def calc_complexity_distributed():
    """Rest service function to calculate complexity of a Git Repo using distributed computing
    """
    file_list, path = clone_clean_gitrepo()
    complexity_results = complexity_with_distributed(file_list)

    # Remove the git cloned folder after use
    if os.path.isdir(path):
        shutil.rmtree(path)

    return complexity_results


@app.route('/calculateComplexityNonDistributed')
def calc_complexity_non_distributed():
    """Rest service function to calculate complexity of a Git Repo using traditional for loop
    """
    file_list, path = clone_clean_gitrepo()
    complexity_without_distributed(file_list)

    # Remove the git cloned folder after use
    if os.path.isdir(path):
        shutil.rmtree(path)

    return "success"


if __name__ == '__main__':
    app.run()
