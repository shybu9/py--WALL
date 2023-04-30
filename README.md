# py--WALL

simple python script for simulating an web firewall.<br>
 ~can be used to filter unauthorized access of methods, paths and key:values by the client over web-http on localhost.<br>
 ~starts by opening a python http server using given port number on localhost.<br>
 ~once started, script will look for given arguments in client-requests.<br>
 ~detected requests are proceeded for handling and response will be sent according to the given error_code.<br>
 ~all the malicious/unauthorized request logs are highlighted along with the client-ip and client-response sent. <br>
 
 ![pywall--help](https://user-images.githubusercontent.com/112984045/235347355-afcd06f4-0e72-4cad-95d8-a38d751ab300.png)



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
 
 #### ~Filtering by request method:
 ```bash
sudo python3 webwall.py -P <port_no.> --error_code <error_response_tobe_sent> --error_msg <msg_tobe_displayed> -r <POST/GET>
 ```
 `$ sudo python3 webwall.py -P 8000 -r GET --error_code 403 --error_msg restricted_method-access_identified`
 
 ![pywall-getrequest-blocke-terminal](https://user-images.githubusercontent.com/112984045/235345404-c6c894b2-8a27-49ec-b99f-6185f6d8d35b.png)
 ![pywall-getrequest-blocke-web](https://user-images.githubusercontent.com/112984045/235345469-8114c64e-55ce-4347-a466-3a43042b4223.png)

 
 
#### ~Filtering by restricted path access:
 ```bash
sudo python3 webwall.py -P <port_no.> --error_code <error_response_tobe_sent> --error_msg <msg_tobe_displayed> --badpath </<restricted_path>
  ```
  `$ sudo python3 webwall.py -P 8000 --badpath /assets --error_code 403 --error_msg restricted_path-access_identified`
  
  ![pywall-pathblocked-assests-terminal](https://user-images.githubusercontent.com/112984045/235345622-d577b872-c775-4e42-804c-2fe61f8e7be6.png)
  ![pywall-pathblocked-assests-web](https://user-images.githubusercontent.com/112984045/235345627-6215b9db-0726-4289-bc11-1bffdca93210.png)



 #### ~Filtering by a single key & its value:
  ```bash
sudo python3 webwall.py -P <port_no.> --error_code <error_response_tobe_sent> --error_msg <msg_tobe_displayed> --badkey <key> --badvalue <value>
  ```
  `$ sudo python3 webwall.py -P 8000 --badkey DNT --badvalue 1 --error_code 403 --error_msg malicious_key:value_identified`
  
![pywall-dntvalue-blocked-terminal](https://user-images.githubusercontent.com/112984045/235345784-9a46a0ae-3ccd-46e2-ba3b-5d7052fc70fb.png)

<br>  
  
  #### ~Filtering by key:value file:
  ```bash
sudo python3 webwall.py -P <port_no.> --error_code <error_response_tobe_sent> --error_msg <msg_tobe_displayed> --keyfile <filename-withpath>
  ```
  `$ sudo python3 webwall.py -P 8000 --keyfile keysnvalues --error_code 403 --error_msg malicious_keyrequest_identified`
  
![pywall-keyfile-blocked-terminal](https://user-images.githubusercontent.com/112984045/235345800-b93a5f57-6fba-4cce-b5fa-6028b2342af7.png)

~ make sure that given file is in key:value(json) file format.

##### * Feel free to use multiple filters
  

* any remarks:<br> 
####      do write to shy.bu9@gmail.com
