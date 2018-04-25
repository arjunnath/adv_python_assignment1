# -*- coding: utf-8 -*-
"""
Created on Sat Apr 21 03:37:01 2018

@author: Arjun Nath
"""
import sys
import os


class Name(object):
    '''
    A Simple class to hold names
    '''
  
    def __init__(self, firstname ="", lastname = "", middlename = None ):
        '''
        class constructor
        '''
        self.firstname = firstname
        self.middlename = middlename
        self.lastname = lastname

    @classmethod
    def isName(self):
        if self.firstname == "" or self.lastname == "" :
            return False
        else :
            return True
