                           Assessment Documentation 

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

# Copy your website files to nginx folder
COPY . /usr/share/nginx/html

# Expose port 80
EXPOSE 80

=>docker build -t host_image .

=>docker run -d -p 8066:80 --name host_container host_image

<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/ceeb10f5-bc8f-4251-88d6-0f768aeb7305" />






