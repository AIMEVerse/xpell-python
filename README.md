# Xpell-Python - Real-Time Interpreter for Python


Xpell-Python is a real-time interpreter for Python application development, such application requires control on several modules  and AI engine.

Xpell enables real-time translation from any command (XCommand) to platform specific command.



The way to communicate with Xpell engine is to send XCommand that will be analyzed and activate the appropriate module:

```
  [XCommand]
     - module (the name of the module to run the command)
     - created (date/timestamp of the command)
     - object - optional - the object within the module to run the command
     - op (the operation (method/function) to run within the module)
     - params (list of parameters)
```





# Credits & License

 ---

 Author: Fridman Fridman <fridman.tamir@gmail.com>

 License:  GPL-3 

 First Release: 28/01/2024

 Copyright Aime Technologies 2024, all right reserved

 
 