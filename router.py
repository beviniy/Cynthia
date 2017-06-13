#-*- coding:utf-8 -*-

"""
@created on 2017-06-13 上午11:55
@auther:Ziv Xiao
@description: None
"""
import re
from handler import BaseHandler, Handler404

class Router(object):

    def __init__(self, router=None):
        self.router = router or []
        pass

    def dispatch(self, url):

        for pattern, target in self.router:
            if re.search(pattern, url):
                if isinstance(target, Router):
                    return target.dispatch(url[len(pattern.rstrip('/')):])
                elif isinstance(target, BaseHandler):
                    return target

        return Handler404()
