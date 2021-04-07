Place follow_path.py file to your FreeCAD's macro dir and execute it as macro. It is meant to run with follow_path.FCStd project.
Also place timerutils.py file in your macro dir. Yes, macro may, but must not have .FCMacro extension. 

The example project - follow_path.FCStd - is based on YouTube video https://www.youtube.com/watch?v=BweWUANsZOY 
But the whole thing in this repo is because his code uses blocking time.sleep() function and as such at least in my computer
the code didn't do anything. Well, it sleeped. But no action in GUI. With QTimer I got it running.
