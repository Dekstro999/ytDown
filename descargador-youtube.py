import tkinter as tk
from tkinter import ttk
from pytube import YouTube
import threading

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
                status_label.config(text=f"Descargando: {yt.title} en resolución {resolution}")
                stream.download()
                status_label.config(text="Descarga completada.")
                progress_var.set(0)
            else:
                status_label.config(text=f"Error: No se encontró una stream con resolución {resolution}.")
        except Exception as e:
            status_label.config(text=f"Error: Ha ocurrido un error: {e}")

    # Iniciar la descarga en un hilo separado para no bloquear la interfaz
    threading.Thread(target=start_download).start()

def progress_callback(stream, chunk, bytes_remaining):
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    percentage_of_completion = (bytes_downloaded / total_size) * 100
    progress_var.set(percentage_of_completion)

# Crear la ventana principal
root = tk.Tk()
root.title("Descargador de YouTube")
root.geometry("800x300")

# Configuración de la fuente
font_large_bold = ('Helvetica', 14, 'bold')

# Crear y colocar los widgets
tk.Label(root, text="URL del video:", font=font_large_bold).grid(row=0, column=0, padx=10, pady=10, sticky='e')
url_entry = tk.Entry(root, width=65, font=('Arial', 12))
url_entry.grid(row=0, column=1, padx=10, pady=10)

tk.Label(root, text="Resolución:", font=font_large_bold).grid(row=1, column=0, padx=10, pady=(10, 0), sticky='e')
resolutions = ['360p', '480p', '720p', '1080p']
resolution_combobox = ttk.Combobox(root, values=resolutions, state='readonly', font=font_large_bold)
resolution_combobox.grid(row=1, column=1, padx=10, pady=(10, 0), sticky='w')

download_button = tk.Button(root, text="Descargar", command=download_video, font=font_large_bold)
download_button.grid(row=2, column=0, columnspan=2, pady=20)

# Barra de progreso
progress_var = tk.DoubleVar()
progress_bar = ttk.Progressbar(root, variable=progress_var, maximum=100)
progress_bar.grid(row=3, column=0, columnspan=2, padx=10, pady=10, sticky='ew')

# Etiqueta de estado
status_label = tk.Label(root, text="", font=('Arial', 12))
status_label.grid(row=4, column=0, columnspan=2, pady=10)

# Iniciar el bucle principal de la interfaz
root.mainloop()
