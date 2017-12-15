import argparse
import os, sys, requests, json
import subprocess
import repo_complexity_analyzer


def register_slave_server():
    """function to register slave server
    """
    # Register the worker to the server
    register_response = requests.get(master_server + '/registerSlave')
    print register_response.text


def perform_worker_task():
    files_checked = 0

    while True:
        # Get the work from the JSON
        file_path = json.loads(requests.get(master_server + '/complexityFromSlave').text)['status']
        print ("--  Received from master:" + str(file_path) + " --")
        # Check if the server is still waiting for other user to join
        if file_path == 'Waiting':
            print("-- Pinging to the server -- ")
        else:
            # Check if the work is done
            if file_path == 'Done':
                print("-- Work Completed --")
                break
            else:
                # Sending the file path for complexity analysis
                avg_complexity_radon = repo_complexity_analyzer.complexity_analyzer_average(file_path)

                print("Complexity analysis of the file:" + str(avg_complexity_radon))
                # If we get empty response
                if avg_complexity_radon == "":
                    print("There are no files")
                    master_response = requests.post(master_server + '/complexityFromSlave',
                                                    json={'file_path': file_path, 'complexity': -1})
                    print master_response.text
                else:
                    # Sometime we receive unknown if there is problem in calculating complexity
                    if "unknown" in str(avg_complexity_radon):
                        average_complexity = 0
                    else:
                        average_complexity = float(avg_complexity_radon)
                    master_response = requests.post(master_server + '/complexityFromSlave',
                                                    json={'file_path': file_path, 'complexity': average_complexity})
                    print master_response.text
                    files_checked += 1

    print("Total Files Checked: ", files_checked)


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

    ARGS, unparsed = args_parser.parse_known_args()

    master_server = 'http://' + ARGS.server_host + ':' + str(ARGS.server_port)
    register_slave_server()
    perform_worker_task()