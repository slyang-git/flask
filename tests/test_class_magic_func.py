# -*- coding: utf-8 -*-

"""
Created by yangshuanglong@wecash.net on 2017/10/20
"""


class Dog(object):

    def __init__(self, name):
        self.name = name

    def __call__(self, *args, **kwargs):
        print('in __call__')

    def __enter__(self):
        print('in __enter__')

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('in __exit__')
        return False


class Duck(object):
    def __init__(self):
        print ('__init__')

dog = Dog('lucy')
dog()

#
# with Dog('lily') as d:
#     print ('hello')

duck = Duck()

setattr(duck, 'key', 'val77888ue')

print(duck.key)