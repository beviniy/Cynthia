#-*- coding:utf-8 -*-

"""
@created on 2017-06-13 下午12:07
@auther:Ziv Xiao
@description: None
"""

from wrappers import Response, Request

class BaseHandler(object):

    def __init__(self):
        pass

    def GET(self, request):
        raise NotImplementedError, 'This method must be implemented in the child class'

    def POST(self, request):
        raise NotImplementedError, 'This method must be implemented in the child class'


class Handler404(BaseHandler):

    def GET(self, request):
        return Response('404 not found')