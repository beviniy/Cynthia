#-*- coding:utf-8 -*-

"""
@created on 2017-06-13 上午10:07
@auther:Ziv Xiao
@description: None
"""


from wrappers import Response, Request
from handler import BaseHandler
from router import Router
from app import App


class HelloHandler(BaseHandler):

    def handle(self, request):
        return Response('hello %s!' % request.args.get('name', 'world'))


if __name__ == '__main__':
    from werkzeug.serving import run_simple

    rounter = Router([('^/hello', HelloHandler())])

    myapp = App(rounter)

    run_simple('localhost', 4000, myapp, use_debugger=True, use_reloader=True)