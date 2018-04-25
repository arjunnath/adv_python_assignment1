# -*- coding: utf-8 -*-
"""
Created on Sat Apr 21 03:37:38 2018

@author: Arjun Nath
"""

from name_base_class import Name

class FullName(Name) :
    
    def __init__(self, firstname ="", lastname = "", middlename = "", title = None):
        super().__init__(firstname, lastname, middlename)
        self.title = title

    @classmethod 
    def get_firstname(self):
        return self.firstname

    @classmethod 
    def get_middlename(self):
        return self.middlename

    @classmethod
    def get_lastnamename(self):
        return self.lastname

    @classmethod 
    def set_firstname(self, fname):
        self.firstname = fname

    @classmethod 
    def set_middlename(self, mname):
        self.middlename = mname

    @classmethod
    def set_lastnamename(self, lname):
        self.lastname = lname

    def set_title(self, strtitle):
        self.title = strtitle

    def get_initials(self) :
        return "initials"
    
    def get_fullname(self) :
        if self.middlename != "" :
            return self.firstname + " " + self.middlename + " " + self.lastname
        else :
            return self.firstname + " " + self.lastname

