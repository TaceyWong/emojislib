# -*- coding: utf-8 -*-

import argparse
from emojislib import *


def main():
    def get(**kw):
        result = list()
        for k,v in kw.items():
            if not v:
                continue

            item = globals()["by_"+k](v)
            if item:
                if isinstance(item,list):
                    result.extend(item)
                else:
                    result.append(item)
        result = "  ".join(map(lambda x:str(x), list(set(result))))
        if result:
            print(result)
        else:
            print(str(by_name("crying_cat_face"))," Not Found")

    def search(**kw):
        result = list()        
        for k,v in kw.items():
            if not v:
                continue
            item = globals()["search_by_"+k](v)
            if item:
                result.extend(item)
        result = "  ".join(map(lambda x:str(x), list(result)))
        if result:
            print(result)
        else:
            print(str(by_name("crying_cat_face"))," Not Found")
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(dest='subparser')
    parser_get = subparsers.add_parser('get')
    parser_get.add_argument(
        '-n', '--name', dest='name', help='get emoji by name')
    parser_get.add_argument(
        '-k', '--key', dest='key', help='get emoji by key')
    parser_get.add_argument(
        '-c', '--cate', dest='cate', help='get emoji by category')
    
    parser_search = subparsers.add_parser('search')
    parser_search.add_argument(
        '-n', '--name', dest='name',  help='search emoji by name')
    parser_search.add_argument(
        '-k', '--key', dest='key', help='search emoji by key')
    parser_search.add_argument(
        '-c', '--cate', dest='cate', help='search emoji by category')

    kwargs = vars(parser.parse_args())
    if kwargs.get('word','').strip() in ('get','search'):
        pass
    
    locals()[kwargs.pop('subparser')](**kwargs)


if __name__  == "__main__":
    main()
    

