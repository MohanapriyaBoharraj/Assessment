                                                    --Assessment Documentation--

   =======================================================PROJECT 1  DOCUMENTATION========================================================================

Firstly, To create a docker image using Static html  

=> sudo mkdir -p /var/www/hosthtml  

Created directory and named it hosthtml 

=> sudo nano /var/www/hosthtml/index.html 

Then Created one nano file, it contains  

        <h1>Hi,Mohana is Here :)</h1> 

        <p>Welcome to my page</p> 

Created configuration file 

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

--Create a Dockerfile--

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

----------------Login docker with in Linux--------------------

Logs you into Docker Hub using the username mohanapriyab.

          =>docker login -u username
  
Creates a new name (tag) for an existing image.    

          =>docker tag tagname username/imagename
  
Uploads the image from your local machine to Docker Hub.   

          =>docker push username/imagename
  
If we want ,we can pull the image from docker hub 

          =>docker pull username/imagename:latest

Then open the Docker hub and it has the image that we created

<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/52f15bf0-74af-4125-99ba-4ebf65518a84" />

------------GITHUB-------------

STEP1: Create a new public repository

STEP2: Go to the git bash and put the commands

STEP3: Initialize the git => git init

STEP4: Clone the repository => git clone

STEP5: Check the current changes of repo => git status

STEP6: Stage all changes => git add .

STEP7: Check status => git status

STEP8: Committing changes => git commit -m "message"

STEP9: Push it in local commits => git push
 
`````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````

     =======================================================PROJECT 2  DOCUMENTATION========================================================================

sudo mkdir -p /var/www/practice2

sudo nano /var/www/practice2/app.py
   
sudo nano /var/www/practice2/log.txt
   
ls /var/www/practice2
   
cd /var/www/practice2
   
cd ~
   
sudo chown -R mohana:mohana /var/www/practice2
   
sudo chmod -R 777 /var/www/practice2

cd /var/www/practice2

sudo nano app.py
   
python3 app.py

Appended a new line
Appended a new line
Appended a new line
Appended a new line

cat log.txt

Log entry at 2026-01-07 10:29:40.280230
Log entry at 2026-01-07 10:29:45.284259
Log entry at 2026-01-07 10:29:50.287982
Log entry at 2026-01-07 10:29:55.292490


sudo nano /var/www/practice2/Dockerfile
   
docker build -t python_img .

docker run -d -p 8054:80 --name py_container python_img
   
docker ps

sudo lsof -i:8054

    COMMAND    PID USER   FD   TYPE DEVICE SIZE/OFF NODE NAME

    docker-pr 6748 root    7u  IPv4  48780      0t0  TCP *:8054 (LISTEN)

    docker-pr 6753 root    7u  IPv6  48781      0t0  TCP *:8054 (LISTEN)
    
sudo nano /var/www/practice2/Dockerfile
   47  sudo nano app.py
   48  cat app.py
   49  cat log.txt
   50  ls
   51  sudo mkdir data
   52  sudo rm -rf log.txt
   53  ls
   54  cd data

cd ..

sudo nano app.py

python3 app.py

sudo chown -R mohana:mohana data

python3 app.py

cat data

cd data

ls

cat log.txt

sudo ufw allow 8028

docker run -d --name py_container -p 8028:80 -v /var/www/practice2:/data python_img

docker create --name py_container -v practice2_volume2:/practice2 alpine




  











