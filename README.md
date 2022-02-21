### Weblab1
### Краткий перечень функциональных требований:  
+ Регистрация  
+ Авторизация  
+ Get list market's post
+ Get list find tutor post
+ Get list find employee post
+ Up a post in market
+ Up a post in find tutor
+ Up a post in find employee
+ Update info in market
+ Update info in find tutor
+ Update info in find employee
### Run:  
### 1.  
Check PATH in ==nginx.conf.template== in the very firstime.  
### 2. Generate SSL certificate  
    openssl req -x509 -out localhost.crt -keyout localhost.key \
      -newkey rsa:2048 -nodes -sha256 \
      -subj '/CN=localhost' -extensions EXT -config <( \
       printf "[dn]\nCN=localhost\n[req]\ndistinguished_name = dn\n[EXT]\nsubjectAltName=DNS:localhost\nkeyUsage=digitalSignature\nextendedKeyUsage=serverAuth")
### 3. In terminal:  
    sh ./configure_nginx.sh
    sh ./run_nginx.sh  
    sh ./run_server.sh  
### 4. For unbind().
    sudo killall nginx  
### Swagger:  
[SwaggerCode](https://app.swaggerhub.com/apis/ttbauman/SocialNetwork/v1)
### Schemas

![](https://github.com/anewday1999/web_lab_project/blob/main/pictures/usecase.png)
![](https://github.com/anewday1999/web_lab1/blob/main/pictures/271945594_445223547057446_3338745181557684151_n.png "pic2")
![](https://github.com/anewday1999/web_lab1/blob/main/pictures/271754414_442511257423432_4071665780707693716_n%20(1).png "Data structure")
### Weblab2  
### 1  
[moodboardPrintest](https://www.pinterest.ru/anewday1999/wgs/)
### 2
[Figma](https://www.figma.com/file/OKsUT7yxeimPKHQRQP2J64/WSP?node-id=0%3A1)
