#!/usr/bin/python
# -*- coding: UTF-8 -*-
 
import sys
import argparse
 
def createParser ():
    '''
    Функция передает параметры командной строки, в программу
    '''
    parser = argparse.ArgumentParser()
    #Передаем параметр города и ссылку
    parser.add_argument ('-c', nargs='+')
    #Передаем параметр месяца
    parser.add_argument ('-m', nargs='+')
    #Передаем параметр даты
    parser.add_argument ('-d', nargs='+')
    return parser
 
 
if __name__ == '__main__':
    parser = createParser()
    namespace = parser.parse_args(sys.argv[1:])
 
    print (namespace)
 
    for city in namespace.c:
        for date in namespace.d:
            print ("Город, {}!".format (city) )
            print ("Дата, {}!".format (date) )
