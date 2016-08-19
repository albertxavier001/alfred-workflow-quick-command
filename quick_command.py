#!/usr/bin/python
# encoding: utf-8

import sys
import subprocess as sub
from workflow import Workflow
import argparse
import json

def parse_args(args_):
    parser = argparse.ArgumentParser()
    parser.add_argument('--query', dest='query', default="")
    parser.add_argument('--command', dest='command', default="")
    parser.add_argument('--output', dest='output', action="store_true", default=False)
    parser.add_argument('--input', dest='input', action="store_true", default=False)
    parser.add_argument('--direct_run', dest='direct_run', action="store_true", default=False)
    parser.add_argument('--add_command', dest='add_command', action="store_true", default=False)
    parser.add_argument('--del_command', dest='del_command', action="store_true", default=False)
    parser.add_argument('--input_add_command', dest='input_add_command', action="store_true", default=False)
    parser.add_argument('--input_del_command', dest='input_del_command', action="store_true", default=False)
    parser.add_argument('--input_direct_run', dest='input_direct_run', action="store_true", default=False)
    args = parser.parse_args(args_)
    # wf.logger.debug("args:{}".format(args))
    return args

def load_command_table():
    with open(".command_table.json", "r") as f:
        data = json.load(f)
    return data

def save_command_table(data):
    with open(".command_table.json", "w") as f:
        json.dump(data, f, indent=4)

def add_new_command(query, data):
    (key, command, description) = query.split(",")
    data[key] = { "command": command, "desc": description}
    save_command_table(data)

def del_some_command(key, data):
    del data[key]
    save_command_table(data)

def add_items(data, query="", pass_key=False):
    
    # shadowsocks
    # if (u"ss on").find(query) >= 0 or query == u"":
    #     command = "export http_proxy=socks5://127.0.0.1:1080 && export http_proxys=socks5://127.0.0.1:1080 && source ~/.bash_profile"
    #     wf.add_item(u"Turn on shadowsocks", u"Copy to clipboard", arg=command, valid=True)
    
    for key in data:
        val = data[key]
        # wf.logger.debug("\n>>>val:{}".format(val))
        # wf.logger.debug(">>>ind:{}".format((key).find(query)))
        # wf.logger.debug(">>>key:{}".format(key))
        # wf.logger.debug(">>>query:{}".format(query))
        if (key).find(query) >= 0 or query == u"":
            if pass_key == False:
                wf.add_item(val[u"desc"], key, arg=val[u"command"], valid=True)
            else:
                wf.add_item(val[u"desc"], key, arg=key, valid=True)

    wf.send_feedback()



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
    args = parse_args(wf.args)

    # Do stuff here ...
    #wf.add_item(u'ON', u'Turn on shadowsocks in terminal', arg=args.query, valid=True)
    #wf.send_feedback()
    # wf.logger.debug("")

    # load data
    data = load_command_table()
    # save_command_table(data)
    # wf.logger.debug("data:{}".format(data))

    # generate command
    if args.input == True or args.input_direct_run == True:
        add_items(data, args.query)

    # output command
    if args.output == True:
        wf.logger.debug(">>> args.command = {}".format(args.command))
        sys.stdout.write(args.command)
        sys.stdout.flush()

    # generate new command
    if args.input_add_command == True:
        wf.logger.debug(">>> args.query = {}".format(args.query))
        wf.add_item(u'Add new command', u'Type "key,command,description"', arg=args.query, valid=True)
        wf.send_feedback()

    #  execute add new command
    if args.add_command == True:
        add_new_command(args.query, data)
        sys.stdout.write("Add new command successfully")
        sys.stdout.flush()

    # find out which command should be delete
    if args.input_del_command == True:
        add_items(data, args.query, pass_key=True)

    #  execute del some command
    if args.del_command == True:
        del_some_command(args.query, data)
        sys.stdout.write("Delete command successfully")
        sys.stdout.flush()

    # direct run command
    if args.direct_run == True:
        script = """ osascript -e 'tell application "Terminal" to do script "{}"' """.format(args.query)
        wf.logger.debug(">>> script = "+script)
        return_code = sub.call(script, shell=True) 
        if return_code == 0:
            sys.stdout.write("Run command successfully")
            sys.stdout.flush() 
        else:
            sys.stdout.write("Run command failed, return code = {}".format(return_code))
            sys.stdout.flush() 

if __name__ == '__main__':
    # Create a global `Workflow` object
    wf = Workflow()
    # Call your entry function via `Workflow.run()` to enable its helper
    # functions, like exception catching, ARGV normalization, magic
    # arguments etc.
    sys.exit(wf.run(main))