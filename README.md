# py--WALL
simple python script for simulating an web firewall.

## PRE-REQUIREMENTS  
* Python3 :
 ```bash 
     sudo apt-get install python3 
 ``` 
  
## DOWNLOADING_SCRIPT :
 ```bash 
     sudo git clone https://github.com/shybu9/py--WALL
 ```  
  
* script_requitements (after downloading_script) :
 ```bash 
     sudo pip3 install -r requirements.txt 
 ```
 

 
 ## USAGE
 
 #### * Filtering by request method:
 ```bash
sudo python3 webwall.py -P <port_no.> --error_code <error_response_tobe_sent> --error_msg <msg_tobe_displayed> -r <POST/GET>
 ```
 `$ sudo python3 webwall.py -P 8000 -r GET --error_code 403 --error_msg restricted_method-access_identified`
 
 
#### * Filtering by restricted path access:
 ```bash
sudo python3 webwall.py -P <port_no.> --error_code <error_response_tobe_sent> --error_msg <msg_tobe_displayed> --badpath </<restricted_path>
  ```
  `$ sudo python3 webwall.py -P 8000 --badpath /assets --error_code 403 --error_msg restricted_path-access_identified`
  
  
 #### * Filtering by a single key & its value:
  ```bash
sudo python3 webwall.py -P <port_no.> --error_code <error_response_tobe_sent> --error_msg <msg_tobe_displayed> --badkey <key> --badvalue <value>
  ```
  `$ sudo python3 webwall.py -P 8000 --badkey suffix --badvalue Request --error_code 403 --error_msg malicious_key:value_identified`
  
  
  #### * Filtering by key:value file:
  ```bash
sudo python3 webwall.py -P <port_no.> --error_code <error_response_tobe_sent> --error_msg <msg_tobe_displayed> --keyfile <filename-withpath>
  ```
  `$ sudo python3 webwall.py -P 8000 --keyfile /home/kali/test/test_restricted_keysandvalues.txt --error_code 403 --error_msg malicious_keyrequest_identified`
  

* any kind of access to given IP:PORT will be reported

![eazepot mbl](https://user-images.githubusercontent.com/112984045/220195119-d37cc62e-f932-4be0-97ff-6b1a2ef914e6.png)
![eazepot other](https://user-images.githubusercontent.com/112984045/220195129-7f3a5ec7-e994-4020-b71e-949c499f0c9c.png)


* any remarks:<br> 
####      do write to shy.bu9@gmail.com
