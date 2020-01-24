##  SCRIPTS TO AUTOMATE LOGIN PROCESS FOR SRM WIFI NETWORKS  

### Dependencies: 

1) Chrome Web Driver      -- Included  - For Linux  
            
2) Selenium For Python    -- pip3 install selenium 

### Files

    - login.py
    - loginwifi.sh 
    - chromedriver
    - SRMCLUSTER VPN Certificate if required 

###  Steps For Running it on your PC

Step 1) Change the Chrome Driver path in line 8 of login.py

Step 2) Fill  line 18 and 19 with your credentials in login.py

Step 3) Run in terminal -  python3  login.py

If you want to automatically login every 6 hours to the network with a background process in linux :

Step 4) Run in terminal - nohup sh loginwifi.sh &

Note: Dont forget to note the PID if you need to kill this process in the future 

      Use options.headless=False in line 7 of login.py to hide the chrome driver

loginwifi.sh is running in Samantha with PID 27985






