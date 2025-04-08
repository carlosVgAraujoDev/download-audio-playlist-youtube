# Baixar Playlists do YouTube

Este projeto tem como objetivo facilitar o download do áudio de playlists do YouTube. Ele é composto por um script principal que utiliza funções auxiliares para interagir com a API do YouTube e manipular os dados necessários para o download.


## Requisitos

- Python 3.x
- ffmpeg (para conversão de áudio)

## Instalação

Para instalar as dependências do projeto, você deve ter o Python e o pip instalados em sua máquina. Em seguida, execute o seguinte comando no terminal:

#### 1. Clone o repositório:
```
git clone https://github.com/carlosVgAraujoDev/download-videos-youtube
cd download-audio-playlist-youtube
```

#### 2. Instalação dos pacotes Python necessários:
```
pip install -r requirements.txt
```

#### 3. Configure o ffmpeg:

- Acesse o link com as versões para download: [FFmpeg Download](https://www.gyan.dev/ffmpeg/builds).  
- Baixe o arquivo com nome semelhante a: `ffmpeg-x.x.x-essentials_build.zip`
- Extraia o conteúdo do arquivo `.zip` diretamente para uma pasta no seu sistema (ex.: `C:\ffmpeg`).  
- Adicione o diretório `bin` da pasta extraída à variável de ambiente **PATH** do sistema:
  - Clique com o botão direito em **"Este Computador"** ou **"Meu Computador"** e selecione **"Propriedades"**.
  - Clique em **"Configurações avançadas do sistema"**.
  - Clique em **"Variáveis de ambiente"**.
  - Na seção **"Variáveis do sistema"**, localize a variável `Path`, selecione-a e clique em **"Editar"**.
  - Clique em **"Novo"** e adicione o caminho para o diretório `bin` (ex.: `C:\ffmpeg\bin`).
  - Clique em **"OK"** para fechar todas as janelas.

- Verifique a instalação abrindo o Prompt de Comando e digitando:

```
  ffmpeg -version
```

## Uso

Para utilizar a aplicação, execute o arquivo `main.py`:

```
python main.py
```

## Informações Adicionais

- Certifique-se de ter uma conexão com a internet ativa, pois a aplicação precisa acessar a API do YouTube.
- Este projeto é uma ferramenta de aprendizado e pode ser expandido com novas funcionalidades, como suporte a diferentes formatos de áudio ou vídeo.

Sinta-se à vontade para contribuir com melhorias ou relatar problemas!