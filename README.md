# Distributed Computing Rest Service Cyclomatic Complexity

This application is a rest service enabled cyclomatic complexity calculator of a given GITHUB respository using distributed and parallel computing. It shows a clear distinction between distributed/ parrallel computing and normal traditional single model based computing in terms of the execution time.

>Name: Anubhav Jain
<br>TCD Student ID: 17310876

This chat server can support multiple clients where clients can join chat rooms, post messages and retrieve messages, and leave chat rooms.

## Dependencies Required
* Python 2.7
* Flask 0.12.2 - Rest service package
* Dask 0.16.0 - Python Distributed and Parallel computing package
* Lizard 1.13.0 - Python package to calculate the cyclomatic complexity
* Radon 2.1.1

## Code Complexity Methodology
* **Using dask distributed python package:** Here dask package is used to handle the master-worker architecture and radon is used raw and complexity metrics calculation, a JSON file is received at the end with all the metrics.
* **Using the user created master-slave architectur:** Here user defined master-slave architecture is created and the master controls the slave and alots them work, here Lizard package is used to calculate the average complexity, in the command line the average complexity and time is printed

# Code Complexity Using Dask Distributing Method
## Starting the servers and running the code
1. **Running the dask master and worker server**
```
sh dask_start.sh {dask_server_ip} {dask_server_port} {dask_number_of_worker}
```
* dask_server_ip: IP of the sever on which dask will run
* dask_server_port: port of the dask server
* dask_num_of_worker: number of Workers for distributed system

or you can run directly with default dask arguments

```
python dask_master_server.py
```
**Default values are:**
* IP (localhost): 127.0.0.1
* Port: 8786
* Number of workers: 2

***

2. **Running the Dask Manager that will cater to all rest requests**
```
sh dask_manager_server_start.sh {server_host} {server_port} {dask_ip} {dask_port}
```
* server_host: Host Ip on which the server will run
* server_port: port the of the manager server
* dask_ip: IP of the sever on which dask will run
* dask_port: port of the dask server

or you can run directly with default dask arguments

```
python repo_complexity_analyzer_server_dask.py
```
**Default values are:**
* Server Host (localhost): 127.0.0.1
* Server Port: 8000
* Dask Server Host (localhost): 127.0.0.1
* Dask Port: 8786

***

## Testing the Complexity of Dask Distributed Server
Assuming our server is running localhost 127.0.0.1 and port 8000
Checking complexity of the GITHUB repo "https://github.com/Anubhavj02/ScalableComputingChatApplication.git"
1. **Testing the Non Distributed Traditional Approach**
<br>

open the browser hit
```sh
http://127.0.0.1:8000/calculateComplexityNonDistributed?url=https://github.com/Anubhavj02/ScalableComputingChatApplication.git
```
Output with raw and complexity metrics using normal flow 
<br>**On browser** 

