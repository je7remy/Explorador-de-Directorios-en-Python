# Explorador de Directorios en Python

Este script en Python permite explorar un directorio especificado por el usuario y mostrar su contenido en un árbol estructurado utilizando la biblioteca `rich`. También cuenta el número de archivos y carpetas, así como el total de caracteres y palabras en los archivos de texto.

## Características

- Explora recursivamente el contenido de un directorio.
- Muestra archivos y carpetas en un formato de árbol visualmente atractivo.
- Ordena los nombres de archivos y carpetas en orden natural.
- Cuenta el número de caracteres y palabras en archivos de texto.
- Permite guardar la salida en un archivo de texto.
- Opción para ejecutar en modo silencioso (sin mostrar la salida en la terminal).

## Requisitos

Este script requiere Python 3 y la biblioteca `rich`, que puede instalarse con:

```sh
pip install rich
```

## Uso

Ejecuta el script en la terminal:

```sh
python script.py
```

El programa solicitará la ruta del directorio a explorar y verificará su validez. Luego generará y mostrará la estructura del directorio en la consola y ofrecerá la opción de guardar la salida en un archivo.

### Opciones interactivas
- **Ruta del directorio**: Se debe proporcionar una ruta válida.
- **Archivo de salida**: Nombre del archivo donde se guardará la salida (por defecto `salida.txt`).
- **Modo silencioso**: Si se elige `s`, la salida no se mostrará en la consola.

## Ejemplo de Salida

```plaintext
📂 /ruta/del/directorio
 ├── 📁 Subcarpeta1
 │   ├── 📄 archivo1.txt (500 caracteres, 100 palabras)
 │   ├── 📄 archivo2.log (300 caracteres, 50 palabras)
 ├── 📁 Subcarpeta2
 │   ├── 📄 imagen.png
 ├── 📄 documento.pdf

📊 Resumen: 2 carpetas, 4 archivos, 800 caracteres, 150 palabras en total.
```

## Autor

Este script fue desarrollado para facilitar la exploración de directorios y el análisis básico de archivos de texto en Python.

## Licencia

Este proyecto está bajo la licencia MIT.

