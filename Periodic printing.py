from threading import Timer

def printit():
  Timer(5.0, printit).start()
  print("Hello, World!")

printit()