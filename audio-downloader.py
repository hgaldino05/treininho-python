import os
import subprocess
import tkinter as tk
from tkinter import filedialog, messagebox, ttk

def download_audio():
    video_url = url_entry.get()
    output_folder = folder_path.get()

    # Configurações para o yt-dlp
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'wav',
            'preferredquality': '192',
        }],
        'outtmpl': os.path.join(output_folder, '%(title)s.%(ext)s'),
    }

    try:
        # Exibe o caminho do arquivo de saída
        print(f"Caminho do arquivo de saída: {ydl_opts['outtmpl']}")

        # Baixa o áudio
        subprocess.run(['yt-dlp', video_url], check=True)

        # Exibe mensagem de sucesso
        messagebox.showinfo("Download Concluído", "Áudio baixado com sucesso!")

    except subprocess.CalledProcessError as e:
        # Exibe mensagem de erro
        messagebox.showerror("Erro", f"Ocorreu um erro durante o download: {str(e)}")

def choose_folder():
    folder = filedialog.askdirectory()
    folder_path.set(folder)

# Cria a GUI
root = tk.Tk()
root.title("YouTube Audio Downloader")

url_label = tk.Label(root, text="URL do vídeo:")
url_label.pack()

url_entry = tk.Entry(root, width=50)
url_entry.pack()

folder_path = tk.StringVar()
folder_button = tk.Button(root, text="Escolher Pasta", command=choose_folder)
folder_button.pack()

download_button = tk.Button(root, text="Baixar Áudio", command=download_audio)
download_button.pack()

root.mainloop()
