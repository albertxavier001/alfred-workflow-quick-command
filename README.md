# alfred-workflow-quick-command
Quickly generate, delete, copy, execute any command




## Usage

### Copy command

Type ```qccopy``` to select any command you need, then the command is copied to clipboard

### Run command directly

Type ```qcrun``` to select any command, then run in terminal

### Add new command
Type ```qcadd``` to add new command in format ```key,command,description```

### Delete some command
Type ```qcdel``` to select and delete some command

### Mannualy modify command
open ```.command_table.json``` to modify any command

#### Command table example

```
{
    "ss on": {
        "command": "export http_proxy=socks5://127.0.0.1:1080 && export http_proxys=socks5://127.0.0.1:1080 && source ~/.bash_profile", 
        "desc": "Turn on shadowsocks json"
    }
}
```

key = "ss on"
command = "export http_proxy=socks5://127.0.0.1:1080 && export http_proxys=socks5://127.0.0.1:1080 && source ~/.bash_profile"
description = "Turn on shadowsocks json"

