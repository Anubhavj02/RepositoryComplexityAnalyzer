import json
from git import Repo  # Package for GIT operations
from flask import request
import os
import subprocess  # Package to get output content from input/Output/Error pipe
import shutil


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
    cyclomatic_complexity = subprocess.Popen(["radon cc \"" + path + "\" -s -j"], stdout=subprocess.PIPE,
                                             shell=True,
                                             executable='/bin/bash')

    # Get result through subprocess
    (cyclomatic_complexity, err) = cyclomatic_complexity.communicate()

    # Join both results
    return json.loads(cyclomatic_complexity)


def clone_clean_gitrepo(gitUrl=None):
    """function to clone, clean and accumulate the file list path from the given git repo
                    Args:
                        file_list: list of files to be computed
    """
    file_list = []
    # Get the url from the request
    if gitUrl is None:
        url = request.args.get('url')
    else:
        url= gitUrl
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
