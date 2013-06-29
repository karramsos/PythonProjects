#! /usr/bin/python
# About this snippet: AN SQLite database 
# Author: Sukhvinder Singh | karramsos@gmail.com | @karramsos

import sqlite3

# Create a version of the database in RAM, this could also be a filename ending with .db
createDb = sqlite3.connect(':memory:')

#Creates the SQLite cursor that is used to query the database
queryCurs = createDb.cursor()

def createTable():
    # Calls the execute method that will submit a create table SQL Query
    # id will auto increment and doesn't require values to be entered
    queryCurs.execute(''' create table customers
    (id integer primary key, name text, street text, city text, state text, balance real)''')
    
def addCust(name, street, city, state, balance):
    # Calls the execute method that will submit a insert SQL Query
    queryCurs.execute('''insert into customers (name, street, city, state, balance)
    values (?,?,?,?,?)''', (name,street, city, state, balance))

def main():
    # Call the method createTable, that will create the table in the database
    createTable()
    
    # Add customers to the database
    addCust('Sukhvinder Singh', '8754 Upward Street', 'Venus', 'CA', 150.76)
    addCust('Monthy Python', '8750 Upward Street', 'Venus', 'CA', 350.60)
    addCust('Guido Rossum', '8769 Upward Street', 'Venus', 'CA', 0.00)
    addCust('Django Flask', '8787 Upward Street', 'Venus', 'CA', 50.90)
    
    # Force the database to make changes with the commit command
    createDb.commit()
    
    # Cycles through the tuple and prints the entries to screen
    for i in queryCurs:
        print'\n'
        for j in i:
            print j
    
    # Print customers ordered by lowest balance and with titles
    queryCurs.execute('select * from customers order by balance')
    
    # Creates a list that contains the titles for my database data
    listTitle = ['Id Num: ','Name: ', 'Street: ', 'City: ', 'State: ', 'Balance: ']
    k = 0
    
    # Cycles through the tuple and prints the entries to screen
    for i in queryCurs:
        print '\n'
        for j in i:
            print listTitle[k],
            print j
            if k < 5: k += 1
            else: k = 0
    
    # Closes the database
    queryCurs.close()

if __name__ == '__main__': main()