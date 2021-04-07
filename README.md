# QtTimer_utils
Few utility functions for QtCore.QTimer to use a timer in finite manner. The example is ment to run as FreeCAD macro as I developed it while faceing problem in there.

These utility functions are usable in any Qt environment, though. QTimer naturally works infinitely, although you can stop it. But what if I don't know when the stop should happen? It should stop when sertain condition appears. In my case - when generator runs out of items. And I don't want full OOP approach with QtObject. I want timer and I want to be able to make use of the fact that it is stopped. Somehow and some time in the future. And when it stops, I want to be able to start it again with different task. And these 3 functions - stopTimer(), makeTimerCallback() and setTimer() provide this ability. 
