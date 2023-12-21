from Conn import Conn
from utils import parse_address

def listen(address:str, count_connect:int): 
    status_conect=Conn()
    status_conect.server=True
    status_conect.serv_address==parse_address(address)
    status_conect.conections_number=[None for _ in range(0,count_connect)]
    return status_conect

