# setup
note: this is a quick tutorial for centos7

make sure nginx is installed
make sure to download a version of python3.x (I'm using 3.5 here)

clone the repo into ```/var/www/<app_name>/```. Yes, put it inside ```<app_name>```

replace every instance of ```<app_name>``` with whatever you want to call this thing

## setup environment
### change dir

```cd /var/www/<app_name>/```

### create python3 virtual environment

```
virtualenv -p /usr/local/bin/python3.5 venv
```

### activate venv

```
source venv/bin/activate
```

### install requirements

```
pip install -r requirements.txt
```

### exit venv

```deactivate```

## create gunicorn daemon

### create the daemon service file

```vi /etc/systemd/system/<app_name>.service```

```
[Unit]
Description=Gunicorn instance to serve <app_name>
After=network.target

[Service] 
User=root 
Group=nginx 
WorkingDirectory=/var/www/<app_name>/ 
Environment="PATH=/var/www/<app_name>/venv/bin" 
ExecStart=/var/www/<app_name>/venv/bin/gunicorn --workers 4 --bind unix:app.sock -m 007 wsgi --reload --error-logfile /var/www/<app_name>/error.log

[Install] 
WantedBy=multi-user.target
```

### make it available

```systemctl enable <app_name>```

### make nginx proxy

```vi /etc/nginx/conf.d/<app_name>.conf```

``` 
server {

    listen 80;

    server_name <website_name>.com www.<website_name>.com;

    access_log  /var/log/nginx/<app_name>-access.log;
    error_log  /var/log/nginx/<app_name>-error.log;

    location / {
        proxy_set_header Host $host;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_pass http://unix:/var/www/<app_name>/app.sock;
    }

}
```

### reload nginx

```systemctl restart nginx```

### run it

```systemctl start <app_name>```
