import os
import re
from rich import print
from rich.tree import Tree
from rich.console import Console

def orden_natural(texto):
    """Convierte texto en partes numéricas y alfabéticas para ordenar correctamente."""
    return [int(fragmento) if fragmento.isdigit() else fragmento.lower() for fragmento in re.split(r'(\d+)', texto)]

def contar_contenido(archivo):
    """Cuenta caracteres y palabras de un archivo si es accesible."""
    try:
        with open(archivo, "r", encoding="utf-8", errors="ignore") as f:
            contenido = f.read()
            caracteres = len(contenido)
            # Usar expresión regular para contar palabras más precisamente
            palabras = len(re.findall(r'\b\w+\b', contenido))
            return caracteres, palabras
    except (PermissionError, IsADirectoryError):
        return 0, 0
    except Exception as e:
        return 0, 0

def listar_contenido(directorio, arbol, contador):
    """Lista el contenido de un directorio con diseño bonito y cuenta archivos/carpetas."""
    try:
        with os.scandir(directorio) as entries:
            contenido = sorted(entries, key=lambda e: (not e.is_dir(), orden_natural(e.name)))
            for entry in contenido:
                if entry.is_dir():
                    contador["carpetas"] += 1
                    nodo = arbol.add(f"[bold cyan]\U0001F4C1 {entry.name}[/bold cyan]")
                    listar_contenido(entry.path, nodo, contador)
                else:
                    contador["archivos"] += 1
                    caracteres, palabras = contar_contenido(entry.path)
                    contador["caracteres"] += caracteres
                    contador["palabras"] += palabras
                    arbol.add(f"[yellow]\U0001F4C4 {entry.name} ([blue]{caracteres} caracteres[/blue], [green]{palabras} palabras[/green])[/yellow]")
    except PermissionError:
        arbol.add("[red]⛔ Acceso denegado[/red]")
    except FileNotFoundError:
        arbol.add("[red]❌ No encontrado[/red]")
    except Exception as e:
        arbol.add(f"[red]⚠️ Error inesperado: {str(e)}[/red]")

if __name__ == "__main__":
    console = Console()
    ruta_base = input("Ingrese la ruta del directorio a explorar: ").strip()
    while not os.path.exists(ruta_base) or not os.path.isdir(ruta_base):
        print("[bold red]🚨 La ruta ingresada no es válida o no es un directorio. Intente nuevamente.[/bold red]")
        ruta_base = input("Ingrese la ruta del directorio a explorar: ").strip()
    
    arbol = Tree(f"[bold green]\U0001F4C2 {ruta_base}[/bold green]")
    contador = {"archivos": 0, "carpetas": 0, "caracteres": 0, "palabras": 0}
    
    listar_contenido(ruta_base, arbol, contador)
    
    output_file = input("Ingrese el nombre del archivo de salida (default: salida.txt): ") or "salida.txt"
    with open(output_file, "w", encoding="utf-8") as f:
        file_console = Console(file=f)
        silent_mode = input("¿Desea ejecutar en modo silencioso? (s/n): ").strip().lower() == 's'
        
        file_console.print(arbol)
        f.write(f"\n📊 Resumen: {contador['carpetas']} carpetas, {contador['archivos']} archivos, [blue]{contador['caracteres']} caracteres[/blue], [green]{contador['palabras']} palabras[/green] en total.\n")
        
    if not silent_mode:
        console.print(arbol)
        print(f"\n📊 [bold]Resumen:[/bold] {contador['carpetas']} carpetas, {contador['archivos']} archivos, [blue]{contador['caracteres']} caracteres[/blue], [green]{contador['palabras']} palabras[/green] en total.")