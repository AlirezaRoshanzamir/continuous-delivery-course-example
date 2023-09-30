import logging
import sys

from gevent.pywsgi import WSGIServer

from fitzy.portal.app import app

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
logger.addHandler(logging.StreamHandler(sys.stdout))

if __name__ == "__main__":
    http_server = WSGIServer(("0.0.0.0", 6792), app, log=logger)
    http_server.serve_forever()
