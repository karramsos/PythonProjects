#!/usr/bin/env python

# Example of a simple multithreaded program that utilises the machanism from the thread module. 
# The two loops are executed concurrently (with the shorter one finishing first), and the total
# elapsed time is only as long as the slowest thread rather than the total time for each separately

import thread
from time import sleep, ctime

def loop0():
    print 'start loop 0 at:', ctime()
    sleep(4)
    print 'loop 0 done at:', ctime()

def loop1():
    print 'start loop 1 at:', ctime()
    sleep(2)
    print 'loop 1 dome at:', ctime()

def main():
    print 'starting at:', ctime()
    thread.start_new_thread(loop0, ())
    thread.start_new_thread(loop1, ())
    sleep(6)
    print 'all DONE at:', ctime()

if __name__ == '__main__':
    main()
