PROJETO: APLICAÇÃO DA TRANSORMADA RÁPIDA DE FOURIER NO PROCESSAMENTO DE SINAIS DE VIBRAÇÃO EM AEROGERADORES DE PEQUENO PORTE E INTEGRAÇÃO COM COMUNICAÇÃO LORA

CENTRO UNIVERSITÁRIO CATÓLICA DE SANTA CATARINA

TRABALHO DE CONCLUSÃO DE CURSO EM ENGENHARIA ELÉTRICA

AUTOR 1: AIRTON MATHIAS

AUTOR 2: RAFAEL JUNKES

ORIENTADOR: CARLOS EDUARDO VIANA

FFTTCC_REV6_FINAL = Código utilizado para a validação da biblioteca FFT. Os dados processados por este programa foram validados utilizando o programa MATLABVALIDACAO.m. Este código capta a leitura do acelerômetro MPU 6050 no eixo X, organiza as informações, processando a FFT e retornando os resultados organizando as 10 maiores amplitudes, apresentando estes dados no Serial Monitor. Processamento realizado através do ESP32 DEV MODULE.

FFT_TCC_DEVICE_LORA_FINAL = Programa final responsável pela execução da FFT e envio dos dados via LORA para o Gateway. O programa inicia com a inclusão das bibliotecas "Wire.h" e "FFT.h". Configura o sensor MPU6050 via I2C, lê aceleração e temperatura, e realiza FFT para analisar frequências. No setup, inicializa comunicações e o sensor. No loop, lê temperatura, executa análise de frequências por intervalos, e envia dados via LoRa ao Wireless Stick Lite(V3). Utiliza "bubbleSort" para ordenar e exibir resultados na serial.

FFT_TCC_GATEWAY_LORA_FINAL = Programa final responsável pela captação dos dados enviados por LORA pelo Device. Após a captação das informações, envia via WIFI ao banco de dados MYSQL. Usa bibliotecas como Wire.h, WiFi.h, HTTPClient.h, SPI.h e SX126XLT.h. Inclui funções para enviar dados coletados via HTTP POST, processar pacotes LoRa recebidos e extrair informações do dispositivo. Setup() configura comunicações e LoRa, e loop() monitora e envia dados ao servidor para armazenamento remoto.
 
MATLABVALIDACAO.m = Código processa a leitura bruta dos arquivos TXT (300_rpm_valores_brutos, 500_rpm_valores_brutos, 700_rpm_valores_brutos) e apresenta a FFT completa no RANGE entre 0 e 1000Hz,
possibilitando a comparação entre os resultados do código "FFTTCC_REV7_FINAL" e a FFT completa.

INDEX.html = Código processado para gerar a página HTML que apresenta os dados enviados ao banco de dados. Apresenta o gráfico processado da FFT, temperatura ambiente medida pelo sensor GY-521 e %
da bateria que alimenta o CUBECELL (transmissor das informações).

Data.php = Código responsável ste script PHP serve como uma API que fornece dados de sensores de vibração e temperatura coletados pelo Gateway e armazenados 
no banco de dados MYSQL. Os dados são formatados em JSON, permitindo que sejam consumidos por aplicações frontend para visualização e análise dos sinais de vibração e outros parâmetros 
monitorados.


