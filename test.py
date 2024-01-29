from xpell import _x,_xlog,_xem,GenericModule,Wormholes,WormholeEvents
# from XLogger import _xlog, _XLogger
# from Xpell import _x
# from XModule import GenericModule
# from XEventManager import _xem
# from Wormhole import Wormholes, WormholeEvents  
import asyncio

print("Xpell test")

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
   


def on_wormhole_open(data):
    print("Wormhole is open")
    get_environment_name_message = {
        "_module": "xenvironment",
        "_op": "get-name"
    }

    res = Wormholes.send_sync(get_environment_name_message)
    print(res)

def main():
    print("starting")

    wormhole_url = "ws://127.0.0.1:3030/"


    Wormholes.on_open = lambda: on_wormhole_open()

    Wormholes.open(wormhole_url)

if __name__ == "__main__":
    try:
        main()
        print("done")
    except Exception as err:
        print(err)
        