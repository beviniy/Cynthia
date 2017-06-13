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

    def handle(self, request):
        raise NotImplementedError, 'This method must be implemented in the child class'


class Handler404(BaseHandler):

    def handle(self, request):
        return Response('404 not found')