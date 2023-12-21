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
ssh -i .\budgetpop.pem ubuntu@IP
```

## Configure Server
```bash
sudo apt-get update
sudo apt-get upgrade
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
