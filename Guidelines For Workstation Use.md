## Guidelines For Using The Workstation  

### How to use the workstation remotely via ssh

For logging in to the machine

    1) Run in the terminal  ssh -p 433 associate@10.4.81.122 
    
    2) Accept the key 

    3) Enter the Password 

For using jupyter notebooks

    1) Run in terminal    ssh -p 443 -L 8880:127.0.0.1:8880 associate@10.4.81.122

    2) Accept the key 

    3) Enter the Password

Useful commands for Linux: 

    1) lsblk - to check the disk drives info. 

    2) htop  - to check the CPU Utilization.

    3) nvidia-smi --query-gpu=timestamp,temperature.gpu,utilization.gpu,utilization.memory,memory.total,memory.free,memory.used,power.draw,clocks.sm,clocks.mem,clocks.gr  --format=csv -l 1 

        To check realtime GPU stats.

    4) w - to see current users.

    5) mkdir - to make your own directories.

    6) Conda related commands can be found in the CONDA CHEAT SHEET.pdf

### General Guidelines for remote use via ssh

    - Sharing of ssh credentials will lead to strict action against members or associates.

    - Avoid turning it off and on again 

        - In case a reboot is required follow this checklist:

            1) Check if any other user is logged on by using the command w in terminal.

            2) Check for system usage stats to verify that important processes are not running in the background htop / nvidia-smi / i7z.

            3) Check tmux sessions by using the command tmux attach.

    - DO NOT Log-off or put the machine in sleep mode just lock it when required (win+l).

    - DO NOT interfere with directories which do not belong to your work.

    - DO NOT install packages on your own, ask the Administrators to set up the environment for you. 

    - Loading personal data on the machine is strictly prohibited.

    - DO NOT attempt to train on GPU when GPU is already busy with other training tasks. 

    - Avoid working while CPU utilization is high might lead to system instability 

### Things that are ready to use

    - Kaggle API is installed to download datasets easily over ssh.

    - Conda is up and running.

    - Basic python packages are already installed.

    - Tensorflow and Pytorch have been installed along with Keras and fastai.

### General Guidelines for woking on Samantha locally

    - Keep the desk clean at all times. 

    - The machine desk is strictly reserved for work purposes only don't sit near the machine for chitchat.

    - Chrome-Driver may open up during your use don't worry about it is to log in to the network automatically.

###  Troubleshooting 

    -  Error "Connection failed" or "unavailable" This means that the machine is probably turned off.

    -  Error "No route to host is available" 

        This means that the  machine is disconnected from the Wi-Fi Network 

        The only way to deal with this problem currently is by reconnecting to the 'SRM CAMPUS' wifi on the machine manually.

    -  The Internet is not working on the machine, cd to home directory and run python3 login.py in the terminal. A background process is already 
     
       running to login to the wifi automatically if it's causing trouble contact administrators.

    -  If any other issue arises contact the administrators immediately.



