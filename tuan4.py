__author__ = 'techbk'

import asyncio
from aiohttp import web
from urlhandler import Url_handler


# import datetime
# import functools
# import sys

# def got_result( future ):
# print( future.result( ) )

@asyncio.coroutine
def index(request):
    return web.Response(body = b"Welcome")


@asyncio.coroutine
def init(loop):
    url_handler = Url_handler(loop)

    app = web.Application(loop = loop)

    app.router.add_route('GET', '/', index)

    app.router.add_route('GET', '/doblastn', url_handler.doblastn)
    app.router.add_route('GET', '/dostart_app1', url_handler.do_start_app1)
    app.router.add_route('GET', '/checkresult/{id}', url_handler.check_result)

    handler = app.make_handler()
    srv = yield from loop.create_server(handler, '0.0.0.0', 8080)
    print("Server started at http://0.0.0.0:8080")
    return srv, handler


loop = asyncio.get_event_loop()
srv, handler = loop.run_until_complete(init(loop))

try:
    loop.run_forever()
except KeyboardInterrupt:
    pass
