# Gmail Auto Mail Manager

Herramientas en Python para automatizar tareas de Gmail usando IMAP, SMTP y IA local con Ollama. Gestiona, responde inteligentemente y elimina correos de forma sencilla, automatizada y sin costo.

## 🤖 Características

- **auto_mail.py**: Responde automáticamente a TODOS los correos no leídos con respuestas personalizadas generadas por IA
- **delete_all_mails.py**: Elimina correos en lote con opciones de filtrado por carpeta y categorías
- **IA Local con Ollama**: Genera respuestas inteligentes y contextuales sin necesidad de APIs pagas
- **Privacidad garantizada**: Toda la IA se ejecuta localmente en tu PC
- Monitoreo continuo cada 60 segundos
- Interfaz de usuario interactiva con confirmación de acciones
- Procesamiento eficiente en lotes de hasta 100 correos

## 📋 Requisitos

### Requisitos del Sistema
- Python 3.7 o superior
- 8 GB de RAM mínimo (16 GB recomendado para mejor rendimiento)
- Ollama instalado (descargar de https://ollama.com)

### Módulos Python
- `imaplib` - Protocolo IMAP para lectura de correos
- `smtplib` - Protocolo SMTP para envío de correos
- `email` - Procesamiento de mensajes de correo
- `time` - Control de intervalos
- `ollama` - Cliente para generar respuestas con IA local

### Modelos Ollama Disponibles
- **deepseek-r1:8b** (Recomendado - Mayor precisión)
- `llama3.2:3b` (Ligero para PCs con menos RAM)
- `phi3:mini` (Ultra-ligero, ~4GB RAM)
- `mistral` (Alternativa equilibrada)

## ⚙️ Instalación

### Paso 1: Instalar Ollama
1. Descargar desde https://ollama.com/download
2. Instalar el ejecutable para Windows
3. Verificar instalación en PowerShell: `ollama --version`

### Paso 2: Descargar un modelo de IA
```powershell
# Recomendado (mejor calidad)
ollama pull deepseek-r1:8b

# Alternativas más ligeras
ollama pull llama3.2:3b
ollama pull phi3:mini
```

### Paso 3: Instalar dependencias Python
```powershell
pip install ollama
```

### Paso 4: Configurar credenciales de Gmail

#### 1. Obtener contraseña de aplicación de Google
Es necesario usar una contraseña de aplicación en lugar de tu contraseña principal de Gmail:

1. Accede a https://myaccount.google.com/apppasswords
2. Selecciona **Mail** y **Windows Computer** (o tu dispositivo)
3. Google generará una contraseña de 16 caracteres
4. Copia esta contraseña

#### 2. Configurar en los scripts
Edita `auto_mail.py` y `delete_all_mails.py` y añade tus credenciales:

```python
EMAIL = "tu-email@gmail.com"
PASSWORD = "contraseña-de-16-caracteres"  # Contraseña de aplicación de Google
```

## 🚀 Uso

### Responder correos automáticamente con IA

```bash
python auto_mail.py
```

**Funcionamiento:**
- Se ejecuta continuamente, revisando cada 60 segundos
- Busca correos no leídos en el inbox
- **Genera respuestas automáticas personalizadas** usando IA (Ollama)
- Las respuestas se adaptan al asunto y contenido del correo
- Máximo 3 líneas por respuesta (respuestas concisas)
- Muestra en consola los correos procesados y respuestas enviadas
- **Totalmente gratis**: Sin límites, sin costo, sin APIs externas

**Nota**: 
- La primera ejecución cargará el modelo de IA (2-5 minutos)
- Cada respuesta tarda 2-10 segundos según tu PC
- Ollama debe estar corriendo (se inicia automáticamente)

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

## 📁 Estructura del Proyecto

```
manager_correos_electronicos/
├── auto_mail.py              # Script de respuesta automática con IA
├── delete_all_mails.py       # Script de eliminación en lote
└── README.md                 # Este archivo
```

## 🔧 Personalización

### Cambiar modelo de IA
En `auto_mail.py`, modifica la línea dentro de `generar_respuesta_ia()`:
```python
response = ollama.chat(model='deepseek-r1:8b', messages=[...])
# Cambia 'deepseek-r1:8b' por otro modelo disponible
```

### Cambiar intervalo de revisión
En `auto_mail.py`, modifica:
```python
time.sleep(60)  # Cambia 60 por segundos deseados
```

### Cambiar el prompt de IA
En `auto_mail.py`, modifica la función `generar_respuesta_ia()`:
```python
promt = f"""Eres un asistente de correo. Genera una respuesta breve y profesional...
# Reemplaza con tu propio prompt personalizado
```

### Añadir filtros específicos
Modifica la función `check_mail()` para responder solo a ciertos correos:
```python
# En lugar de:
if True:
    # Cambia a:
if "palabra_clave" in subject.lower():
```

## 🔒 Consideraciones de Seguridad

- **CRÍTICO**: Nunca publiques tus credenciales en repositorios públicos
- Usa únicamente contraseñas de aplicación generadas por Google, no tu contraseña principal
- Se recomienda usar un archivo `.gitignore` si trabajas con control de versiones:
  ```
  *.py
  !auto_mail.py
  !delete_all_mails.py
  ```
- La contraseña de aplicación de 16 caracteres es específica para esto y no compromete tu cuenta principal
- **Privacidad**: Todo se procesa localmente, ningún dato sale de tu PC

## 💡 Ventajas de usar IA local (Ollama)

✅ **Totalmente gratis** - Sin límites de API, sin suscripciones  
✅ **Privacidad total** - Tus correos nunca salen de tu PC  
✅ **Sin dependencias externas** - Funciona offline  
✅ **Personalizable** - Ajusta los prompts según necesites  
✅ **Rápido** - Respuestas en segundos  

## 📊 Ejemplos de Respuestas Generadas por IA

### Entrada
- **Asunto**: "Consulta sobre el presupuesto del proyecto"
- **Contenido**: "Hola, necesitamos revisar los costos..."

### Salida (Respuesta IA)
```
Hola, gracias por tu correo.
He recibido tu consulta sobre presupuesto y la revisaré pronto.
Te responderé con los detalles en breve.
```

## 🐛 Solución de Problemas

### El script no responde
- **Verifica**: ¿Ollama está corriendo? (`ollama list`)
- **Verifica**: ¿El modelo está descargado? (`ollama list`)
- **Verifica**: ¿EMAIL y PASSWORD están configurados?

### Las respuestas tardan mucho
- Normal en primeras ejecuciones (carga del modelo)
- Depende de tu RAM y procesador
- Los modelos más ligeros son más rápidos

### Error de conexión a Gmail
- Verifica credenciales (EMAIL y PASSWORD)
- Confirma que usas "contraseña de aplicación", no tu contraseña de Gmail
- Activa el acceso a aplicaciones menos seguras si es necesario

### Ollama no inicia
- Descargar nuevamente desde https://ollama.com
- Ejecutar como administrador
- Reiniciar el sistema

## 📝 Licencia

N/A

## 👤 Autor

Chávez Aguirre Juan Fernando

---

**Última actualización**: Marzo 2026  
**Rama**: feat/Agregando-IA
