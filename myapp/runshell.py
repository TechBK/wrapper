__author__ = 'techbk'

import asyncio

@asyncio.coroutine
def runshell(cmd):

    print('run shell', cmd )
    #print( 'Blastn' )
    #print( datetime.datetime.now() )

    # Create the subprocess, redirect the standard output into a pipe
    create = asyncio.create_subprocess_shell( cmd = cmd,
                                             stdout = asyncio.subprocess.PIPE,stderr = asyncio.subprocess.PIPE )
    # Wait for create
    proc = yield from create  # proc is Process Instance

    out,err = yield from proc.communicate()

    return out,err