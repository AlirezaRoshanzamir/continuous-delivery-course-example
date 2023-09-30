import socket


def resolve_or_default(hostname: str, default: str = "localhost") -> str:
    try:
        socket.gethostbyname(hostname)
        return hostname
    except socket.error:
        return default
