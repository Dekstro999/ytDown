import tkinter as tk
from tkinter import ttk, messagebox
from pytube import YouTube

def download_video():
    url = url_entry.get()
    resolution = resolution_combobox.get()
    
    if not url:
        messagebox.showerror("Error", "Por favor, ingrese la URL del video.")
        return
    
    if not resolution:
        messagebox.showerror("Error", "Por favor, seleccione una resolución.")
        return
    
    try:
        yt = YouTube(url)
        stream = yt.streams.filter(progressive=True, file_extension='mp4', res=resolution).first()
        
        if stream:
            messagebox.showinfo("Descargando", f"Descargando: {yt.title} en resolución {resolution}")
            stream.download()
            messagebox.showinfo("Éxito", "Descarga completada.")
        else:
            messagebox.showerror("Error", f"No se encontró una stream con resolución {resolution}.")
    except Exception as e:
        messagebox.showerror("Error", f"Ha ocurrido un error: {e}")

# Crear la ventana principal
root = tk.Tk()
root.title("Descargador de YouTube")
root.geometry("800x300") 

# Configuración de la fuente
font_large_bold = ('Helvetica', 14, 'bold')

# Crear y colocar los widgets
tk.Label(root, text="URL del video:", font=font_large_bold).grid(row=0, column=0, padx=10, pady=10, sticky='e')
url_entry = tk.Entry(root, width=65, font=('Arial',12))
url_entry.grid(row=0, column=1, padx=10, pady=10)

tk.Label(root, text="Resolución:", font=font_large_bold).grid(row=1, column=0, padx=10, pady=(10, 0), sticky='e')
resolutions = ['360p', '480p', '720p', '1080p']  
resolution_combobox = ttk.Combobox(root, values=resolutions, state='readonly', font=font_large_bold)
resolution_combobox.grid(row=1, column=1, padx=10, pady=(10, 0), sticky='w')

download_button = tk.Button(root, text="Descargar", command=download_video, font=font_large_bold)
download_button.grid(row=2, column=0, columnspan=2, pady=20)

# Iniciar el bucle principal de la interfaz
root.mainloop()
