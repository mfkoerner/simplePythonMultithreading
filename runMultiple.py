from multiprocessing import Process
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

   allProcesses = set()

   for kwargs in kwargsList.copy():
      args = kwargs.pop( "args", [] )
      p = Process( target=func, args=args, kwargs=kwargs )
      p.start()
      allProcesses.add( p )

   # Wait for all children to finish
   for process in allProcesses:
      logging.debug( "waiting for PID %d", process.pid )
      process.join()
      logging.debug( "PID %d finished", process.pid )
      if process.exitcode:
         logging.error( "PID %d exited with bad exitcode %d",
                        process.pid, process.exitcode )
