/*============================================================================
PROJETO: APLICAÇÃO DA TRANSORMADA RÁPIDA DE FOURIER NO 
PROCESSAMENTO DE SINAIS DE VIBRAÇÃO EM AEROGERADORES 
DE PEQUENO PORTE E INTEGRAÇÃO COM COMUNICAÇÃO LORA
AUTOR 1: AIRTON MATHIAS
AUTOR 2: RAFAEL JUNKES
ORIENTADOR: CARLOS EDUARDO VIANA
MODELO MICROPROCESSADPOR: ESP-WROOM-32-DEVKIT1
IDE: Arduino IDE 2.3.1
============================================================================*/

#include <Wire.h>
#include "MPU6050.h" //https://github.com/ElectronicCats/mpu6050
 
MPU6050 mpu;
 
#define SAMPLES 256 // Número de amostras para o vetor de armazenamento
#define SAMPLING_FREQ 1000 // Frequência de amostragem em Hz
 
void setup() {
Serial.begin(115200);
 Wire.begin();
 
Serial.println("Initializing MPU6050...");
 mpu.initialize();
Serial.println("MPU6050 initialized successfully");
}
 
void loop() {
 // Ler os dados do acelerômetro
 int16_t ax_raw, ay_raw, az_raw;
mpu.getAcceleration(&ax_raw, &ay_raw, &az_raw);
 
 // Converter para unidades de g
 double ax_g = (double)ax_raw / 16384.0;
 double ay_g = (double)ay_raw / 16384.0;
 double az_g = (double)az_raw / 16384.0;
 
 // Armazenar os dados em vetores
 static double ax[SAMPLES];
 static double ay[SAMPLES];
 static double az[SAMPLES];
 
 for (int i = SAMPLES - 1; i > 0; i--) {
   ax[i] = ax[i - 1];
   ay[i] = ay[i - 1];
   az[i] = az[i - 1];
 }
 ax[0] = ax_g*1000;
 ay[0] = ay_g;
 az[0] = az_g;
 
 // Imprimir os valores dos vetores X, Y e Z no Serial Plotter
//Serial.print("X: ");
 Serial.println(ax[0]);
//Serial.print("\tY: ");
//Serial.print(ay[0]);
//Serial.print("\tZ: ");
//Serial.println(az[0]);
 
  delayMicroseconds(500);  ; // Ajuste conforme necessário para a taxa de atualização desejada
}
