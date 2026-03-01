# Gmail Auto Mail Manager

Herramientas en Python para automatizar tareas de Gmail usando IMAP y SMTP. Gestiona, responde y elimina correos de forma sencilla y automatizada.

## Características

- **auto_mail.py**: Responde automáticamente a correos no leídos que contienen palabras clave específicas en el asunto
- **delete_all_mails.py**: Elimina correos en lote con opciones de filtrado por carpeta y categorías
- Monitoreo continuo cada 60 segundos
- Interfaz de usuario interactiva con confirmación de acciones
- Procesamiento eficiente en lotes de hasta 100 correos

## Configuración

### 1. Obtener contraseña de aplicación de Google

Es necesario usar una contraseña de aplicación en lugar de tu contraseña principal de Gmail:

1. Accede a https://myaccount.google.com/apppasswords
2. Selecciona **Mail** y **Windows Computer** (o tu dispositivo)
3. Google generará una contraseña de 16 caracteres
4. Copia esta contraseña para usarla en la configuración

### 2. Configurar credenciales

Edita ambos scripts Python y añade tus credenciales en las primeras líneas:

```python
EMAIL = "tu-email@gmail.com"
PASSWORD = "contraseña-de-16-caracteres"  # Contraseña de aplicación de Google
```

## Uso

### Responder correos automáticamente

```bash
python auto_mail.py
```

**Funcionamiento:**
- Se ejecuta continuamente, revisando cada 60 segundos
- Busca correos no leídos en el inbox
- Detecta correos con "tarea" en el asunto
- Envía respuesta automática: "Hola, recibí tu mensaje. Te respondo pronto."
- Muestra en consola los correos procesados

### Eliminar correos en lote

```bash
python delete_all_mails.py
```

**Opciones disponibles:**
1. **Inbox completo** - Elimina todos los correos del inbox
2. **Carpeta específica** - Selecciona una carpeta personalizada para eliminar
3. **Categorías** - Limpia categorías automáticas (Social, Promotions, Updates, Forums)
4. **Papelera** - Vacía la papelera (eliminación permanente)

**Características:**
- Muestra confirmación antes de eliminar
- Procesa en lotes de 100 correos para mejor rendimiento
- Muestra barra de progreso durante la operación
- Lista todas las carpetas disponibles para consulta

## Estructura del Proyecto

```
manager_correos_electronicos/
├── auto_mail.py              # Script de respuesta automática
├── delete_all_mails.py       # Script de eliminación en lote
└── README.md                 # Este archivo
```

## Consideraciones de Seguridad

- **CRÍTICO**: Nunca publiques tus credenciales en repositorios públicos
- Usa únicamente contraseñas de aplicación generadas por Google, no tu contraseña principal
- Se recomienda usar un archivo `.gitignore` si trabajas con control de versiones
- La contraseña de aplicación de 16 caracteres es específica para esto y no compromete tu cuenta principal

## Requisitos

- Python 3.7 o superior
- Módulos estándar de Python (incluidos en cualquier instalación):
  - `imaplib` - Protocolo IMAP para lectura de correos
  - `smtplib` - Protocolo SMTP para envío de correos
  - `email` - Procesamiento de mensajes de correo
  - `time` - Control de intervalos

## Personalización

### Cambiar palabra clave de respuesta automática

En `auto_mail.py`, modifica la línea:
```python
if "tarea" in subject.lower():
```

Cambia `"tarea"` por la palabra clave que desees.

### Cambiar mensaje de respuesta

En `auto_mail.py`, modifica:
```python
reply = MIMEText("Hola, recibí tu mensaje. Te respondo pronto.")
```

### Cambiar intervalo de revisión

En `auto_mail.py`, modifica:
```python
time.sleep(60)  # Cambia 60 por segundos deseados
```

## Licencia

N/A

## Autor

Chávez Aguirre Juan Fernando
