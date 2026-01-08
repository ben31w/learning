# Files

## Find Files

- `find . -name PATTERN` 
  - recursively search for files that match the pattern.
  - * = wildcard.
  
- `ls | grep REGEX`
  - list files in this directory that match the REGEX.
  - . = any character, \. = escape and search for literal dot
  

## Manage Directories

- `mkdir MY_DIR` make directory

- `rmdir MY_DIR` remove directory, must be empty!

- `rm -rf MY_DIR` recursively remove directory

## Manage Files

- `touch MY_FILE` create file

- `edit MY_FILE` edit file

- `cat MY_FILE` display content of file

- `rm MY_FILE` delete file

- `chmod 777 MY_SHELL_FILE`  change file mode bits to read/write/execute

## Run Files

- `dex DESKTOP_FILE` run a desktop file 

## Zip Files

- `tar -cvf TAR_FILE_OUT DIR_IN` create tar file from a directory

- `tar -xvf TAR_FILE` extract zip file in current directory

- `tar -xvf TAR_FILE -C DIR` extract zip file to given directory. This is a capital C!!

- `7z e 7ZIP_FILE.7z` extract 7-Zip file in current directory, or you can specify a destinatino with -o.

- `gunzip *`  extract all .tar.gz files in current directory, and delete .tar.gz files



# Network Management

- `ifconfig` interface configurations

- `ip a` get IP address

- `ip r` get router's IP address

- `sudo arp-scan -l` sends arp packet to all addresses on the LAN, and gets IP-MAC mappings. Noisy, active scan.

- `arp -a` lists arp cache

- `ssh <NAME/IP> -lroot` SSH into a computer, log in as root



# Package Management

## Advanced Packaging Tool (APT)

- Basic functionality:
  - package management tool for Debian-based systems
  - provides access to a remote package repository
  - provides tools for installing and upgrading packages from the remote repo or from local files.

- `apt update` updates package repository

- `apt install PACKAGE` installs a package from the repository

- `apt install LOCAL_DEB_FILE` installs a loca .deb file
  - You may need to give the absolute path
  - If you are updating an application with a local deb file, simply install it like normal
    (https://askubuntu.com/questions/982407/how-to-update-software-installed-via-deb-file).

- `apt remove PACKAGE`

- `apt list --installed`

## Snap

- Basic functinality:
  - package management tool for various Linux distributions



# Process Management

- Process: a running instance of a program, with a process control block and process ID (PID)

- `lsof` list open files and processes using them

- `kill -9 PID` kill process with this PID

- `gnome-system-monitor` running processes GUI

- `baobab` disk usage GUI



# Programming Langauges

## Java

- `javac JAVA_FILE(S) [-d CLASS_FILE_DIRECTORY]`  compile .java files into .class files

- `java [-classpath CLASS_FILE_DIRECTORY] CLASS_FILE`  run .class file

## Python

- `python3 -m pip install --upgrade pip`

- `python3 -m venv .venv` creates a virtual environment called .venv

- `source .venv/bin/activate` activated virtual environment

- `deactivate` deactvate virtual environment

## pyenv

- Setup instructions
  - https://itsfoss.gitlab.io/post/how-to-manage-multiple-python-versions-with-pyenv-on-linux/ 
  - https://www.pythontutorials.net/blog/importerror-no-module-named-tkinter-please-install-the-python3-tk-package/

- `pyenv install VERSION` install specified version

- `pyenv install --list`  list all versions available for installation

- `pyenv global VERSION` set global python version

- `pyenv local VERSION` set current directory's python version

- `pyenv shell VERSION` set current shell's python version

- `pyenv version` list currently selected version

- `pyenv versions`  list installed versions


# User Management

- `sudo su` switch to root

- `passwd root` set root's password



