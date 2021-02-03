#!/usr/bin/env python3
import logging
import sys
from multiprocessing import freeze_support
from runMultiple import callAsProcesses

logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)

def myFunc( n, m ):
   # do some dumb operations to take up CPU cycles
   for i in range( 10000000 ):
      j = i / 1.2
   print( "I'm a printer, I print number {} and {}".format( n, m ) )

if __name__ == '__main__':

   # Windows requires extra config to multiprocessing to prevent starting process
   # n+1 before process n has properly spawned. This line is optional if running
   # on linux.
   freeze_support()

   myInputs = [
      { "args": ( 1, 2 ), },
      { "args": ( 1, 4 ), },
      { "args": ( 4, 2 ), },
      { "args": ( 8, 2 ), },
   ]

   callAsProcesses( myFunc, myInputs )
