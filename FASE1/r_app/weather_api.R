# FarmTech Solutions - Consulta API Meteorológica (Versão Simplificada)
# Versão que funciona melhor em VSCode/RStudio

# Instalar e carregar bibliotecas necessárias
if (!require(httr)) {
  install.packages("httr")
  library(httr)
}
if (!require(jsonlite)) {
  install.packages("jsonlite")
  library(jsonlite)
}

# === CONFIGURAÇÃO DOS PARÂMETROS ===
# Altere estes valores conforme necessário:
LATITUDE <- -15.7942    # Brasília (exemplo)
LONGITUDE <- -47.8822   # Brasília (exemplo)  
DIAS <- 7              # Período de consulta

cat("======================================\n")
cat("    FARMTECH SOLUTIONS - CLIMA API\n")
cat("  Consulta Meteorológica para Agricultura\n")
cat("======================================\n\n")

cat("=== PARÂMETROS DE CONSULTA ===\n")
cat("Latitude:", LATITUDE, "°\n")
cat("Longitude:", LONGITUDE, "°\n")
cat("Período:", DIAS, "dias\n\n")

# Função para consultar API Open Meteo
consultar_clima <- function(latitude, longitude, dias) {
  data_inicio <- Sys.Date()
  data_fim <- Sys.Date() + dias - 1
  
  url <- paste0(
    "https://api.open-meteo.com/v1/forecast?",
    "latitude=", latitude,
    "&longitude=", longitude,
    "&daily=temperature_2m_max,temperature_2m_min,precipitation_sum,windspeed_10m_max,relative_humidity_2m_mean",
    "&timezone=America/Sao_Paulo",
    "&start_date=", data_inicio,
    "&end_date=", data_fim
  )
  
  cat("=== CONSULTANDO API ===\n")
  cat("Aguarde...\n\n")
  
  tryCatch({
    resposta <- GET(url)
    
    if (status_code(resposta) != 200) {
      stop(paste("Erro HTTP:", status_code(resposta)))
    }
    
    dados <- fromJSON(content(resposta, "text", encoding = "UTF-8"))
    return(dados)
    
  }, error = function(e) {
    cat("ERRO na consulta API:", e$message, "\n")
    return(NULL)
  })
}

# Função para exibir dados meteorológicos
exibir_dados_clima <- function(dados) {
  if (is.null(dados)) {
    cat("Não foi possível obter dados meteorológicos.\n")
    return()
  }
  
  cat("=== DADOS METEOROLÓGICOS ===\n")
  cat("Localização:", dados$latitude, "°N,", dados$longitude, "°E\n")
  cat("Timezone:", dados$timezone, "\n")
  cat("Elevação:", dados$elevation, "m\n\n")
  
  # Dados diários
  daily <- dados$daily
  datas <- daily$time
  temp_max <- daily$temperature_2m_max
  temp_min <- daily$temperature_2m_min
  precipitacao <- daily$precipitation_sum
  vento <- daily$windspeed_10m_max
  umidade <- daily$relative_humidity_2m_mean
  
  cat("=== PREVISÃO DIÁRIA ===\n")
  for (i in 1:length(datas)) {
    cat("Data:", datas[i], "\n")
    cat("  Temp. Máxima:", temp_max[i], "°C\n")
    cat("  Temp. Mínima:", temp_min[i], "°C\n")
    cat("  Precipitação:", precipitacao[i], "mm\n")
    cat("  Vento Máximo:", vento[i], "km/h\n")
    cat("  Umidade Média:", umidade[i], "%\n")
    cat("  ----------------------------------------\n")
  }
  
  # Estatísticas resumidas
  cat("\n=== ESTATÍSTICAS DO PERÍODO ===\n")
  cat("Temperatura Máxima Média:", round(mean(temp_max, na.rm = TRUE), 1), "°C\n")
  cat("Temperatura Mínima Média:", round(mean(temp_min, na.rm = TRUE), 1), "°C\n")
  cat("Precipitação Total:", round(sum(precipitacao, na.rm = TRUE), 1), "mm\n")
  cat("Vento Máximo do Período:", round(max(vento, na.rm = TRUE), 1), "km/h\n")
  cat("Umidade Média do Período:", round(mean(umidade, na.rm = TRUE), 1), "%\n")
  
  # Análise agrícola básica
  cat("\n=== ANÁLISE PARA AGRICULTURA ===\n")
  temp_media <- mean(c(temp_max, temp_min), na.rm = TRUE)
  precip_total <- sum(precipitacao, na.rm = TRUE)
  
  if (temp_media > 25) {
    cat("• Temperaturas ALTAS - Ideal para culturas tropicais\n")
  } else if (temp_media > 15) {
    cat("• Temperaturas MODERADAS - Bom para diversas culturas\n")
  } else {
    cat("• Temperaturas BAIXAS - Cuidado com culturas sensíveis ao frio\n")
  }
  
  if (precip_total > 50) {
    cat("• Precipitação ALTA - Boa disponibilidade hídrica\n")
  } else if (precip_total > 10) {
    cat("• Precipitação MODERADA - Pode necessitar irrigação complementar\n")
  } else {
    cat("• Precipitação BAIXA - Irrigação será necessária\n")
  }
  
  cat("\n=== RECOMENDAÇÕES FARMTECH ===\n")
  if (temp_media > 20 && precip_total > 30) {
    cat("✓ Condições FAVORÁVEIS para plantio\n")
  } else if (temp_media < 10) {
    cat("⚠ ATENÇÃO: Risco de geadas - proteger culturas sensíveis\n")
  } else if (precip_total < 5) {
    cat("⚠ ATENÇÃO: Período seco - ativar sistema de irrigação\n")
  }
}

# === EXECUÇÃO PRINCIPAL ===
dados_clima <- consultar_clima(LATITUDE, LONGITUDE, DIAS)
exibir_dados_clima(dados_clima)

cat("\n======================================\n")
cat("Para alterar os parâmetros, modifique as\n")
cat("variáveis LATITUDE, LONGITUDE e DIAS no\n")
cat("início do código e execute novamente.\n")
cat("======================================\n")