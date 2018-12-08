"""
get/search methods
"""
from __future__ import absolute_import
from .emojis import Emojis



class TypeException(Exception):
    def __init__(self,expect,get_):
        super().__init__(self) 
        self.expect = expect
        self.get_ = get_
    def __str__(self):
        return "expect {},but get {}".format(self.expect,self.get_)

def __check_type(input_value,expect=str):
    if not isinstance(input_value,str):
        raise TypeException(expect,type(input_value))

def by_name(name):
    __check_type(name)
    return Emojis.get(name.lower())

def by_key(key):
    __check_type(key)
    emojis = filter(lambda v:key.lower() in v.keywords,Emojis.values())
    return list(emojis)

def by_cate(cate):
    __check_type(cate)
    emojis = filter(lambda v:cate.lower()==v.category,Emojis.values())
    return list(emojis)

def search_by_name(name):
    __check_type(name)
    return list(filter(lambda v:name.lower() in v.name,Emojis.values()))

def search_by_key(key):
    __check_type(key)
    emojis = list()
    key = key.lower()
    for v in Emojis.values():
        keys = v.keywords
        flag = False
        for i in keys:
            if key in i:
                flag = True
                break
        if flag:
            emojis.append(v)
    return emojis


def search_by_cate(cate):
    __check_type(cate)
    return list(filter(lambda v:cate.lower() in v.category,Emojis.values()))