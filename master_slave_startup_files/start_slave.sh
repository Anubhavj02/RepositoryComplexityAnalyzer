#!/usr/bin/env bash
# Script file for executing the chat server on the machine and accept the first command line argument as port number

echo "Name: Anubhav Jain, Student Id: 17310876"

echo "Master Slave Complexity Analyzer Using Distributed Computing"

echo "Running Slave Server"
python complexity_slave_server.py --server_host $1 --server_port $2