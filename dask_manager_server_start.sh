#!/usr/bin/env bash
# Script file for executing the chat server on the machine and accept the first command line argument as port number

echo "Name: Anubhav Jain, Student Id: 17310876"

echo "Dask Complexity Analyzer Using Distributed Computing"

echo "Running Dask Master Manager Server"
python repo_complexity_analyzer_server_dask.py --server_host $1 --server_port $2 --dask_ip $3 --dask_port $4