# Plataforma de Profesionales

## Descripción
Este proyecto es un prototipo de plataforma web donde los profesionales pueden crear su perfil y los visitantes pueden buscarlos y contactarlos.

## Funcionalidades
- Registro e inicio de sesión solo para profesionales.
- Crear y editar perfil con:
  - Foto principal y galería.
  - Descripción de servicios.
  - Distrito / ciudad (mostrado en mapa).
  - Tarifa aproximada.
- Listado público de profesionales con buscador y filtros.
- Perfil público de cada profesional.
- Botón de contacto vía WhatsApp.

## Instalación y uso
1. Crear una carpeta principal y dos subcarpetas(uno para el frontend y otro para el backend) y ejecutar estos los comandos en su respectiva subcarpeta

ejecutar el siguiente comando en la carpeta del frontend:
```bash
git clone https://github.com/joel-machaca/manejo-de-perfiles-profesionales.git .
```

ejecutar el siguiente comando en la carpeta del backend:
```bash
git clone https://github.com/joel-machaca/backend-perfiles.git .
```

## Variables de entorno 
### (FRONTEND)
Crea un archivo `.env` en la carpeta del "frontend" y añade las variables

VITE_API_URL= url del backend 

ejecutar para instalar dependencias
```bash
npm install
```
finalmente ejecutar :
```bash
npm run dev
```


### (BACKEND)

Crea un archivo `.env` en la carpeta del "backend" y añade las variables necesarias.

FRONTEND_URL= aqui va la url del frontend paso (1)
SUPABASE_KEY= aqui va la clave "API KEY" de supabase (2)
SUPABASE_URL= aqui va la url del proyecto (3)
DATABASE_URL= aqui va la url de la base de datos (4)

Crear y activar entorno virtual:
```bash
python -m venv .venv
```
luego (windows)
```bash
.venv\Scripts\activate
```
instalar dependencias
```bash
pip install -r requirements.txt
```

ejecutar el backend
```bash
uvicorn main:app --reload
```

## Variables de entorno y creacion de la base de datos 


### (1) FRONTEND_URL
pegar la url del frontend despues de ejecutar el comando "npm run dev"


### (2) SUPABASE (storage) funciona para guardar las imagenes SUPABASE_KEY

#### Para obtener la clave "API KEY":

1. Crea una cuenta en [Supabase](https://supabase.com/) y accede a tu proyecto.

2. Ve a Project Settings → API KEYS.

3. Allí encontrarás la API Key cifrada como **** **** **** ****. Haz clic en Reveal y copia el código.

4. Pega ese código en la variable de entorno SUPABASE_KEY de tu backend.

Luego, para configurar el almacenamiento de imágenes:

1. En el panel de tu proyecto, ve a Storage / Almacenamiento.

2. Haz clic en New Bucket.

3. Asigna el nombre uploads.

4. Activa la opción Public bucket (primera opción).

5. Haz clic en Create para crear el bucket.

### (3) SUPABASE: obtener la URL del proyecto (SUPABASE_URL)

1. Entra a tu proyecto en Supabase.

2. Ve a Settings → API (también llamado “Project API”).

3. Copia el enlace que aparece como Project URL.

4. Pega ese enlace en la variable de entorno SUPABASE_URL de tu backend.

### (4) BASE DE DATOS (PostgreSQL) DATABASE_URL

1. Crea una base de datos en PostgreSQL.

2. Copia los datos de conexión y pégalos en la variable de entorno DATABASE_URL de tu backend.

3. El formato debe ser:

DATABASE_URL=postgres+psycopg2://usuario:contraseña@host:puerto/nombreBD

Reemplaza usuario, contraseña, host, puerto y nombreBD con los datos de tu base de datos.



## Uso de la aplicación

- Abre el frontend: http://localhost:5173

- El backend debe estar corriendo en http://localhost:8080

- Registra un profesional, crea perfil, prueba búsqueda y botón de contacto por WhatsApp.

## Notas

- No subas credenciales reales al repositorio.

- Ajusta las URLs en .env según tu entorno (local o producción).

- Para producción, usa hosting gratuito (Vercel, Netlify, Railway, etc.) y actualiza variables de entorno con las URLs correspondientes.


