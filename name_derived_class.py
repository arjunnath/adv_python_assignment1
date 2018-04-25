# -*- coding: utf-8 -*-
"""
Created on Sat Apr 21 03:37:38 2018

@author: Arjun Nath
"""

import sys
from name_base_class import Name

class FullName(Name) :
    '''
    Class FullName inherits from class Name.
    It adds several new methods to the existing methods from Name
    '''
    
    def __init__(self, fname ="", mname = "", lname = "", title = None):
        '''
        Initalizer - if lastname is empty ,then midddlname is lastname
        Empty first name is not allowed
        '''
        if fname == "" :
            raise Exception("First Name cannot be empty")
        elif lname == "" and mname != "":
            lname = mname
            mname = ""
            super().__init__(fname, lname)
        else :
            super().__init__(fname, mname, lname)
        self.title = title

    def set_title(self, strtitle):
        self.title = strtitle

    def get_full_name(self):
        '''
        :return full name as First Name, Mid Name, Last Name
        '''
        exception_message = None
        try:
            if self.middlename is not None :
                names = (self.firstname, self.middlename, self.lastname)
            else :
                names = (self.firstname, self.lastname)
            full_name = self.STR_SPACE.join(names)
        except:
            exception_message = sys.exc_info()[0]
        return full_name, exception_message

    def get_capitalized_name(self):
        '''
        :return capitalized full name
        '''
        exception_message = None
        try:
            full_name, err = self.get_full_name()
        except:
            exception_message = sys.exc_info()[0]        
        return full_name.upper() , exception_message

    def get_initials(self) :
        '''
        :return capitalized initials
        '''
        full_name, err = self.get_full_name()
        names = full_name.split(" ")
        initials = ""
        for n in names :
            initials += n[0].upper() + self.STR_DOT
        return initials
    
    @staticmethod
    def split_full_name(str_full_name) :
        '''
        :return tuple of names out of full name
        '''
        names = str_full_name.split(" ")
        length = len(names)
        if length == 3 :    
            fname, midname, lname = names
            return (fname, midname, lname)
        if length == 2 :
            fname, lname = names
            return (fname, lname)
        