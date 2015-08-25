__author__ = 'techbk'

import asyncio
from aiohttp import web
from runprocess import run_process
from runshell import runshell

class Url_handler:
    def __init__( self,loop ):
        self._loop = loop
        self._task = {}
        self._taskid = 0

    def __setid(self):
        self._taskid = self._taskid + 1
        return str( self._taskid )

    @asyncio.coroutine
    def doblastn( self,request ):
        cmd = ( u"blastdbcmd -db db/refseq_rna.00 -entry nm_000122 -out test_query.fa"
        "&& blastn -query test_query.fa -db db/refseq_rna.00 -task blastn -dust no -outfmt "
        "'7 qseqid sseqid evalue bitscore' -max_target_seqs 2" )
        task_run_process = asyncio.async( runshell( cmd ) )
        #task_run_process.add_done_callback( got_result )
        id = self.__setid()
        text = "Do Start App: http://localhost:8080/checkresult/" + id
        self._task[id] = task_run_process

        return web.Response( body = text.encode( 'utf-8' ) )

    @asyncio.coroutine
    def do_start_app1( self,request ):
        task_run_process = asyncio.async( run_process( 10 ) )
        #task_run_process.add_done_callback( got_result )
        self._taskid = self._taskid + 1
        id = str( self._taskid )
        text = "Do Start App: http://localhost:8080/checkresult/" + id
        self._task[id] = task_run_process

        return web.Response( body = text.encode( 'utf-8' ) )



    @asyncio.coroutine
    def check_result( self,request ):
        id = request.match_info.get( 'id' )
        if id:
            task_run_process = self._task.get(id,False)
            #assert isinstance( task_run_process,asyncio.Task )
            if task_run_process:
                if task_run_process.done():
                    print(task_run_process.done())
                    result = yield from task_run_process
                    print( result )
                    text = "App " + id + " done!"
                    if result[1]:
                        text += "\nError: " + result[1].decode('ascii')
                        #return web.Response( body = text.encode( 'utf-8' ) )
                    if result[0]:
                        text += "\nOutput: \n" + result[0].decode('ascii')


                    # return web.Response(body=result)

                    return web.Response( body = text.encode( 'utf-8' ) )
                else:
                    text = "App Not Done"
                    return web.Response( body = text.encode( 'utf-8' ) )

            else:
                text = "App ko ton tai"
                return web.Response( body = text.encode( 'utf-8' ) )
        else:
            text = "Link cua ban ko ton tai"
            return web.Response( body = text.encode( 'utf-8' ) )