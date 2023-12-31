## Create environment
```bash
pip install virtualenv
```

```bash
python -m venv env
```

## Packages
```bash
https://wkhtmltopdf.org/downloads.html   ---> Download executable wkhtmltopdf
```
```bash
pip install -r requirements.txt
```

## Activate environment
```bash
.\env\Scripts\activate
```

## Access to server
```bash
ssh -i .\key.pem ubuntu@44.209.162.29
ssh -i llave.pem ubuntu@IP -l root
sudo su -
```

## Configure Server
```bash
sudo apt-get update
sudo apt-get upgrade
sudo apt install python3-pip
pip3 --version
pip install "pipenv==2021.5.29"

sudo pipenv install
pipenv --venv  --> root@ip-172-31-43-84:/var/www/webApp# pipenv --venv
/root/.local/share/virtualenvs/webApp-c1qRIGue

pip install pipenv
```
## Apache 

```bash
https://www.digitalocean.com/community/tutorials/how-to-install-the-apache-web-server-on-ubuntu-20-04
sudo apt update
sudo apt install apache2
sudo ufw app list --->Available applications:
  Apache
  Apache Full
  Apache Secure
  OpenSSH
sudo ufw enable
sudo ufw allow 'Apache'
sudo ufw status --->Output
Status: active

sudo systemctl status apache2 --> Active

sudo a2ensite webApp.conf
sudo systemctl reload apache2
sudo apachectl configtest ---> Probar errores


```
### Install Module WSGI

```bash
sudo apt-get install libapache2-mod-wsgi-py3

root@ip-172-31-43-84:/var/www/webApp# sudo a2enmod wsgi
Module wsgi already enabled
root@ip-172-31-43-84:/var/www/webApp#

sudo apachectl configtest

sudo apachectl restart
```

#### Verificar si esta Apache
```bash
 sudo ufw app list
```

#### Instalar Apache
```bash
sudo apt install apache2
sudo systemctl status apache2
sudo ufw allow 'Apache'
```
#### Module msgi
```bash
sudo apt-get install apache2 libapache2-mod-wsgi
```
#### WebApp
```bash
sudo apt-get install python3-pip
```

#### Extra

```bash
sudo systemctl start apache2
sudo systemctl stop apache2

```

### Additional features

https://wkhtmltopdf.org/downloads.html

ruta = os.path.join(os.path.dirname(__file__), "csv_vacio.csv")
pip install pipenv
<br>
nano ~/.bashrc

export PATH="$HOME/.local/bin:$PATH"

source ~/.bashrc


```bash
# Asegúrate de estar dentro del entorno virtual
ubuntu@ip-172-31-44-230:/var/www/webApp$ pipenv shell

# Dentro del entorno virtual, verifica las dependencias instaladas
(webApp) ubuntu@ip-172-31-44-230:/var/www/webApp$ pip list


activate_this = '/home/ubuntu/.local/share/virtualenvs/webApp-c1qRIGue/bin/activate_this.py'

# Ejecuta activate_this.py para activar el entorno virtual
with open(activate_this) as file_:
    exec(file_.read(), dict(__file__=activate_this))

# Agrega la ruta del proyecto al sistema
project_dir = '/var/www/webApp'
if project_dir not in sys.path:
    sys.path.append(project_dir)

# Importa tu aplicación Flask después de activar el entorno virtual
from app import app as application



```