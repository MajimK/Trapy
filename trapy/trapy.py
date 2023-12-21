from Listen import listen
from Conn import Conn
import utils

def listen(address: str) -> Conn:
    return listen(address)

def accept(conn) -> Conn:
    pass


def dial(address) -> Conn:
    pass


def send(conn: Conn, data: bytes) -> int:
    pass


def recv(conn: Conn, length: int) -> bytes:
    pass


def close(conn: Conn):
    pass
