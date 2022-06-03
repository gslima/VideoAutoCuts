# VideoAutoCuts
(Pequeno script para automatizar cortes de vídeos)

(Short script to automate video cuts)


Entre os tempos de corte e o nome do corte num arquivo videocuts.txt para ele cospir trechos de vídeos.
Coloque os arquivos de vídeo no mesmo diretório que você está rodando o script, além do arquivo contendo os dados dos cortes.

Se:

o nome do arquivo de vídeo a ser cortado é "Terca-EP01".mp4, você entra uma linha com o prefixo "test"

e

o tempo do corte começa em 00:00:52 e vai até 00:03:10 e tem o título "Definição de cultura",

o formato do arquivo videocuts.txt deve ser:

testTerca-EP01

cut00:00:52|00:03:10|Definição de cultura

(coloque aqui todos os cortes do vídeo)

(após todos os cortes do vídeo, coloque um texto começando novamente com "test", que ele automaticamente irá gerar cortes a partir de outro arquivo de vídeo).

Este script faz uso do programa ffmpeg e o bash do linux. Para instalar, digite, antes de rodar o script.

````
sudo apt update
sudo apt install ffmpeg
````

Para rodar o script:

````
bash gcutter.sh
````
