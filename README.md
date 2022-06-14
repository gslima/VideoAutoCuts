# VideoAutoCuts
(Pequeno script para automatizar cortes de vídeos)

(Short script to automate video cuts)


Entre os tempos de corte e o nome do corte num arquivo videocuts.txt para ele cuspir trechos de vídeos.
Coloque os arquivos de vídeo no mesmo diretório que você está rodando o script, além do arquivo contendo os dados dos cortes.

Se:

o nome do arquivo de vídeo a ser cortado é "Terca-EP01".mp4, você entra uma linha com o prefixo "test"

e

o tempo do corte começa em 00:00:52 e vai até 00:03:10 e tem o título "Tópico 1",

o formato do arquivo **videocuts.txt** deve ser (p.ex.):

~~~
testTercaEP01
cut00:00:52|00:03:10|Tópico 1
cut00:03:10|00:13:10|Tópico 2
testQuartEP02
cut00:00:52|00:03:10|Tópico 3
cut00:03:10|00:13:10|Tópico 4

~~~

Coloque no **"videocuts.txt"** todos os cortes do vídeo. Após todos os cortes do vídeo, coloque um texto começando novamente com "test",
que ele automaticamente irá gerar cortes a partir de outro arquivo de vídeo.

~~~
(testNomeDoVideo)
(cutTempoDeInício|TempoDeFim|NomeDoCorte)
~~~

Este script faz uso do programa ffmpeg e o python do Linux. Para instalar, digite, antes de rodar o script.

````
sudo apt update
sudo apt install ffmpeg
````

Para rodar o script:

````
python3 gcutter.py
````
