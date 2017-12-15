from distributed import Worker
from tornado.ioloop import IOLoop
from threading import Thread

loop = IOLoop.current()
t = Thread(target=loop.start)
t.start()


def create_worker(num_worker, server_ip, server_port):
    """ Instantiate the dask workers
        Args:
            num_worker: number of workers
            server_ip: dask scheduler IP
            server_port: dask port
    """
    for i in range(int(num_worker)):
        print "-- worker initializing --"
        dask_server = Worker('tcp://'+server_ip+":"+str(server_port), loop=loop)
        dask_server.start()