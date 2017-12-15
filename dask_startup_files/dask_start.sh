#!/usr/bin/env bash
# Script file for executing the chat server on the machine and accept the first command line argument as port number

echo "Name: Anubhav Jain, Student Id: 17310876"

echo "Dask Complexity Analyzer Using Distributed Computing"

echo "Running Dask Master Server"
python dask_master_server.py --dask_ip $1 --dask_port $2 --num_worker $3