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
 
 ![pywall-getrequest-blocke-terminal](https://user-images.githubusercontent.com/112984045/235345404-c6c894b2-8a27-49ec-b99f-6185f6d8d35b.png)
 ![pywall-getrequest-blocke-web](https://user-images.githubusercontent.com/112984045/235345469-8114c64e-55ce-4347-a466-3a43042b4223.png)

 
 
#### * Filtering by restricted path access:
 ```bash
sudo python3 webwall.py -P <port_no.> --error_code <error_response_tobe_sent> --error_msg <msg_tobe_displayed> --badpath </<restricted_path>
  ```
  `$ sudo python3 webwall.py -P 8000 --badpath /assets --error_code 403 --error_msg restricted_path-access_identified`
  
  ![pywall-pathblocked-assests-terminal](https://user-images.githubusercontent.com/112984045/235345622-d577b872-c775-4e42-804c-2fe61f8e7be6.png)
  ![pywall-pathblocked-assests-web](https://user-images.githubusercontent.com/112984045/235345627-6215b9db-0726-4289-bc11-1bffdca93210.png)



 #### * Filtering by a single key & its value:
  ```bash
sudo python3 webwall.py -P <port_no.> --error_code <error_response_tobe_sent> --error_msg <msg_tobe_displayed> --badkey <key> --badvalue <value>
  ```
  `$ sudo python3 webwall.py -P 8000 --badkey DNT --badvalue 1 --error_code 403 --error_msg malicious_key:value_identified`
  
![pywall-dntvalue-blocked-terminal](https://user-images.githubusercontent.com/112984045/235345784-9a46a0ae-3ccd-46e2-ba3b-5d7052fc70fb.png)

<br>  
  
  #### * Filtering by key:value file:
  ```bash
sudo python3 webwall.py -P <port_no.> --error_code <error_response_tobe_sent> --error_msg <msg_tobe_displayed> --keyfile <filename-withpath>
  ```
  `$ sudo python3 webwall.py -P 8000 --keyfile keysnvalues --error_code 403 --error_msg malicious_keyrequest_identified`
  
![pywall-keyfile-blocked-terminal](https://user-images.githubusercontent.com/112984045/235345800-b93a5f57-6fba-4cce-b5fa-6028b2342af7.png)
  
  

* any remarks:<br> 
####      do write to shy.bu9@gmail.com
