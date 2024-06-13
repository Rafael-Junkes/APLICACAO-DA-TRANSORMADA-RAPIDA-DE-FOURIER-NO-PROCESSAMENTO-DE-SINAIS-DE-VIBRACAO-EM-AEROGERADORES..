% Número de amostras
numSamples = 2048;

% Frequência de amostragem em Hz
samplingFreq = 2000;

% Tamanho da FFT (potência de 2)
FFT_N = 1024;

% Carregar os valores de aceleração a partir de um arquivo
accelValues = load('300_rpm_valores_brutos.txt');

% Verifique se o número de valores está correto
if length(accelValues) ~= numSamples
    error('Número incorreto de amostras. O arquivo deve conter exatamente %d valores.', numSamples);
end

% Seleciona os primeiros FFT_N valores para a FFT
fft_input = accelValues(1:FFT_N);

% Calcula a FFT
fft_output = fft(fft_input);

% Estrutura para armazenar frequências e magnitudes
freqMagArray = struct('frequency', [], 'magnitude', []);

% Preenche o array com as frequências e magnitudes
for k = 2:FFT_N/2  % Ignora o primeiro componente (DC)
    mag = abs(fft_output(k)) / FFT_N; % Calcula a magnitude
    frequency = (k-1) * samplingFreq / FFT_N; % Calcula a frequência correspondente
    
    if frequency <= 1000
        freqMagArray(k-1).frequency = frequency;
        freqMagArray(k-1).magnitude = mag * 1000; % Multiplica a magnitude por 1000
    end
end

% Remove entradas vazias da estrutura
freqMagArray = freqMagArray(~cellfun('isempty', {freqMagArray.frequency}));

% Converte a estrutura em tabela para facilitar a manipulação
freqMagTable = struct2table(freqMagArray);

% Plotando a FFT completa com limite de 0 a 1000 Hz
figure;
frequencies = (1:FFT_N-1) * samplingFreq / FFT_N;
magnitudes = abs(fft_output(2:FFT_N)) / FFT_N;

% Limita os dados ao intervalo de 0 a 1000 Hz
limit = frequencies <= 1000;
frequencies = frequencies(limit);
magnitudes = magnitudes(limit);

plot(frequencies, magnitudes);
xlim([0, 1000]); % Limita a apresentação até 1000 Hz
ylim([0, 120]); % Limita o eixo Y até 120
title('FFT Completa');
xlabel('Frequência (Hz)');
ylabel('Magnitude');
grid on;
