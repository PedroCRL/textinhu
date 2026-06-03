# ViniciusLisboaPorto_RM561406_fase2_cap7
#ViniciusdeSantanaGama_RM566672_fase2_cap7
#PedroCarvalhoRochaLima_RM567330_fase2_cap7
#MarlonPaulinoMarinho_RM566793_fase2_cap7
#DaniloMarquesDantas_RM567583_fase2_cap7

# ============================================================================
# ANÁLISE EXPLORATÓRIA - PRODUTIVIDADE DE SOJA NO BRASIL
# Trabalho: Estatística Descritiva Aplicada ao Agronegócio
# ============================================================================

# Carregar bibliotecas necessárias
library(readxl)
library(ggplot2)
library(dplyr)

# ============================================================================
# 1. IMPORTAÇÃO E PREPARAÇÃO DOS DADOS
# ============================================================================

# Ler arquivo Excel
dados <- read_excel("base_agronegocio_soja_2024.xlsx")

# CONVERTER de data para número e AJUSTAR
dados$Produtividade_kg_ha <- as.numeric(dados$Produtividade_kg_ha) / 14516966.4
dados$Num_Produtores <- as.numeric(dados$Num_Produtores)

# Converter Nivel_Tecnologico para fator ordenado
dados$Nivel_Tecnologico <- factor(dados$Nivel_Tecnologico,
                                  levels = c("Médio", "Alto", "Muito Alto"),
                                  ordered = TRUE)

# Verificar estrutura
cat("\n==========================================\n")
cat("ESTRUTURA DOS DADOS\n")
cat("==========================================\n\n")
str(dados)

cat("\n==========================================\n")
cat("PRIMEIRAS LINHAS\n")
cat("==========================================\n\n")
print(head(dados))

# ============================================================================
# 2. ANÁLISE EXPLORATÓRIA - PRODUTIVIDADE (Variável Quantitativa Contínua)
# ============================================================================

cat("\n==========================================\n")
cat("ANÁLISE DA PRODUTIVIDADE DE SOJA (kg/ha)\n")
cat("==========================================\n\n")

# ---------------------------------------------------------------------------
# 2.1 MEDIDAS DE TENDÊNCIA CENTRAL
# ---------------------------------------------------------------------------

media_prod <- mean(dados$Produtividade_kg_ha)
mediana_prod <- median(dados$Produtividade_kg_ha)

cat("MEDIDAS DE TENDÊNCIA CENTRAL:\n")
cat(sprintf("Média: %.2f kg/ha\n", media_prod))
cat(sprintf("Mediana: %.2f kg/ha\n\n", mediana_prod))

# ---------------------------------------------------------------------------
# 2.2 MEDIDAS DE DISPERSÃO
# ---------------------------------------------------------------------------

variancia_prod <- var(dados$Produtividade_kg_ha)
desvio_padrao_prod <- sd(dados$Produtividade_kg_ha)
coef_variacao_prod <- (desvio_padrao_prod / media_prod) * 100
amplitude_prod <- max(dados$Produtividade_kg_ha) - min(dados$Produtividade_kg_ha)

cat("MEDIDAS DE DISPERSÃO:\n")
cat(sprintf("Variância: %.2f\n", variancia_prod))
cat(sprintf("Desvio Padrão: %.2f kg/ha\n", desvio_padrao_prod))
cat(sprintf("Coeficiente de Variação: %.2f%%\n", coef_variacao_prod))
cat(sprintf("Amplitude Total: %.2f kg/ha\n", amplitude_prod))
cat(sprintf("Valor Mínimo: %.2f kg/ha\n", min(dados$Produtividade_kg_ha)))
cat(sprintf("Valor Máximo: %.2f kg/ha\n\n", max(dados$Produtividade_kg_ha)))

# ---------------------------------------------------------------------------
# 2.3 MEDIDAS SEPARATRIZES
# ---------------------------------------------------------------------------

quartis_prod <- quantile(dados$Produtividade_kg_ha, probs = c(0.25, 0.5, 0.75))
decis_prod <- quantile(dados$Produtividade_kg_ha, probs = seq(0.1, 0.9, 0.1))

cat("MEDIDAS SEPARATRIZES:\n")
cat("\nQuartis:\n")
print(quartis_prod)

cat("\nDecis:\n")
print(decis_prod)

AIQ <- IQR(dados$Produtividade_kg_ha)
cat(sprintf("\nAmplitude Interquartílica (AIQ): %.2f kg/ha\n\n", AIQ))

# ---------------------------------------------------------------------------
# 2.4 ANÁLISE GRÁFICA - PRODUTIVIDADE
# ---------------------------------------------------------------------------

