from xpell import _x, _xlog, _xem, GenericModule, Wormholes, WormholeEvents
import asyncio

print("Xpell test")

_x.info()
_x.load_module(GenericModule)

_x.start()


def on_wormhole_open(data):
    print("Wormhole is open")
    get_environment_name_message = {
        "_module": "xenvironment",
        "_op": "get-name"
    }

    res = Wormholes.send_sync(get_environment_name_message)
    print(res)

async def main():
    print("starting")

    wormhole_url = "ws://127.0.0.1:3030/"

    Wormholes.on_open = lambda: on_wormhole_open()

    loop = asyncio.get_event_loop()

    # Create a task for running the Wormholes WebSocket client
    task = loop.create_task(Wormholes.open(wormhole_url))

    try:
        # Wait for the task to complete
        await task
    except Exception as err:
        print("Test error :{\n", err)


if __name__ == "__main__":
    asyncio.run(main())
    # try:
    # except Exception as err:
    #     print("Test error :{\n", err)