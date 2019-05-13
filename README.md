# Roger-skyline-1 [![42](https://i.imgur.com/9NXfcit.jpg)](i.imgur.com/9NXfcit.jpg)

Virtual machine and web server deployment automation [a 42 project].

---

## Description

- Directory contents:

```
README.md        config           info             iso              roger_skyline.py src              web

./config:
config_cron.sh             config_grub.sh             config_ssh.sh
config_denialofservices.sh config_network.sh          update
config_firewall.sh         config_ports.sh            watch_crontab

./iso:
build_iso.sh     isolinux.cfg     preseed-mini.iso preseed.cfg

./src:
__init__.py   createvm.py   delete.py     install_os.py loadscript.py parser.py     secure.py     shutdown.py   start.py

./web:
deploy_apache.sh www

./web/www:
index.html
```

---


## Script

_Script files description_

| [name].py | Description |
| --- | --- |
| **start.py** | Runs the vm once installed with the os.|
| **start.py** | Runs the vm once installed with the os.|

---

## Ports

Port were modified:

| Port | Service |
| --- | --- |
| `2266` | ssh |

---

## Using this Script

- Make sure you have an ethernet network insterface + Make sure you have access to the world wide web +  Install Python3.5 and VirtualBox on your machine.

- Copy of the repository:

```shell=
git clone https://github.com/Ant0wan/Roger-skyline-1.git && cd libft
```

- Modify the 'info' file with your appropriate setting.

- Launch :

```shell=
./roger-skyline-1 [arg]
```
