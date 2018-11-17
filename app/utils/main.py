from flask import request


def helloWorld():
    return 'Hello World!'


def checkWho():
    response = {}

    # TODO: Check if behind proxy
    response['ip'] = request.remote_addr
    response['language'] = request.headers['accept-language']
    response['software'] = request.headers['user-agent']

    return response