```json
[{"/repos/ScalableComputingChatApplication/ChatServer.py": [{"name": "process_message", "col_offset": 4, "rank": "C", "classname": "ClientThread", "complexity": 11, "closures": [], "endline": 216, "type": "method", "lineno": 174}, {"name": "ClientThread", "col_offset": 0, "rank": "A", "complexity": 5, "lineno": 156, "endline": 216, "type": "class", "methods": [{"name": "__init__", "col_offset": 4, "rank": "A", "classname": "ClientThread", "complexity": 1, "closures": [], "endline": 162, "type": "method", "lineno": 158}, {"name": "run", "col_offset": 4, "rank": "A", "classname": "ClientThread", "complexity": 3, "closures": [], "endline": 172, "type": "method", "lineno": 165}, {"name": "process_message", "col_offset": 4, "rank": "C", "classname": "ClientThread", "complexity": 11, "closures": [], "endline": 216, "type": "method", "lineno": 174}]}, {"closures": [], "name": "server_main", "col_offset": 0, "rank": "A", "complexity": 4, "lineno": 455, "endline": 485, "type": "function"}, {"name": "remove_user_from_chat_room", "col_offset": 4, "rank": "A", "classname": "Chatroom", "complexity": 3, "closures": [], "endline": 126, "type": "method", "lineno": 104}, {"name": "run", "col_offset": 4, "rank": "A", "classname": "ClientThread", "complexity": 3, "closures": [], "endline": 172, "type": "method", "lineno": 165}, {"closures": [], "name": "process_join_msg", "col_offset": 0, "rank": "A", "complexity": 2, "lineno": 219, "endline": 233, "type": "function"}, {"closures": [], "name": "process_hello_msg", "col_offset": 0, "rank": "A", "complexity": 2, "lineno": 236, "endline": 251, "type": "function"}, {"closures": [], "name": "process_leave_msg", "col_offset": 0, "rank": "A", "complexity": 2, "lineno": 254, "endline": 268, "type": "function"}, {"closures": [], "name": "process_chat_msg", "col_offset": 0, "rank": "A", "complexity": 2, "lineno": 271, "endline": 285, "type": "function"}, {"closures": [], "name": "process_disconnect_msg", "col_offset": 0, "rank": "A", "complexity": 2, "lineno": 288, "endline": 302, "type": "function"}, {"closures": [], "name": "disconnect_user_from_chatroom", "col_offset": 0, "rank": "A", "complexity": 2, "lineno": 305, "endline": 328, "type": "function"}, {"closures": [], "name": "broadcast_msg_chatroom_users", "col_offset": 0, "rank": "A", "complexity": 2, "lineno": 331, "endline": 356, "type": "function"}, {"closures": [], "name": "create_chat_room", "col_offset": 0, "rank": "A", "complexity": 2, "lineno": 359, "endline": 388, "type": "function"}, {"closures": [], "name": "delete_from_chat_room", "col_offset": 0, "rank": "A", "complexity": 2, "lineno": 391, "endline": 422, "type": "function"}, {"closures": [], "name": "send_msg_to_client", "col_offset": 0, "rank": "A", "complexity": 2, "lineno": 440, "endline": 451, "type": "function"}, {"name": "Chatroom", "col_offset": 0, "rank": "A", "complexity": 2, "lineno": 36, "endline": 152, "type": "class", "methods": [{"name": "__init__", "col_offset": 4, "rank": "A", "classname": "Chatroom", "complexity": 1, "closures": [], "endline": 53, "type": "method", "lineno": 41}, {"name": "add_user_to_chat_room", "col_offset": 4, "rank": "A", "classname": "Chatroom", "complexity": 1, "closures": [], "endline": 79, "type": "method", "lineno": 55}, {"name": "send_chat_msg", "col_offset": 4, "rank": "A", "classname": "Chatroom", "complexity": 2, "closures": [], "endline": 102, "type": "method", "lineno": 81}, {"name": "remove_user_from_chat_room", "col_offset": 4, "rank": "A", "classname": "Chatroom", "complexity": 3, "closures": [], "endline": 126, "type": "method", "lineno": 104}, {"name": "disconnect_user_from_chat_room", "col_offset": 4, "rank": "A", "classname": "Chatroom", "complexity": 2, "closures": [], "endline": 152, "type": "method", "lineno": 128}]}, {"name": "send_chat_msg", "col_offset": 4, "rank": "A", "classname": "Chatroom", "complexity": 2, "closures": [], "endline": 102, "type": "method", "lineno": 81}, {"name": "disconnect_user_from_chat_room", "col_offset": 4, "rank": "A", "classname": "Chatroom", "complexity": 2, "closures": [], "endline": 152, "type": "method", "lineno": 128}, {"closures": [], "name": "send_error_msg_to_client", "col_offset": 0, "rank": "A", "complexity": 1, "lineno": 425, "endline": 437, "type": "function"}, {"name": "__init__", "col_offset": 4, "rank": "A", "classname": "Chatroom", "complexity": 1, "closures": [], "endline": 53, "type": "method", "lineno": 41}, {"name": "add_user_to_chat_room", "col_offset": 4, "rank": "A", "classname": "Chatroom", "complexity": 1, "closures": [], "endline": 79, "type": "method", "lineno": 55}, {"name": "__init__", "col_offset": 4, "rank": "A", "classname": "ClientThread", "complexity": 1, "closures": [], "endline": 162, "type": "method", "lineno": 158}]}, {"/repos/ScalableComputingChatApplication/ChatClient.py": [{"closures": [], "name": "client_main", "col_offset": 0, "rank": "A", "complexity": 5, "lineno": 6, "endline": 52, "type": "function"}, {"closures": [], "name": "send_receive_msg", "col_offset": 0, "rank": "A", "complexity": 1, "lineno": 55, "endline": 58, "type": "function"}]}]
```
***

**Command line Output with time in seconds***
```sh
 Length:2
127.0.0.1 - - [15/Dec/2017 19:25:57] "GET /calculateComplexityDistributed?url=https://github.com/Anubhavj02/ScalableComputingChatApplication.git HTTP/1.1" 200 -
[########################################] | 100% Completed |  0.2s--- 0.285113096237 seconds ---
```
***

# Code Complexity Using User Defined Master Slave Architecture
## Starting the servers and running the code
1. **Running the master server**
```
sh master_slave_startup_files/start_master.sh {server_host} {server_port} {url} {num_worker}
```
* server_host: IP of the sever on which master will run
* server_port: port of the master server
* url: Git repo to be clone and analyzed
* num_worker: number of Workers for distributed system

or you can run directly with default arguments

```
python repo_complexity_analyzer_master_slave.py
```
* server_host: 127.0.0.1
* server_port: 8080
* url: 'https://github.com/geekcomputers/Python.git'
* num_worker: 2

***

2. **Running the slave servers**
Run the below commands multiple times to start multiple slave servers and match the number of worker given to master above to achieve the task
```
sh master_slave_startup_files/start_slave.sh {server_host} {server_port}
```
default
* server_host: IP of the master sever on which master will run
* server_port: port of the master server

or you can run directly with default arguments

```
python complexity_slave_server.py
```
default
* server_host: 127.0.0.1
* server_port: 8080

***

## Output of the master slave architecture using Lizard
Assuming our server is running localhost 127.0.0.1 and port 8000
Checking complexity of the GITHUB repo "https://github.com/geekcomputers/Python.git"
1. **Output of the Master Server**
<br>

On the command line
```sh
('Execution Time taken: ', 0.4360389709472656)
('Average Complexity of the repo: ', 2.017622461170848)
```

2. **Output Snippet of Slave server**
```sh
/System/Library/Frameworks/Python.framework/Versions/2.7/bin/python2.7 /var/root/PycharmProjects/RepositoryComplexityAnalyzer_aj/complexity_slave_server.py
registered
--  Received from master:Waiting --
-- Pinging to the server -- 
--  Received from master:Waiting --
-- Pinging to the server -- 
--  Received from master:/repos/Python/recyclebin.py --
--  Received from master:/repos/Python/CountMillionCharacters-Variations/variation1.py --
Complexity analysis of the file:2.0
{
  "success": true
}

--  Received from master:/repos/Python/game_of_life/game_o_life.py --
Complexity analysis of the file:5.0
{
  "success": true
}

--  Received from master:Done --
-- Work Completed --
('Total Files Checked: ', 48)

Process finished with exit code 0

```

# Evaluation of results
## Dask Time vs Number of workers graph
## Master Slave Time vs Number of workers graph