# Histograma com densidade
hist_prod <- ggplot(dados, aes(x = Produtividade_kg_ha)) +
  geom_histogram(aes(y = after_stat(density)), 
                 bins = 8, 
                 fill = "#2E7D32", 
                 color = "white", 
                 alpha = 0.7) +
  geom_density(color = "#1B5E20", linewidth = 1.2) +
  geom_vline(xintercept = media_prod, color = "red", linetype = "dashed", linewidth = 1) +
  geom_vline(xintercept = mediana_prod, color = "blue", linetype = "dashed", linewidth = 1) +
  labs(title = "Distribuição da Produtividade de Soja",
       subtitle = "Principais Municípios Produtores do Brasil",
       x = "Produtividade (kg/ha)",
       y = "Densidade",
       caption = "Linha vermelha: Média | Linha azul: Mediana") +
  theme_minimal() +
  theme(plot.title = element_text(face = "bold", size = 14))

print(hist_prod)

# Boxplot
boxplot_prod <- ggplot(dados, aes(x = "", y = Produtividade_kg_ha)) +
  geom_boxplot(fill = "#4CAF50", 
               color = "#1B5E20", 
               alpha = 0.7,
               outlier.color = "red",
               outlier.size = 3) +
  stat_summary(fun = mean, geom = "point", shape = 23, size = 4, fill = "red") +
  labs(title = "Boxplot da Produtividade de Soja",
       subtitle = "Análise de Dispersão e Identificação de Outliers",
       x = "",
       y = "Produtividade (kg/ha)",
       caption = "Losango vermelho: Média") +
  theme_minimal() +
  theme(plot.title = element_text(face = "bold", size = 14))

# ============================================================================
# 3. ANÁLISE GRÁFICA - NÍVEL TECNOLÓGICO (Variável Qualitativa Ordinal)
# ============================================================================

cat("\n==========================================\n")
cat("ANÁLISE DO NÍVEL TECNOLÓGICO\n")
cat("==========================================\n\n")

# Tabela de frequências
freq_tec <- table(dados$Nivel_Tecnologico)
freq_rel <- prop.table(freq_tec) * 100

cat("DISTRIBUIÇÃO DE FREQUÊNCIAS:\n")
print(freq_tec)
cat("\nFREQUÊNCIAS RELATIVAS (%):\n")
print(round(freq_rel, 2))

# Gráfico de barras
barplot_tec <- ggplot(dados, aes(x = Nivel_Tecnologico, fill = Nivel_Tecnologico)) +
  geom_bar(alpha = 0.8) +
  geom_text(stat = 'count', aes(label = after_stat(count)), 
            vjust = -0.5, size = 5, fontface = "bold") +
  scale_fill_manual(values = c("Médio" = "#FF9800",
                               "Alto" = "#4CAF50",
                               "Muito Alto" = "#1976D2")) +
  labs(title = "Distribuição dos Municípios por Nível Tecnológico",
       subtitle = "Classificação baseada em adoção de tecnologias agrícolas",
       x = "Nível Tecnológico",
       y = "Frequência Absoluta",
       fill = "Nível") +
  theme_minimal() +
  theme(plot.title = element_text(face = "bold", size = 14),
        legend.position = "none",
        axis.text.x = element_text(face = "bold", size = 11))

print(barplot_tec)

# Boxplot comparativo
boxplot_comp <- ggplot(dados, aes(x = Nivel_Tecnologico, 
                                  y = Produtividade_kg_ha,
                                  fill = Nivel_Tecnologico)) +
  geom_boxplot(alpha = 0.7) +
  stat_summary(fun = mean, geom = "point", shape = 23, size = 4, 
               fill = "white", color = "black") +
  scale_fill_manual(values = c("Médio" = "#FF9800",
                               "Alto" = "#4CAF50",
                               "Muito Alto" = "#1976D2")) +
  labs(title = "Produtividade de Soja por Nível Tecnológico",
       subtitle = "Comparação entre categorias tecnológicas",
       x = "Nível Tecnológico",
       y = "Produtividade (kg/ha)",
       caption = "Losango branco: Média por categoria") +
  theme_minimal() +
  theme(plot.title = element_text(face = "bold", size = 14),
        legend.position = "none",
        axis.text.x = element_text(face = "bold", size = 11))

print(boxplot_comp)

# ============================================================================
# 4. ANÁLISE CRUZADA
# ============================================================================

cat("\n==========================================\n")
cat("ESTATÍSTICAS POR NÍVEL TECNOLÓGICO\n")
cat("==========================================\n\n")

analise_cruzada <- dados %>%
  group_by(Nivel_Tecnologico) %>%
  summarise(
    N_Municipios = n(),
    Media_Produtividade = mean(Produtividade_kg_ha),
    Mediana_Produtividade = median(Produtividade_kg_ha),
    DP_Produtividade = sd(Produtividade_kg_ha),
    Min_Produtividade = min(Produtividade_kg_ha),
    Max_Produtividade = max(Produtividade_kg_ha)
  ) %>%
  arrange(desc(Media_Produtividade))

print(analise_cruzada)

# ============================================================================
# FIM DA ANÁLISE
# ============================================================================

cat("\n==========================================\n")
cat("ANÁLISE CONCLUÍDA COM SUCESSO!\n")
cat("==========================================\n\n")
cat("FIAP - Análise de Dados do Agronegócio\n")