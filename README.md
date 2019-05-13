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

- Info file

| [name] | Description |
| --- | --- |
| **info** | Text file parsed when executing roger_skyline.py. It contains all configuration settings.|

- Info file entries that can be modified

```
VM_name = RogerSkylineDebian
OS_type = Debian_64
cpu = 4
ram = 1024
disk_size = 8000
bridge = en0
iso_path = ./iso/preseed-mini.iso
disk_pathname = /tmp/rogerskylinedebian
disk_file_format = vdi
disk_type = hdd
ip_vm = 10.11.21.42 (modify preseeding if changed)
netmask = 255.255.255.252 (modify preseeding if changed)
user = antoine (modify preseeding if changed)
passwd = root (modifiy preseeding if changed)
ssh_port = 2266
dns_port = 53
secure = yes ( a 'no' will disable the web server deployment and all Roger-skyline-1 parts)
```

- Script files `./src/` + ./roger_skyline.py`

| [name].py | Description |
| --- | --- |
| **roger_skyline.py** | Main script. Can take argument for mgt.|
| **createvm.py** | Configure the vm using info file.|
| **install_os.py** | Subscript for OS installation.|
| **loadscript.py** | Inject Roger-skyline-1 configuration files into the vm.|
| **parser.py** | Parse info file and create the dinfo dictionnary.|
| **secure.py** | Main script for deploying Roger-skyline-1 scripts including web server.|
| **shutdown.py** | Shutdown the vm.|
| **start.py** | Run the vm or start a SSH session.|

- Roger-skyline-1 configuration files

| [name].sh | Description |
| --- | --- |
| **config_cron.sh** | Inject scheduled tasks to crontab that update all source packages and feed a /var/log/update_script.log.|
| **config_denialofservices.sh** | Protect open ports and set traps for port scans.|
| **config_firewall.sh** | Set rules of the firewall.|
| **config_grub.sh** | Disable grub at boot time.|
| **config_network.sh** | Set network settings. (modify preseeding if changed)|
| **config_ports.sh** | Protect from denial of services attacks.|
| **config_ssh.sh** | Set private key and change ssh port.|

---

## Ports

Port that was modified:

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
