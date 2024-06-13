FFTTCC_REV5_FINAL = Código utilizado para a validação da biblioteca FFT. Os dados processados por este programa foram validados utilizando o programa MATLABVALIDACAO.m. Este código capta a leitura do acelerômetro MPU 6050 no eixo X, organiza as informações, processando a FFT e retornando os resultados organizando as 10 maiores amplitudes, apresentando estes dados no Serial Monitor. Processamento realizado através do ESP32 DEV MODULE.

MATLABVALIDACAO.m = Código processa a leitura bruta dos arquivos TXT (300_rpm_valores_brutos, 500_rpm_valores_brutos, 700_rpm_valores_brutos) e apresenta a FFT completa no RANGE entre 0 e 1000Hz,
possibilitando a comparação entre os resultados do código "FFTTCC_REV7_FINAL" e a FFT completa.

INDEX.html = Código processado para gerar a página HTML que apresenta os dados enviados ao banco de dados. Apresenta o gráfico processado da FFT, temperatura ambiente medida pelo sensor GY-521 e %
da bateria que alimenta o CUBECELL (transmissor das informações).

Data.php = Código responsável ste script PHP serve como uma API que fornece dados de sensores de vibração e temperatura coletados pelo Gateway e armazenados 
no banco de dados MYSQL. Os dados são formatados em JSON, permitindo que sejam consumidos por aplicações frontend para visualização e análise dos sinais de vibração e outros parâmetros 
monitorados.
