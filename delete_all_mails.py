# Script para eliminar todos los correos de Gmail
import imaplib
import email
from dotenv import load_dotenv
import os
import json

load_dotenv()

def load_config():
    """Carga la configuración desde el archivo .json"""
    with open("config.json", "r") as f:
        return json.load(f)
    
CONFIG = load_config()
EMAIL = os.getenv("EMAIL")
PASSWORD = os.getenv("PASSWORD")


def delete_all_emails():
    """Elimina todos los correos del inbox"""
    try:
        # Conectar a Gmail
        mail = imaplib.IMAP4_SSL("imap.gmail.com")
        mail.login(EMAIL, PASSWORD)
        
        # Seleccionar el inbox
        mail.select("inbox")
        
        # Buscar TODOS los correos
        status, messages = mail.search(None, "ALL")
        
        if status == "OK":
            message_ids = messages[0].split()
            total = len(message_ids)
            
            if total == 0:
                print("No hay correos para eliminar.")
            else:
                print(f"Se encontraron {total} correos.")
                confirmacion = input(f"¿Estás seguro de que quieres eliminar {total} correos? (si/no): ")
                
                if confirmacion.lower() in ["si", "sí", "s", "yes", "y"]:
                    # Procesar en lotes de 100 correos
                    batch_size = 100
                    for i in range(0, len(message_ids), batch_size):
                        batch = message_ids[i:i + batch_size]
                        # Crear rango de IDs para el lote
                        ids_range = b','.join(batch).decode()
                        
                        # Marcar el lote completo
                        mail.store(ids_range, '+FLAGS', '\\Deleted')
                        
                        # Mostrar progreso
                        processed = min(i + batch_size, total)
                        print(f"Procesados {processed}/{total} correos...")
                    
                    # Eliminar permanentemente
                    print("Eliminando permanentemente...")
                    mail.expunge()
                    print(f"{total} correos eliminados exitosamente.")
                else:
                    print("Operación cancelada.")
        
        mail.logout()
        
    except Exception as e:
        print(f"Error: {e}")


#----------------------------------------------------------------------------------------------------------------------------------------------
def delete_emails_from_folder(folder="inbox"):
    """Elimina todos los correos de una carpeta específica"""
    try:
        mail = imaplib.IMAP4_SSL("imap.gmail.com")
        mail.login(EMAIL, PASSWORD)
        
        # Listar todas las carpetas disponibles
        print("\nCarpetas disponibles:")
        status, folders = mail.list()
        for folder_info in folders:
            print(folder_info.decode())
        
        # Seleccionar la carpeta especificada
        status, response = mail.select(folder)
        
        if status != "OK":
            print(f"\nError: No se pudo acceder a la carpeta '{folder}'.")
            print("Verifica que el nombre sea correcto.")
            mail.logout()
            return
        
        # Buscar todos los correos en esa carpeta
        status, messages = mail.search(None, "ALL")
        
        if status == "OK":
            message_ids = messages[0].split()
            total = len(message_ids)
            
            print(f"\nSe encontraron {total} correos en '{folder}'.")
            
            if total > 0:
                confirmacion = input(f"¿Eliminar {total} correos de '{folder}'? (si/no): ")
                
                if confirmacion.lower() in ["si", "sí", "s", "yes", "y"]:
                    # Procesar en lotes de 100 correos
                    batch_size = 100
                    for i in range(0, len(message_ids), batch_size):
                        batch = message_ids[i:i + batch_size]
                        ids_range = b','.join(batch).decode()
                        
                        mail.store(ids_range, '+FLAGS', '\\Deleted')
                        
                        processed = min(i + batch_size, total)
                        print(f"Procesados {processed}/{total} correos...")
                    
                    print("Eliminando permanentemente...")
                    mail.expunge()
                    print(f"{total} correos de '{folder}' eliminados exitosamente.")
                else:
                    print("Operación cancelada.")
        
        mail.logout()
        
    except Exception as e:
        print(f"Error: {e}")


