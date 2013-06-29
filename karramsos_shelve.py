#! /usr/bin/python
# About this snippet: Example on using the shelve module
# Author: Sukhvinder Singh | karramsos@gmail.com | @karramsos

import shelve

def addCust(database):
    customer = {}
    
    print "Add a new customer to the databse\n"
    
    custNum = raw_input('Enter a customer number: ')
    customer['firstName'] = raw_input('Customer First Name: ')
    customer['lastName'] = raw_input('Customer Last Name: ')
    customer['streetAdd'] = raw_input('Customer Street Address: ')
    customer['city'] = raw_input('Customer City: ')
    customer['state'] = raw_input('Customer State: ')
    customer['zip'] = raw_input('Customer Zip Code: ')
    
    database[custNum] = customer
    return

def main():
    database = shelve.open('customer.dat', writeback=True)
    
    addCust(database)
    
    lookForCust = 1
    
    while (lookForCust != '0'):
        lookForCust = raw_input('Enter Customer Number (0 to Exit)')
        
        if lookForCust =='0':
            break
        else:
            try:
                for i in database[lookForCust]:
                    print i, ' ', database[lookForCust][i]
                
            except KeyError:
                print "Customer not in database"
                break
            else:
                print '\n'
    
    database.close()
    
if __name__ == '__main__': main()
                
                
                