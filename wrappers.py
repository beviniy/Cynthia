#-*- coding:utf-8 -*-

"""
@created on 2017-06-13 上午10:03
@auther:Ziv Xiao
@description: None
"""


from werkzeug.wrappers import Response as BaseResponse, Request as BaseRequest


class Response(BaseResponse):
    pass


class Request(BaseRequest):
    pass

