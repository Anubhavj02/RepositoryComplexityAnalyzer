import argparse  # For accessing the command line arguments
from distributed import Scheduler  # Dask distributed scheduler
from tornado.ioloop import IOLoop
from threading import Thread
import dask_worker_servers # Dask work file

args_parser = argparse.ArgumentParser()

args_parser.add_argument(
    '--dask_ip',
    type=str,
    default="127.0.0.1",
    help='port of the dask server'
)

args_parser.add_argument(
    '--dask_port',
    type=str,
    default="8786",
    help='port of the dask server'
)

args_parser.add_argument(
    '--num_worker',
    type=str,
    default=2,
    help='port of the dask server'
)

ARGS, unparsed = args_parser.parse_known_args()

loop = IOLoop.current()
t = Thread(target=loop.start)
t.start()

# Start the dask scheduler/master on the port
s = Scheduler(loop=loop)
s.start('tcp://'+str(ARGS.dask_ip)+':'+str(ARGS.dask_port))

# Initialize the dask workers
dask_worker_servers.create_worker(ARGS.num_worker, ARGS.dask_ip, ARGS.dask_port)