# -*- coding: utf-8 -*-
"""
Created on Sat Apr 21 03:39:25 2018

@author: Arjun Nath
"""

from name_derived_class import FullName


def main() :
    
    print("---------------------------------------------")
    print("Assignment 1 for Intel Advanced Python Class")
    print("---------------------------------------------")
    print()
    nameobj1 = FullName("Arjun", "Rohan", "Nath")
    
    print("First name is " + nameobj1.get_firstname())
    print("Last name is " + nameobj1.get_lastname())
    
    strfname, err = nameobj1.get_full_name()
    print("Full name is " + strfname )
    
    strfname, err = nameobj1.get_capitalized_name()
    print("Capitalized name is " + strfname)
    
    strinitials = nameobj1.get_initials()
    print("Initials are " + strinitials)

    print("---------------------------------------------")
    
    nameobj2 = FullName("Vlad", "Tepes")

    print("First name is " + nameobj1.get_firstname())
    print("Last name is " + nameobj1.get_lastname())
    
    strfname, err = nameobj2.get_full_name()
    print("Full name is " + strfname )
    
    strfname, err = nameobj2.get_capitalized_name()
    print("Capitalized name is " + strfname)
    
    strinitials = nameobj2.get_initials()
    print("Initials are " + strinitials)

    print("---------------------------------------------")
    tuplefname = FullName.split_full_name("Charles Darwin")
    print("Split Full Name = ", tuplefname)
    


if __name__ == '__main__':
    main()


