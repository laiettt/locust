# locust

***
## structure

locust/  
&nbsp;|─ src  
&nbsp;|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; |─ apis  
&nbsp;|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; |─ locustfiles  
&nbsp;|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; |─ model  
&nbsp;|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; |─ utils  
&nbsp;|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ tasks  
&nbsp;|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; |─ task1.py  
&nbsp;|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ task2.py  
&nbsp;|─ testdatas   
&nbsp;|─ requirements.txt  
&nbsp;|─ .gitignore  
└─ README.md  

***
## structure summary

apis ->  api call  
utils -> some common function, like request or read csv  
model -> define object  
tasks -> by service or main function  
locustfiles -> run locust  

***

## create requirements
```
- pip3 install pipreqs
- pipreqs . --encoding=utf8

# if requirements.txt already exists, use --forcre {path} to overwrite, like
- pipreqs --force . --encoding=utf8
```

## install requirements
```
- pip3 install -r requirements.txt
```

***

## run locust file
```
( cd to locust file path )
- locust -f chatroom.py
(defalut testfile is qa01.csv, run qa02.csv with 'locust -f chatroom.py testfile=qa02')
```

## run locust with Distributed (master and slave)
```
( cd to locust file path )
- locust -f chatroom.py --master
- locust -f chatroom.py --testfile=qa01 --worker
- locust -f chatroom.py --testfile=qa02 --worker

(different machine) 
- locust -f chatroom.py --worker --master-host={192.168.*.*}
```