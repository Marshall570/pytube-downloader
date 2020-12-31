import os
import platform
import subprocess
import sys


def setup_downloader():
    try:
        subprocess.check_call(
            [
                sys.executable,
                '-m',
                'pip',
                'install',
                'youtube-dl',
                '-q'
            ]
        )

        print('-'*20 + ' PY_DOWNLOADER ' + '-'*20)

        download_path = os.path.expanduser('~') + '/Downloads/'
        
        link = input('Insira o link do vídeo/playlist: ')

        if link.find('&list') != -1:
            download_path += '%(playlist)s/%(playlist_index)s - %(title)s.%(ext)s'
        else:
            download_path += '%(title)s.%(ext)s'

        if platform.system().startswith('Win'):
            download_path.replace('/', '\\')

        print('\n1) Vídeo + Áudio\n2) Apenas Áudio')
        option = int(input('Insira a opção do download: '))

        while option not in (1, 2):
            option = int(input('Insira uma opção do download válida: '))

        if option == 1:
            youtube_dl_options = {
                'quiet': True,
                'format': 'bestvideo+bestaudio',
                'outtmpl': download_path,
            }
        else:
            youtube_dl_options = {
                'quiet': True,
                'format': 'bestaudio',
                'outtmpl': download_path,
                'postprocessors': [{
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'mp3',
                    'preferredquality': '192'
                }],
            }

        print('\nBaixando arquivos...')
        start_downloader(youtube_dl_options, link)

    except Exception as e:
        print(e)


def start_downloader(options, link):
    import youtube_dl

    try:
        with youtube_dl.YoutubeDL(options) as downloader:
            downloader.download([link.strip()])
    except Exception as e:
        print(e)
        quit()
    finally:
        print('Download efetuado com sucesso na pasta <Downloads>!')

    print('\nPressione enter para encerrar o programa...')


setup_downloader()
