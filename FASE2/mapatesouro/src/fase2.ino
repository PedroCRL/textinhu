#include <Arduino.h>
#include "DHT.h"

// --- MAPEAMENTO DOS PINOS ---
#define DHT_PIN 4
#define LDR_PIN 34
#define BTN_N_PIN 25
#define BTN_P_PIN 26
#define BTN_K_PIN 27
#define RELE_PIN 13
#define LED_STATUS_PIN 12

// --- CONFIGURAÇÃO DO SENSOR DHT ---
#define DHT_TYPE DHT22
DHT dht(DHT_PIN, DHT_TYPE);

// --- VARIÁVEIS GLOBAIS ---
unsigned long previousMillis = 0;
const long interval = 500;
int ledState = LOW;
unsigned long lastLogTime = 0;
const long logInterval = 5000; // Intervalo de log (5 segundos)
unsigned long lastResumoTime = 0;
const long resumoInterval = 30000; // Intervalo de resumo (30 segundos)
int contadorRegistros = 0;

// Array para armazenar dados (últimos 50 registros)
#define MAX_REGISTROS 50
struct DadosSensor {
  unsigned long timestamp;
  float umidade;
  float ph;
  bool n;
  bool p;
  bool k;
  bool irrigando;
};
DadosSensor registros[MAX_REGISTROS];
int indiceAtual = 0;

// --- FUNÇÕES DE GERENCIAMENTO CSV ---
void adicionarRegistro(float umidade, float ph, bool n, bool p, bool k, bool irrigando) {
  unsigned long timestamp = millis() / 1000; // Timestamp em segundos
  
  // Armazena no array circular
  registros[indiceAtual].timestamp = timestamp;
  registros[indiceAtual].umidade = umidade;
  registros[indiceAtual].ph = ph;
  registros[indiceAtual].n = n;
  registros[indiceAtual].p = p;
  registros[indiceAtual].k = k;
  registros[indiceAtual].irrigando = irrigando;
  
  indiceAtual = (indiceAtual + 1) % MAX_REGISTROS;
  contadorRegistros++;
  
  // Envia via Serial
  sendCSVToSerial(umidade, ph, n, p, k, irrigando, timestamp);
}

void sendCSVToSerial(float umidade, float ph, bool n, bool p, bool k, bool irrigando, unsigned long timestamp) {
  // Envia com marcador especial para o script Python identificar
  Serial.print("CSV_DATA:");
  Serial.print(timestamp);
  Serial.print(",");
  Serial.print(umidade, 2);
  Serial.print(",");
  Serial.print(ph, 2);
  Serial.print(",");
  Serial.print(n);
  Serial.print(",");
  Serial.print(p);
  Serial.print(",");
  Serial.print(k);
  Serial.print(",");
  Serial.println(irrigando);
}

void exibirResumo() {
  Serial.println("\n");
  Serial.println("========================================");
  Serial.println("       RESUMO DOS DADOS COLETADOS      ");
  Serial.println("========================================");
  Serial.println("Timestamp,Umidade(%),pH,Nitrogenio,Fosforo,Potassio,Irrigando");
  Serial.println("----------------------------------------");
  
  int totalParaExibir = min(contadorRegistros, MAX_REGISTROS);
  int inicio = 0;
  
  // Se temos mais registros que o máximo, começamos do mais antigo no array circular
  if (contadorRegistros > MAX_REGISTROS) {
    inicio = indiceAtual;
  }
  
  for (int i = 0; i < totalParaExibir; i++) {
    int idx = (inicio + i) % MAX_REGISTROS;
    Serial.print("CSV_DATA:");
    Serial.print(registros[idx].timestamp);
    Serial.print(",");
    Serial.print(registros[idx].umidade, 2);
    Serial.print(",");
    Serial.print(registros[idx].ph, 2);
    Serial.print(",");
    Serial.print(registros[idx].n);
    Serial.print(",");
    Serial.print(registros[idx].p);
    Serial.print(",");
    Serial.print(registros[idx].k);
    Serial.print(",");
    Serial.println(registros[idx].irrigando);
  }
  
  Serial.println("----------------------------------------");
  Serial.print("Total de registros coletados: ");
  Serial.println(contadorRegistros);
  Serial.print("Exibindo últimos: ");
  Serial.println(totalParaExibir);
  Serial.println("========================================");
  Serial.println("\n");
}

