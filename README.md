# ETL Flow con Prefect en AWS EC2
<p align="center">
  <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/9/93/Amazon_Web_Services_Logo.svg/330px-Amazon_Web_Services_Logo.svg.png" width="100"/>
  <img src="https://www.cdnlogo.com/logos/a/99/aws-ec2.svg" width="70"/>
  <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/b/bc/Amazon-S3-Logo.svg/1712px-Amazon-S3-Logo.svg.png" width="80"/>
  <img src="https://prefect-284-docs.netlify.app/img/logos/prefect-logo-mark-solid-white-500.png" width="90"/>
</p>



En este proyecto realicé las siguientes tareas:

- Creé una instancia EC2 (t2.micro) con Ubuntu.
- Instalé Prefect en la instancia y levanté un servidor local.
- Conecté la aplicación con un bucket de Amazon S3.
- El @flow (flujo) primero lee un archivo `.json` ubicado en la carpeta (`/landing`) en S3, para luego aplicarle una transformacion al .json. Despues sube ese json a otra carpeta (`/processed`) en el mismo bucket.

El objetivo del proyecto es mostrar un pipeline simple de ETL usando Prefect, aprovechando los servicios gratuitos del Free Tier. Aca lo interesante es la infraestructura.

## Como ejecutar el proyecto EC2

### 1. Conectarse por SSH a la instancia EC2

```bash
ssh -i "clave.pem" ubuntu@18.229.xxx.xxx
```

(luego instalo git, python, pip...)

### 2. Levantar entorno virtual
```bash
python3.10 -m venv venv
```

```bash
source venv/bin/activate
```

### 3. Instalar dependencias del archivo requirements.txt
```bash
pip install -r requirements.txt
```

### 4. Levantar servidor Prefect
```bash
prefect server start --host 0.0.0.0 --port 4200 -b
```
- `-b` para que se ejecute en segundo plano.

### 5. Crear archivo .env con credenciales AWS
- Que seran leidas por `boto3` gracias a la libreria `dotenv`

### 6. Ejecutar flow/flujo ETL
```bash
python3.10 etl.py
```