from PySide import QtCore

"""
    Disclaimer: No error checking is made. For example stopTimer()'s first
    parameter should be QtCore.QTimer and second either None or callable.
    If your generator yields naturally to callable objects then obviously 
    makeTimerCallback()'s strategy fails.
"""

def stopTimer(timer, onTimeout = None):
    
    if onTimeout == None:
        timer.timeout.disconnect()
    else:
        timer.timeout.disconnect(onTimeout)
    
    timer.stop()


def makeTimerCallback(timer, generator):

    cb = lambda: next(generator, lambda: stopTimer(timer, onTimeout))
    onTimeout = lambda: callable(cb()) and cb()()
    # This wierd line above does:
    # Generators are not callable, but if they run out, function next() returns 
    # whatever the second argument is. But stopTimer() has to be inside lambda,
    # because the expression is evaluated - next() is a function not a language
    # construct. And callable() is function, too. Luckily we can call next()
    # on stopped generators as many times we want, but it still will return the
    # second argument. So, if calling cb() returns generator, right side of 
    # operator 'and' never executes. Language rule. But if it returns callable
    # thing, right side calls (indirectly, through cb()) next() again and also
    # executes returned function, whose body is stopTimer()
    
    return onTimeout


def setTimer(timeout, generator):
    
    timer = QtCore.QTimer()
    timer.setInterval(timeout)

    onTimeout = makeTimerCallback(timer, generator)
    # Create the callback function that stops the timer when generator runs out

    timer.timeout.connect(onTimeout)
    timer.start()
    
    return timer