void setup() {
  // CHECKPOINT 1
  Serial.begin(115200);
  delay(1000); // Tempo para o monitor serial conectar
  Serial.println("--- CHECKPOINT 1: Setup iniciado ---");
  Serial.println("Sistema de Logging CSV - Sem SPIFFS");
  Serial.println("Resumo a cada 30 segundos");

  // Inicia o sensor DHT
  //dht.begin();
  
  // CHECKPOINT 2
  Serial.println("--- CHECKPOINT 2: DHT.begin() executado ---");

  pinMode(LDR_PIN, INPUT);
  pinMode(BTN_N_PIN, INPUT);
  pinMode(BTN_P_PIN, INPUT);
  pinMode(BTN_K_PIN, INPUT);
  pinMode(RELE_PIN, OUTPUT);
  pinMode(LED_STATUS_PIN, OUTPUT);

  digitalWrite(RELE_PIN, LOW);
  digitalWrite(LED_STATUS_PIN, LOW);

  // CHECKPOINT 3
  Serial.println("--- CHECKPOINT 3: Setup completo. Entrando no loop... ---");
  Serial.println("\nTimestamp,Umidade(%),pH,Nitrogenio,Fosforo,Potassio,Irrigando");
  Serial.println("-------------------------------------------------------------------");
}

void loop() {
  // CHECKPOINT 4
  Serial.println("--- CHECKPOINT 4: Loop iniciado ---");

  float umidade = dht.readHumidity();
  
  if (isnan(umidade)) {
    Serial.println("!!! ERRO: Falha ao ler o sensor DHT. Verificando novamente...");
    delay(1000); // Espera um segundo antes de tentar de novo
    return;
  }

  int valorLDR = analogRead(LDR_PIN);
  bool n_pressionado = (digitalRead(BTN_N_PIN) == HIGH);
  bool p_pressionado = (digitalRead(BTN_P_PIN) == HIGH);
  bool k_pressionado = (digitalRead(BTN_K_PIN) == HIGH);
  float ph = (valorLDR / 4095.0) * 14.0;

  bool deveIrrigar = (umidade < 50.0 && ph > 6.0 && ph < 7.0 && n_pressionado);

  if (deveIrrigar) {
    digitalWrite(RELE_PIN, HIGH);
    unsigned long currentMillis = millis();
    if (currentMillis - previousMillis >= interval) {
      previousMillis = currentMillis;
      ledState = !ledState;
      digitalWrite(LED_STATUS_PIN, ledState);
    }
  } else {
    digitalWrite(RELE_PIN, LOW);
    digitalWrite(LED_STATUS_PIN, LOW);
    ledState = LOW;
  }

// --- SEÇÃO PRINT
Serial.print("DADOS: Umidade: " + String(umidade) + "%");
Serial.print(" | pH: " + String(ph));
Serial.print(" | N: " + String(n_pressionado));
Serial.print(" | P: " + String(p_pressionado));
Serial.print(" | K: " + String(k_pressionado));
Serial.print(" | Irrigando: " + String(deveIrrigar));
Serial.println(" --- Fim do Loop ---");

  // Adiciona registro a cada logInterval
  unsigned long currentTime = millis();
  if (currentTime - lastLogTime >= logInterval) {
    lastLogTime = currentTime;
    adicionarRegistro(umidade, ph, n_pressionado, p_pressionado, k_pressionado, deveIrrigar);
  }

  // Exibe resumo a cada 30 segundos
  if (currentTime - lastResumoTime >= resumoInterval) {
    lastResumoTime = currentTime;
    exibirResumo();
  }

  delay(5000);
}
