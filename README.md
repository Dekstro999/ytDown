# Descargador de YouTube

Este proyecto es una aplicación de escritorio desarrollada en Python que permite descargar videos de YouTube en diferentes resoluciones. Utiliza la biblioteca `pytube` para la descarga de videos y `tkinter` para la interfaz gráfica de usuario (GUI).

## Opciones de Ejecución

### Opción 1: Ejecutar el Ejecutable Empaquetado

Si solo quieres usar la aplicación sin modificar el código, puedes descargar el ejecutable empaquetado.

#### Requisitos

No necesitas instalar Python ni ninguna biblioteca adicional para ejecutar esta aplicación. Todo lo necesario está incluido en el ejecutable empaquetado.

#### Instalación y Ejecución

1. **Descargar el archivo comprimido**

   Descarga el archivo `proto0.4.rar` desde el enlace proporcionado.

2. **Descomprimir el archivo**

   Usa una herramienta de descompresión (como WinRAR, 7-Zip, etc.) para extraer el contenido del archivo `proto0.4.rar`.

3. **Ejecutar la aplicación**

   Navega hasta la carpeta donde descomprimiste el contenido del archivo `proto0.4.rar` y haz doble clic en el archivo `YourDownload.exe` para iniciar la aplicación.

### Opción 2: Clonar el Repositorio y Ejecutar desde el Código Fuente

Si prefieres clonar el repositorio y modificar el código, sigue las instrucciones a continuación.

#### Requisitos

Para ejecutar este proyecto desde el código fuente, necesitarás tener instalados los siguientes componentes:

- Python 3.6 o superior
- Bibliotecas de Python:
  - `pytube`
  - `tkinter` (viene preinstalada con Python)
  - `ttk` (parte de `tkinter`)

#### Instalación

1. **Clonar el repositorio**

   ```bash
   git clone https://github.com/tu-usuario/descargador-youtube.git
   cd descargador-youtube
   ```

2. **Crear y activar un entorno virtual (opcional pero recomendado)**

   ```bash
   python -m venv venv
   source venv/bin/activate  # En Windows usa `venv\Scripts\activate`
   ```

3. **Instalar las dependencias**

   ```bash
   pip install pytube
   ```

#### Ejecución

Para ejecutar la aplicación desde el código fuente, simplemente corre el script principal:

```bash
python YourDownload.py
```

## Uso

1. **Interfaz de usuario**

   - **URL del video**: Introduce la URL del video de YouTube que deseas descargar.
   - **Resolución**: Selecciona la resolución deseada del video (360p, 480p, 720p, 1080p).
   - **Botón de descarga**: Presiona el botón "Descargar" para iniciar la descarga.

2. **Progreso de la descarga**

   - La barra de progreso se actualizará para mostrar el avance de la descarga.
   - Los mensajes de estado aparecerán en la parte inferior de la ventana, indicando el estado actual del proceso (descargando, error, descarga completada).

## Contribución

Si deseas contribuir a este proyecto, por favor sigue estos pasos:

1. Haz un fork del repositorio.
2. Crea una nueva rama (`git checkout -b feature/nueva-funcionalidad`).
3. Realiza los cambios necesarios y haz commit (`git commit -am 'Añadir nueva funcionalidad'`).
4. Sube los cambios a tu repositorio (`git push origin feature/nueva-funcionalidad`).
5. Abre un Pull Request en GitHub.

## Acerca de

Este proyecto es de código abierto y libre de pirañas.

## Licencia

Este proyecto está bajo la licencia MIT. Para más detalles, consulta el archivo `LICENSE`.
```

Este README proporciona instrucciones tanto para usuarios que solo quieren ejecutar la aplicación empaquetada como para desarrolladores que desean clonar el repositorio y modificar el código fuente.
