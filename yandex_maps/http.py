#coding: utf-8
from __future__ import with_statement
from contextlib import closing
import httplib

# urllib2 doesn't support timeouts for python 2.5

def request(method, url, data=None, headers={}, timeout=None):
    host_port = url.split('/')[2]
    timeout_set = False
    try:
        connection = httplib.HTTPConnection(host_port, timeout = timeout)
        timeout_set = True
    except TypeError:
        connection = httplib.HTTPConnection(host_port)

    with closing(connection):
        if not timeout_set:
            connection.connect()
            connection.sock.settimeout(timeout)
            timeout_set = True

        connection.request(method, url, data, headers)
        response = connection.getresponse()
        return (response.status, response.read())
