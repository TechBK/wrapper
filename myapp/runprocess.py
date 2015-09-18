__author__ = 'techbk'
import asyncio

@asyncio.coroutine
def run_process( time ):

    assert isinstance( time,int )
    code = u'import time; print("Sleep {time:d}"); time.sleep({time:d})'.format( **{"time": time} )

    print(code)
    print( 'Chuong trinh OK' )
    print( datetime.datetime.now() )

    # Create the subprocess, redirect the standard output into a pipe
    create = asyncio.create_subprocess_exec( sys.executable,'-c',code,
                                             stdout = asyncio.subprocess.PIPE,stderr = asyncio.subprocess.PIPE )
    # Wait for create
    proc = yield from create  # proc is Process Instance

    out,err = yield from proc.communicate()

    return out,err