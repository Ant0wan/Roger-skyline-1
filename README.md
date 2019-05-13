# Roger-skyline-1 [![42](https://i.imgur.com/9NXfcit.jpg)](i.imgur.com/9NXfcit.jpg)

Virtual machine and web server deployment automation [a 42 project].

---

## Description

Roger-skyline.py is a script that performs a virtual machine deployment using Virtual Box.

This little software can execute multiple tasks such as starting, connecting ssh, powering off, configuring or deleting the virtual machine which elements have been configured in `info` file.

Roger_skyline.py may take a unique argument:

```
./roger_skyline.py does not take more than 1 argument.
Usage: ./roger_skyline.py [option]
Options:
	start	starts the VM
	stop	poweroffs the VM
	ssh	connects to the VM using SSH
	delete	stops and deletes the VM with its disk
```

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


## Files description

- Script files

| [name].py | Description |
| --- | --- |
| **start.py** | Runs the vm once installed with the os.|
| **start.py** | Runs the vm once installed with the os.|

- Script files `./src/` + ./roger_skyline.py`

| [name].py | Description |
| --- | --- |
| **roger_skyline.py** | Main script. Can take argument for mgt.|
| **createvm.py** | Configure the vm .|
| **install_os.py** | Runs the vm once installed with the os.|
| **loadscript.py** | Runs the vm once installed with the os.|
| **parser.py** | Runs the vm once installed with the os.|
| **secure.py** | Runs the vm once installed with the os.|
| **shutdown.py** | Runs the vm once installed with the os.|
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
