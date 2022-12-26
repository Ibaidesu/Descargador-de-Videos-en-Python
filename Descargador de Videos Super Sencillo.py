# Descargador De Videos Sencillo MOD por I'm Valkiria2007
from pytube import YouTube
yt = YouTube("XXXXXXXXXXXXXXXXXXXXXXX")

# Obtén el primer stream de video disponible en calidad máxima
video = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()

# Descarga el video en la carpeta actual
video.download()

# También puedes especificar una ruta de descarga diferente
video.download('Aqui Pones Donde quieres que te lo descargue')

print('Tu video ya esta descargado')