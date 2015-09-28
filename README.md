# noVnc Django PoC
PoC of the Django authentication plugin for Websockify.

Usage:  

Open two terminals. In both of them you need to cd into the "authenticated_websocket_django" directory.  
In one terminal run the webserver: python ./manage.py runserver 8000  
In the other one run the websocket server: ./websockify/run 6080   --auth-plugin="websockify.django_auth_plugins.SessionIdAuthAndHostPort" --auth-host-port  
Open your browser and go to http://127.0.0.1:8000, log in and click on the button "Connect".   
There are two different users available, both associated with different target hosts and ports (see the webosckify log to see that it tries to connect to different targets).  

First user:  
Username: luca  
Password: luca  

Second user:  
Username: bob  
Password: bob  


