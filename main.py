from pytubefix import YouTube
from pytubefix import Playlist
from pydub import AudioSegment
import os

PLAYLIST_URL = 'URL_DA_PLAYLIST_AQUI'  # Substitua pela URL da sua playlist
# Exemplo: 'https://www.youtube.com/playlist?list=PL077764AA439803F2'
DOWNLOADS_PATH = 'downloads'
MP3_PATH = 'mp3'

os.makedirs(DOWNLOADS_PATH, exist_ok=True)
os.makedirs(MP3_PATH, exist_ok=True)

playlist = Playlist(PLAYLIST_URL)
playlist._video_regex = r"\"url\":\"(/watch\?v=[\w-]*)"
videos_playlist = playlist.video_urls

def download_video(link):
    youtube_object = YouTube(link)
    youtube_object = youtube_object.streams.get_audio_only()
    try:
        youtube_object.download(output_path="downloads")
    except:
        print("Ocorreu um erro")
    print("Download concluído com sucesso")
    
    
def converte_arquivos_para_mp3(caminho_arquivos, caminho_destino_mp3):
    for filename in os.listdir(caminho_arquivos):
        if filename.endswith(".m4a"):
            m4a_path = os.path.join(caminho_arquivos, filename)
            mp3_filename = os.path.splitext(filename)[0] + ".mp3"
            mp3_path = os.path.join(caminho_destino_mp3, mp3_filename)

            try:
                print(f"Convertendo: {filename} → {mp3_filename}")
                audio = AudioSegment.from_file(m4a_path, format="m4a")
                audio.export(mp3_path, format="mp3")
                print("✔️ Conversão concluída\n")
            except Exception as e:
                print(f"❌ Erro ao converter {filename}: {e}")
  
    
for video in videos_playlist:
  download_video(video)

converte_arquivos_para_mp3(DOWNLOADS_PATH, MP3_PATH)