#----------------------------------------------------------------------------------------------------------------------------------------------
def delete_emails_from_categories():
    """Elimina correos de categorías específicas (Social, Promotions, Updates, Forums)"""
    try:
        mail = imaplib.IMAP4_SSL("imap.gmail.com")
        mail.login(EMAIL, PASSWORD)
        
        categories = ["[Gmail]/Social", "[Gmail]/Promotions", "[Gmail]/Updates", "[Gmail]/Forums"]
        
        for category in categories:
            try:
                status, response = mail.select(category)
                
                if status == "OK":
                    status, messages = mail.search(None, "ALL")
                    
                    if status == "OK":
                        message_ids = messages[0].split()
                        total = len(message_ids)
                        
                        print(f"\n{category}: {total} correos encontrados")
                        
                        if total > 0:
                            confirmacion = input(f"¿Eliminar {total} correos de {category}? (si/no): ")
                            
                            if confirmacion.lower() in ["si", "sí", "s", "yes", "y"]:
                                batch_size = 100
                                for i in range(0, len(message_ids), batch_size):
                                    batch = message_ids[i:i + batch_size]
                                    ids_range = b','.join(batch).decode()
                                    
                                    mail.store(ids_range, '+FLAGS', '\\Deleted')
                                
                                mail.expunge()
                                print(f"{total} correos de {category} eliminados.")
                            else:
                                print("Eliminación cancelada para esta categoría.")
            
            except:
                print(f"No se pudo acceder a {category}")
        
        mail.logout()
        
    except Exception as e:
        print(f"Error: {e}")


#----------------------------------------------------------------------------------------------------------------------------------------------
def empty_trash():
    """Vacía la papelera (elimina permanentemente todos los correos en trash)"""
    try:
        mail = imaplib.IMAP4_SSL("imap.gmail.com")
        mail.login(EMAIL, PASSWORD)
        
        # En Gmail, la papelera es [Gmail]/Trash
        status, response = mail.select("[Gmail]/Trash")
        
        if status != "OK":
            print("Error: No se pudo acceder a la papelera.")
            mail.logout()
            return
        
        status, messages = mail.search(None, "ALL")
        
        if status == "OK":
            message_ids = messages[0].split()
            total = len(message_ids)
            
            if total == 0:
                print("La papelera está vacía.")
            else:
                print(f"Papelera: {total} correos encontrados")
                confirmacion = input(f"¿Vaciar la papelera ({total} correos)? Esta acción es permanente. (si/no): ")
                
                if confirmacion.lower() in ["si", "sí", "s", "yes", "y"]:
                    batch_size = 100
                    for i in range(0, len(message_ids), batch_size):
                        batch = message_ids[i:i + batch_size]
                        ids_range = b','.join(batch).decode()
                        
                        mail.store(ids_range, '+FLAGS', '\\Deleted')
                        
                        processed = min(i + batch_size, total)
                        print(f"Procesados {processed}/{total} correos...")
                    
                    mail.expunge()
                    print(f"Papelera vaciada: {total} correos eliminados permanentemente.")
                else:
                    print("Operación cancelada.")
        
        mail.logout()
        
    except Exception as e:
        print(f"Error: {e}")


#----------------------------------------------------------------------------------------------------------------------------------------------
def main_menu():
    """Menú principal para seleccionar una opción"""
    print("\n" + "="*50)
    print("   GESTOR DE ELIMINACIÓN DE CORREOS DE GMAIL")
    print("="*50)
    print("\nOpciones disponibles:")
    print("1. Eliminar todos los correos del Inbox")
    print("2. Eliminar correos de una carpeta específica")
    print("3. Eliminar correos de categorías (Social, Promotions, Updates, Forums)")
    print("4. Vaciar papelera (eliminación permanente)")
    print("5. Salir")
    print("\n" + "="*50)
    
    opcion = input("\nSelecciona una opción (1-5): ")
    
    if opcion == "1":
        delete_all_emails()
    elif opcion == "2":
        folder = input("Ingresa el nombre de la carpeta (ej: '[Gmail]/Spam'): ")
        delete_emails_from_folder(folder)
    elif opcion == "3":
        delete_emails_from_categories()
    elif opcion == "4":
        empty_trash()
    elif opcion == "5":
        print("Saliendo...")
        return False
    else:
        print("Opción no válida. Intenta de nuevo.")
    
    return True


if __name__ == "__main__":
    while main_menu():
        pass
