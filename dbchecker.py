import os
import re
import colorama
from colorama import Fore, Style
from multiprocessing import Pool

# Initialisation de Colorama
colorama.init(autoreset=True)

# Configuration des chemins
search_path = "C:/path/to/your/database"
save_path = "C:/path/to/output/folder"

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_centered(text, color=Fore.RED):
    width = os.get_terminal_size().columns
    print(color + text.center(width))

def search_in_file(args):
    file_path, mot, case_sensitive = args
    mot_regex = re.compile(re.escape(mot), 0 if case_sensitive else re.IGNORECASE)
    with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
        found = False
        result = ""
        for line in f:
            if mot_regex.search(line):
                found = True
                highlighted_line = mot_regex.sub(Fore.GREEN + r'\g<0>' + Fore.RED, line.strip())
                result += f"{highlighted_line}\n"
        return (file_path, result) if found else None

def main():
    while True:
        clear_console()
        print_centered("***************************************************************")
        print_centered("*                    DB String Checker                        *")
        print_centered("*                       Par Vicious                           *")
        print_centered("*                     Discord: wodxx.                         *")
        print_centered("***************************************************************")
        print_centered("*   Recherche rapide de pseudo/mail/IP/uuid/name/tel          *")
        print_centered("*   C'est plus utile si vous avez des base de données.        *")
        print_centered("***************************************************************")
        # Changer la couleur du texte suivant en blanc
        colorama.init(autoreset=False)
        print(Fore.WHITE, end="")

        mots = input("\nEntrez les string à chercher (séparés par un espace) / ex: String1 String2 String3 : ")
        if mots.lower() == 'exit':
            break

        case_sensitive = input("Voulez-vous une recherche sensible à la casse ? (y/n) : ").lower() == 'y'

        filename = input("Entrez le nom du fichier de sortie (sans extension) : ")
        output_file = os.path.join(save_path, f"{filename}.txt")

        tasks = []
        for mot in mots.split():
            for root, _, files in os.walk(search_path):
                for file in files:
                    tasks.append((os.path.join(root, file), mot, case_sensitive))

        with Pool() as pool:
            results = pool.imap_unordered(search_in_file, tasks)
            with open(output_file, 'w', encoding='utf-8') as out_file:
                for result in results:
                    if result:
                        file_path, found_lines = result
                        print(Fore.YELLOW + f"Résultats pour {os.path.basename(file_path)}:\n" + Fore.RED + found_lines)
                        out_file.write(f"Trouvé dans {file_path}\n")
                        out_file.write(found_lines)
                        out_file.write("\n")

        print(Fore.GREEN + f"\nRecherche terminée. Vérifiez les résultats dans {output_file}")

        input("\nAppuyez sur Entrée pour relancer ou tapez 'exit' pour quitter: ")
        if input().lower() == 'exit':
            break

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"Une erreur s'est produite: {e}")
    input("Appuyez sur Entrée pour fermer...")
