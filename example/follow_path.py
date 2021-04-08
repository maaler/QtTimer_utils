# timerutils.py should be in same folder (your macro dir) with this file
from timerutils import *
import time

# Basically copy/paste code from video: https://www.youtube.com/watch?v=BweWUANsZOY
# with minor naming changes and turning the function into generator
def followPath(follower_name, path_name):

    obj   = App.ActiveDocument.getObject(follower_name)
    shape = App.ActiveDocument.getObject(path_name).Shape
    edge  = App.ActiveDocument.getObject(path_name).Shape.Edge1
    
    pathLength = shape.Length
    
    for i in range(int(pathLength)):
        
        uv = edge.getParameterByLength(i)
        vec = edge.valueAt(uv)
        obj.Placement.Base = vec
        
        FreeCADGui.ActiveDocument.update()
        FreeCADGui.ActiveDocument.Sphere.show()
        yield(i)


def fetchPath():

    paths = ["BezCurve", "BezCurve001",  "BezCurve002", "BezCurve003", ]
    for p in paths:
        yield p


def myTest():
    
    def monitor():
        
        while timer.isActive():
            yield True
        
        p = next(nextPath, None)

        if p != None:
            timer.timeout.disconnect() 
            cb = makeTimerCallback(timer, followPath("Sphere", p))
            timer.timeout.connect(cb)
            timer.timeout.connect(lambda: makeTimerCallback(timer, next(monitor(), None)))
            timer.start()
            
            yield timer
        
        else:
            timer.timeout.disconnect()
    
    nextPath = fetchPath()
    timer = setTimer(50, followPath("Sphere", next(nextPath)))
    # connect timeout to callback that stops timer 
    # (and also disconnects, but only this very same callback) 
    # when followPath() runs out

    timer.timeout.connect(lambda: next(monitor()))
    # keep an eye on timer's state and if stopped then fetch next path and start it again
    # There are 2 callbacks connected to timer.timeout now

    return timer


def testWithTimeDotSleep():
    
    # it fails to perform as expected...
    for path in fetchPath():
        followPath("Sphere", path)
        FreeCADGui.ActiveDocument.update()
        FreeCADGui.ActiveDocument.Sphere.show()
        print(path)
        time.sleep(.1) # Blocks the whole thing. Nothing happens. 

if __name__ == "__main__":
    
    #testWithTimeDotSleep()
    timer = myTest()


