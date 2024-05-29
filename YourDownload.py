import tkinter as tk
from tkinter import ttk
from pytube import YouTube
import threading
import os

# Verificar si la carpeta DVideos existe, si no, crearla
videos_folder = os.path.join(os.getcwd(), "DVideos")
if not os.path.exists(videos_folder):
    os.makedirs(videos_folder)

def download_video():
    url = url_entry.get()
    resolution = resolution_combobox.get()
    
    if not url:
        status_label.config(text="Error: Por favor, ingrese la URL del video.")
        return
    
    if not resolution:
        status_label.config(text="Error: Por favor, seleccione una resolución.")
        return
    
    def start_download():
        try:
            yt = YouTube(url, on_progress_callback=progress_callback)
            stream = yt.streams.filter(progressive=True, file_extension='mp4', res=resolution).first()

            if stream:
                global filepath
                filepath = os.path.join(videos_folder, yt.title + ".mp4")  # Guardar en la carpeta DVideos
                stream.download(output_path=videos_folder)
                status_label.config(text=f"Descargando: {yt.title} en resolución {resolution}")
                status_label.after(1000, check_download_completion)  # Comprueba si la descarga se ha completado
            else:
                status_label.config(text=f"Error: No se encontró una stream con resolución {resolution}.")
        except Exception as e:
            status_label.config(text=f"Error: ERROR 404 - {e}")


    threading.Thread(target=start_download).start()  # Iniciar la descarga en un hilo separado

def check_download_completion():
    if os.path.exists(filepath):
        status_label.config(text="Descarga completada.")
        progress_var.set(0)
        open_folder_button.config(state=tk.NORMAL)  
    else:
        status_label.after(1000, check_download_completion)

def progress_callback(stream, chunk, bytes_remaining):
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    percentage_of_completion = (bytes_downloaded / total_size) * 100
    progress_var.set(percentage_of_completion)

def open_download_folder():
    os.system(f'explorer {os.path.realpath(videos_folder)}')


# Crear la ventana principal
root = tk.Tk()
root.title("YourDownload 0.5")

# Establecer el ícono de la ventana
icon_path = os.path.join(os.getcwd(), "icon.ico")
root.iconbitmap(icon_path)

# Establecer la imagen de fondo
background_image = tk.PhotoImage(file=os.path.join(os.getcwd(), "flor.png"))
background_label = tk.Label(root, image=background_image)
background_label.place(relx=0.5, rely=0.5, anchor="center", relwidth=1, relheight=1)  # Modificado para ajustar a la ventana

# Limitar el tamaño mínimo de la ventana
root.minsize(800, 350)

# Crear y colocar los widgets
# Etiqueta "URL del video"
label_url = tk.Label(root, text="URL del video:", font=('Helvetica', 14, 'bold'), fg="black")
label_url.place(x=20, y=20)

url_entry = tk.Entry(root, width=65, font=('Arial', 12))
url_entry.place(x=170, y=20)

# Etiqueta "Resolución"
label_resolution = tk.Label(root, text="Resolución:", font=('Helvetica', 14, 'bold'), fg="black")
label_resolution.place(x=20, y=60)

resolutions = ['360p', '480p', '720p', '1080p']
resolution_combobox = ttk.Combobox(root, values=resolutions, state='readonly', font=('Helvetica', 14, 'bold'))
resolution_combobox.place(x=170, y=60)

download_button = tk.Button(root, text="Descargar", command=download_video, font=('Helvetica', 14, 'bold'))
download_button.place(relx=0.5, rely=0.4, anchor="center")

# Botón para buscar el video
open_folder_button = tk.Button(root, text="Buscar video", command=open_download_folder, font=('Helvetica', 14, 'bold'))
open_folder_button.place(relx=0.5, rely=0.6, anchor="center")

# Barra de progreso
progress_var = tk.DoubleVar()
progress_bar = ttk.Progressbar(root, variable=progress_var, maximum=100)
progress_bar.place(relx=0.5, rely=0.8, anchor="center", relwidth=0.9)

# Etiqueta de estado
status_label = tk.Label(root, text="", font=('Arial', 12))
status_label.place(relx=0.5, rely=0.9, anchor="center")

root.mainloop()
