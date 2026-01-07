                                                    --Assessment Documentation--

Firstly, To create a docker image using Static html  

 	=> sudo mkdir -p /var/www/hosthtml  

Created directory and named it hosthtml 

  => sudo nano /var/www/hosthtml/index.html 

Then Created one nano file, it contains  

  <h1>Hi,Mohana is Here :)</h1> 

  <p>Welcome to my page</p> 

Created configuratin file 

  => sudo nano /etc/nginx/sites-available/hosthtml 

It contains, 

    server { 

    listen 8077; 

    server_name _; 

    root /var/www/hosthtml; 

    index index.html; 

    location / { 

    try_files $uri $uri/ =404; 

    } 

    } 

=>sudo ln -s /etc/nginx/sites-available/hosthtml /etc/nginx/sites-enabled/ 

=> sudo nginx -t 

=> sudo systemctl restart nginx 

Then run it in browser  
 
 <img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/6acb1dc5-a533-491d-9ad9-cfaa9d3f0431" />

=>sudo nano Dockerfile

  FROM nginx:latest

  COPY . /usr/share/nginx/html

  EXPOSE 80

=>docker build -t host_image .

=>docker run -d -p 8066:80 --name host_container host_image

<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/ceeb10f5-bc8f-4251-88d6-0f768aeb7305" />

=>sudo lsof -i:8077
  
  When i run 8077 port,it belongs to nginx
  
  COMMAND  PID     USER   FD   TYPE DEVICE SIZE/OFF NODE NAME
  
  nginx   3476     root    8u  IPv4  33334      0t0  TCP *:8077 (LISTEN)
  
  nginx   3477 www-data    8u  IPv4  33334      0t0  TCP *:8077 (LISTEN)

=>sudo lsof -i:8066
  
  When i run 8066 port,it belongs to docker
  
  COMMAND    PID USER   FD   TYPE DEVICE SIZE/OFF NODE NAME
  
  docker-pr 5068 root    7u  IPv4  39892      0t0  TCP *:8066 (LISTEN)
  
  docker-pr 5073 root    7u  IPv6  39893      0t0  TCP *:8066 (LISTEN)

---Login docker with in Linux---
=>docker login -u mohanapriyab
  Logs you into Docker Hub using the username mohanapriyab.

=>docker tag demo1 mohanapriyab/demo1:latest
  Creates a new name (tag) for an existing image.
  
=>docker push mohanapriyab/demo1:latest
  Uploads the image from your local machine to Docker Hub.

Then open the Docker hub and it has the image that we created

<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/52f15bf0-74af-4125-99ba-4ebf65518a84" />




  











