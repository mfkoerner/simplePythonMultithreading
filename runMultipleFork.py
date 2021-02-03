import os 
import sys
import logging
  
def callAsProcesses( func, kwargsList ):
   """
   Calls function in separate forked processes for each dict in kwargsList

   INPUTS:
   func           function to call multiple times
   kwargsList     list of dictionaries structured as keyword arguments
                  kwargsList[ "args" ] contains positional arguments
   
   EXAMPLE:
      func = myFunc
      kwargsList = [
         {
            "args": [ 1, 2 ],
            "bar": 7,
         },
         {
            "args": [ 4, 3 ],
            "bar": 9,
            "baz": True,
         },
      ]

      This will cause myFunc to be called twice as follows
       - myFunc( 1, 2, bar=7 )
       - myFunc( 4, 3, bar=9, baz=True )
   """

   # Safety assumptions
   assert len( kwargsList ) < 20      # Confirm reasonable number of processes
   hasArgsList = [ "args" in i for i in kwargsList ]
   assert all( hasArgsList ) == any( hasArgsList )    # no mixing "args" presence

   allChildren = set()
   childPid = 0

   for kwargs in kwargsList.copy():
      args = kwargs.pop( "args", [] )
      childPid = os.fork()

      if childPid > 0:
         # childPid > 0 means we are the parent
         # store PID to wait later and move on to next case
         allChildren.add( childPid )

      elif not childPid:
         # childPid of 0 means we are the child process
         # call function and exit loop
         func( *args, **kwargs )
         break

      else:
         # we should never get here, something went wrong with fork
         logging.error( "unexpected childPid=%d", childPid )
         sys.exit( 1 )

   if childPid: # only run in parent
      # Wait for all children to finish
      for pid in allChildren:
         logging.debug( "waiting for PID %d", pid )
         os.waitpid( pid, 0 )
         logging.debug( "PID %d finished", pid )
