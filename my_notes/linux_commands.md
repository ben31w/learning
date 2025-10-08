# Files

## Find Files
- `find . -name PATTERN` 
  - recursively search for files that match the pattern.
  - * = wildcard.
- `ls | grep REGEX`
  - list files in this directory that match the REGEX.
  - . = any character, \. = escape and search for literal dot
  
## Important Files
- `~/.bashrc`
  - executed by bash for non-login shells
  - can define aliases here
  - you must run `source ~/.bashrc` after you edit the file to apply the changes.

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
- `tar -xf ZIP_FILE` extract zip file in current directory, or you can specify a destination with -c.
- `tar -cf ZIP_FILE` create zip file
- `7z e 7ZIP_FILE.7z` extract 7-Zip file in current directory, or you can specify a destinatino with -o.
- `gunzip *`  extract all .tar.gz files in current directory, and delete .tar.gz files



# Network Management
- `ifconfig` interface configurations
- `ip a` get IP address
- `ip r` get router's IP address
- `sudo arp-scan -l` sends arp packet to all addresses on the LAN, and gets IP-MAC mappings. Noisy, active scan.
- `arp -a` lists arp cache
- `ssh 162.243.40.233 -lroot` SSH into a computer, log in as root



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



# User Management
- `sudo su` switch to root
- `passwd root` set root's password



