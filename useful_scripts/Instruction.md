# Usage Instructions

**Notes**: 
* You can add all these scripts to your path for easy access.
* All scripts only work with Unix System

## Adding scripts to Path
1. go to your home folder in your terminal (Opens to home by default)
```bash
$ cd ~
```
2. Run the following command:
```bash
$ sudo vim .bashrc
```
3. Add the following line to your .bashrc:
```bash
$ export PATH="$PATH:$Folder_Path"
```
> * Here the $Folder_Path is replaced with wherever your folder is cloned in drive. 
> * Don't forget to link the /useful_scripts folder.

## samantha.sh
open your terminal and run the following code:
```bash
$ ./secshell.sh
```
## samantha_jupyter.sh
<u>Simple script to ssh into samantha</u><br>
open your terminal and run the following code:
```sh
$ ./secshell.sh
```
> Wait for password prompt
open your terminal and run the following code:
```sh
$ jupyter lab --port 8880
```
> **Note**: 'lab' and 'notebook' can be used interchangably