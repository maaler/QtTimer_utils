# QtTimer_utils
Few utility functions for QtCore.QTimer to use a timer in finite manner. The example is ment to run as FreeCAD macro as I developed it while faceing problem in there. Put timerutils.py file into your FreeCAD's macro dir.

These utility functions should be usable in any Qt environment, though. QTimer naturally works infinitely, although you can stop it. But what if I don't know when the stop should happen? It should stop when certain condition appears. In my case - when generator runs out of items. But I don't know how long it takes. And I don't want full OOP approach with QtObject. I want timer and I want to be able to make use of the fact that it is stopped. Somehow and some time in the future. And when it stops, I want to be able to start it again with different task. And these 3 functions - stopTimer(), makeTimerCallback() and setTimer() provide this ability.

Look into example folder to see how data from one generator is fetched to keep timer going from path to path.
