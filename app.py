#-*- coding:utf-8 -*-

"""
@created on 2017-06-13 下午7:39
@auther:Ziv Xiao
@description: None
"""
from wrappers import Response, Request

class App(object):

    def __init__(self, router):
        self.router = router

    def dispatch(self, request):
        handler = self.router.dispatch(request.full_path)
        return getattr(handler, request.method)(request)

    def __call__(self, environ, start_response):
        request = Request(environ)
        response = self.dispatch(request)
        return response(environ, start_response)