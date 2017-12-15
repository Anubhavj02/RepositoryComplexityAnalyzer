import argparse

from flask import Flask  # To implement rest service
import time
import repo_complexity_analyzer
from flask import request
from flask import jsonify
import os
import shutil

app = Flask(__name__)


# Sever manager class to hold the complexity and worker related attributes
class ServerManagerNode:
    def __init__(self, slave_count, url):
        # Number slaves to be associated with the worker
        self.slave_count = slave_count
        # Current number of slaves registered
        self.current_slave_count = 0
        self.start_time = 0.0
        # List to file path and its complexity
        self.file_complexity_list = []
        # Clone and get the file list
        file_list, path = repo_complexity_analyzer.clone_clean_gitrepo(url)
        self.path = path
        # List of files whose complexity needs to be calculated
        self.file_list = file_list
        # Total number of files to be analyzed
        self.total_file = len(self.file_list)


@app.route('/complexityFromSlave', methods=['GET'])
def get_work():
    """function to assign the work to the slaves
    """

    # If the current number slaves are less than the required
    if server_manager_node.current_slave_count < server_manager_node.slave_count:
        time.sleep(0.1)
        return jsonify({'status': 'Waiting'})
    # If the repo is empty
    if len(server_manager_node.file_list) == 0:
        return jsonify({'status': 'Done'})

    # Pull the first file name
    file_path = server_manager_node.file_list[0]
    # Delete the first index such that the pointer points to the next
    del server_manager_node.file_list[0]
    print "Sending work to slave:"+file_path
    # Sending the work as response to the slave with the file path to be analyzed
    return jsonify({'status': file_path})


@app.route('/registerSlave', methods=['GET'])
def register_slave():
    """function to regsister slave to the master=
    """
    print "-- Registering the slave to the master --"
    # Increase the registered slave count
    server_manager_node.current_slave_count = server_manager_node.current_slave_count + 1
    # if the current slave count matched the required slave count start the timer
    if server_manager_node.current_slave_count == server_manager_node.slave_count:
        server_manager_node.start_time = time.time()
    return "registered"


def calculate_average_file_complexity():
    # Check whether all files have been analyzed or not
    if len(server_manager_node.file_complexity_list) == server_manager_node.total_file:
        # Stop the timer
        time_end = time.time() - server_manager_node.start_time
        print("Execution Time taken: ", time_end)
        print("No. of files analyzed:" + str(len(server_manager_node.file_complexity_list)))
        # Calculating average complexity
        average_complexity = 0
        for file_comp in server_manager_node.file_complexity_list:
            if file_comp['complexity'] > 0:
                average_complexity += file_comp['complexity']
            else:
                print("No files to be analyzed")
        average_complexity = average_complexity / len(server_manager_node.file_complexity_list)
        print("Average Complexity of the repo: ", average_complexity)

        # Remove the git cloned folder after use
        if os.path.isdir(server_manager_node.path):
            shutil.rmtree(server_manager_node.path)


@app.route('/complexityFromSlave', methods=['POST'])
def complexity_from_slave():
    """function to receive the complexity from the slaves
    """
    code_complexity_req = request.json
    file_path= code_complexity_req['file_path']
    code_complexity= code_complexity_req['complexity']
    # Add the file path and its complexity to the list
    server_manager_node.file_complexity_list.append({'file_path': file_path, 'complexity': code_complexity})
    calculate_average_file_complexity()
    return jsonify({'success': True})


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
        default=8080,
        help='port of the server'
    )

    args_parser.add_argument(
        '--url',
        type=str,
        default='https://github.com/geekcomputers/Python.git',
        help='GIT Url'
    )

    args_parser.add_argument(
        '--num_worker',
        type=int,
        default=2,
        help='number of worker'
    )

    ARGS, unparsed = args_parser.parse_known_args()
    server_manager_node = ServerManagerNode(ARGS.num_worker, ARGS.url)
    app.run(port=ARGS.server_port, host=ARGS.server_host)