#!/usr/bin/env bash
# Script file for executing the chat server on the machine and accept the first command line argument as port number

echo "Name: Anubhav Jain, Student Id: 17310876"

echo "Master Slave Complexity Analyzer Using Distributed Computing"

echo "Running Master Server"
python repo_complexity_analyzer_master_slave.py --server_host $1 --server_port $2 --url $3 --num_worker $4