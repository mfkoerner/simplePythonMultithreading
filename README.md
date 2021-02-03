# simplePythonMultithreading
Some quick examples of multithreading in python

run testRunMultiple.py to make sure that everything is working on your system.

You should get an output that looks something like this:
```
$ ./testRunMultiple.py
DEBUG:root:waiting for PID 270
I'm a printer, I print number 1 and 2                                     
I'm a printer, I print number 8 and 2
DEBUG:root:PID 270 finished
DEBUG:root:waiting for PID 267
DEBUG:root:PID 267 finished
DEBUG:root:waiting for PID 269
I'm a printer, I print number 1 and 4
I'm a printer, I print number 4 and 2
DEBUG:root:PID 269 finished
DEBUG:root:waiting for PID 268
DEBUG:root:PID 268 finished
```

And the output should be in a slightly different order each time you run the test. This is natural


I'd recommend basing any parallel code you write off of the example in runMultiple.py NOT the fork() example.
