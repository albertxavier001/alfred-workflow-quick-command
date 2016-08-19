#!/usr/bin/python
# encoding: utf-8



import sys
import subprocess as sub
from workflow import Workflow
import argparse




def main(wf):
    # The Workflow instance will be passed to the function
    # you call from `Workflow.run`. Not so useful, as
    # the `wf` object created in `if __name__ ...` below is global.
    #
    # Your imports go here if you want to catch import errors (not a bad idea)
    # or if the modules/packages are in a directory added via `Workflow(libraries=...)`
    
    # import somemodule
    # import anothermodule
    
    # parse cmd arg
    parser = argparse.ArgumentParser()
    parser.add_argument('--query', dest='query', default="")
    args = wf.args
    cmd_args = parser.parse_args(args)
    wf.logger.debug("cmd_args:{}".format(cmd_args))

    # Do stuff here ...
    #wf.add_item(u'ON', u'Turn on shadowsocks in terminal', arg=cmd_args.query, valid=True)
    #wf.send_feedback()
    
    
    


if __name__ == '__main__':
    # Create a global `Workflow` object
    wf = Workflow()
    # Call your entry function via `Workflow.run()` to enable its helper
    # functions, like exception catching, ARGV normalization, magic
    # arguments etc.
    sys.exit(wf.run(main))