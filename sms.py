import requests
from colorama import init, Fore, Style

init(autoreset=True)

ROJO = Fore.RED
VERDE = Fore.GREEN
RESET = Style.RESET_ALL

banner = ROJO + """
░▒▓█▓▒░░▒▓█▓▒░▒▓████████▓▒░▒▓███████▓▒░░▒▓██████████████▓▒░░▒▓█▓▒░░▒▓███████▓▒░ 
░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░        
 ░▒▓█▓▒▒▓█▓▒░░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░        
 ░▒▓█▓▒▒▓█▓▒░░▒▓██████▓▒░ ░▒▓███████▓▒░░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓██████▓▒░  
  ░▒▓█▓▓█▓▒░ ░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░ 
  ░▒▓█▓▓█▓▒░ ░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░ 
   ░▒▓██▓▒░  ░▒▓████████▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░▒▓███████▓▒░  
""" + RESET

hongo = [
    "           _.-'78o `\"`--._",
    "       ,o888o.  .o888o,   ''-.",
    "     ,88888P  `78888P..______.]",
    "    /_..__..----\"\"        __.'",
    "    `-._       /\"\"| _..-''",
    "        \"`-----\\  `\\",
    "                |   ;.-\"\"--..",
    "                | ,8o.  o88. `.",
    "                `;888P  `788P  :",
    "          .o\"\"-.|`-._         ./",
    "         J88 _.-/    \";-P----'",
    "         `--'\\`|     /  /",
    "             | /     |  |",
    "             \\|     /   |"
]

def send_sms():
    print(banner)
    
    number = input("Ingrese el número de teléfono (formato internacional, ej: +59891234567): ")
    message = input("Ingrese el mensaje a enviar: ")
    
    use_custom_key = input("¿Desea usar una API Key personalizada? (s/n): ").strip().lower()
    if use_custom_key == 's':
        api_key = input("Ingrese su API Key de Textbelt: ")
    else:
        api_key = "textbelt"
        print("Usando clave de API gratuita (1 mensaje por día permitido).")
    
    response = requests.post("https://textbelt.com/text", data={
        "phone": number,
        "message": message,
        "key": api_key
    })
    
    result = response.json()
    if result.get("success"):
        print(VERDE + "\nMENSAJE ENVIADO" + RESET)
    else:
        print(ROJO + "\nMENSAJE NO ENVIADO" + RESET)
        print(f"Error: {result.get('error', 'Desconocido')}")

if __name__ == "__main__":
    send_sms()
