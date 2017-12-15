import argparse

from flask import Flask  # To implement rest service
import shutil  # Package for operation files and directories
import os
import time
from dask.distributed import Client, progress  # Package to implement distributed and parallel computing
import json
import repo_complexity_analyzer


app = Flask(__name__)

# Dask Client Master Server
dask_master_server = Client('127.0.0.1:8786')


def complexity_without_distributed(file_list):
    """function to compute complexity of the list of files in non-distributed tradition looping way
                    Args:
                        file_list: list of files to be computed
    """
    file_complexity_list = []
    # Start the timer to track time
    start_time = time.time()
    for path in file_list:
        file_complexity_list.append(repo_complexity_analyzer.complexity_analyzer(path))
    print("--- %s seconds ---" % (time.time() - start_time))
    return json.dumps(file_complexity_list)


def complexity_with_distributed(file_list):
    """function to compute complexity of the list of files in a distributed master-slave server methodology
                    Args:
                        file_list: list of files to be computed
    """

    # Start the timer to track time
    start_time = time.time()
    dask_master_server_node = dask_master_server.map(repo_complexity_analyzer.complexity_analyzer, file_list)
    progress(dask_master_server_node)
    print("--- %s seconds ---" % (time.time() - start_time))
    complexity_result_list = dask_master_server.gather(dask_master_server_node)
    return json.dumps(complexity_result_list)


@app.route('/calculateComplexityDistributed')
def calc_complexity_distributed():
    """Rest service function to calculate complexity of a Git Repo using distributed computing
    """
    file_list, path = repo_complexity_analyzer.clone_clean_gitrepo()
    print "Length:" + str(len(file_list))
    complexity_results = complexity_with_distributed(file_list)

    # Remove the git cloned folder after use
    if os.path.isdir(path):
        shutil.rmtree(path)

    return complexity_results


@app.route('/calculateComplexityNonDistributed')
def calc_complexity_non_distributed():
    """Rest service function to calculate complexity of a Git Repo using traditional for loop
    """
    file_list, path = repo_complexity_analyzer.clone_clean_gitrepo()
    complexity_without_distributed(file_list)

    # Remove the git cloned folder after use
    if os.path.isdir(path):
        shutil.rmtree(path)

    return "success"


if __name__ == '__main__':

    args_parser = argparse.ArgumentParser()
    args_parser.add_argument(
        '--server_host',
        type=str,
        default='127.0.0.1',
        help='IP of server where it is hosted'
    )
    args_parser.add_argument(
        '--server_port',
        type=int,
        default=8000,
        help='port of the server'
    )

    ARGS, unparsed = args_parser.parse_known_args()

    # run the server
    app.run(port=ARGS.server_port, host=ARGS.server_host)