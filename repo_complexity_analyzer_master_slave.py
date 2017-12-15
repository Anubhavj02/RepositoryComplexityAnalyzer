import argparse

from flask import Flask  # To implement rest service
import time
import repo_complexity_analyzer

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
