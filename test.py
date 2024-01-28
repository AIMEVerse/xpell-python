from Xpell import _x
from XModule import GenericModule
from XEventManager import _xem
import asyncio
# print("Xpell test")

_x.info()
_x.load_module(GenericModule)

# _x._fire_on_frame_event = True
# _xem.once("xpell-frame", lambda data: print(data))
# _xem.on("xpell-frame", lambda data: print(data))

_x.start()

GenericModule.create({
    "_type": "xobject",
    "_name": "test",
    "_children": [
        {
            "_type": "xobject",
            "_name": "test2"
        }
    ]
})






