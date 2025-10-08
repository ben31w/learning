# VirtualBox

Host key is Right Ctrl. This is used to uncapture the mouse.

# KVM

## macOS VM

### How To Install
https://www.makeuseof.com/macos-ubuntu-linux-virtual-machine/

### How to Start
- `cd ~/KVM/macOS`
- `sudo ./basic.sh`
- Select Boot macOS from MainDisk
- Password is same as this computer.

### How to Stop

Ctrl+C inside the terminal you ran the startup script in.

### How to Set Up SMB Shared Drive

This is a shared folder between host and guest.
It's useful for copy+pasting text between the machines.
Actually setting up shared clipboards is difficult/I haven't figure it out.

https://chatgpt.com/c/67b2910c-12e8-8002-935f-51427b727ebc

### Access SMB Shared Drive

- host location: /home/ben31w/shared
- VM location:
  - in Finder, mac Key + K
  - smb://192.168.1.155/shared  (or whatever current host IP address is)
  - username and password are set up on the host machine!!
    - cat /etc/samba/smb.conf
    - currently ben31w/host password

### QEMU Keyboard shortcuts

- Ctrl + Alt + G : Capture/grab
- Ctrl + Alt + F : Fullscreen

Currently storing useful stuff (AppleScript files) in Documents folder.
  
