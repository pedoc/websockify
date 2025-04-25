import websockify
import sys

if sys.platform != "win32":
    import resource

if __name__ == '__main__':
    websockify.websocketproxy.websockify_init()
