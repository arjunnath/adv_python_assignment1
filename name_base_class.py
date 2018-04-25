# -*- coding: utf-8 -*-
"""
Created on Sat Apr 21 03:37:01 2018

@author: Arjun Nath
"""
import sys
import os


class Name(object):
    '''
    A class to hold names with some basic class methods
    '''
    STR_SPACE = " "
    STR_DOT = "."
    
    # def __init__(self, firstname ="", middlename = None, lastname = ""  ):
    def __init__(self, *args, **kwargs):
        '''
        class constructor - Initialize name variables
        Constructor can take 2 or 3 string names
        '''
        if len(args) == 2 :
            self.firstname = args[0]
            self.middlename = None
            self.lastname = args[1]
            #print("Base class init. Names are :" + self.firstname + " " + self.lastname )
        if len(args) == 3 :
            self.firstname = args[0]
            self.middlename = args[1]
            self.lastname = args[2]
            #print("Base class init. Names are :" + self.firstname + " " + self.middlename + " " + self.lastname )


    def get_firstname(self):
        return self.firstname

    def get_middlename(self):
        return self.middlename

    def get_lastname(self):
        return self.lastname

    def set_firstname(self, fname):
        self.firstname = fname

    def set_middlename(self, mname):
        self.middlename = mname

    def set_lastname(self, lname):
        self.lastname = lname


    @classmethod
    def isName(self):
        ''' 
        Every name should have at least one first and one last name
        '''
        try :
            if self.firstname == "" or self.lastname == "" :
                return False
            else :
                return True
        except :
            print("Exception in isName()")
    
