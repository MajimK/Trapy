import socket

class Conn:
    def __init__(self) -> None:
        self.serv_address:str=None
        self.destination_address:str=None
        self.client:bool=False
        self.server:bool=False
        self.conections_number:list=[]
        self.socket=socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_TCP)

class ConnException:
    pass