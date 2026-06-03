
# Instalar pacotes se faltar
need <- c("dplyr", "readr")
to_install <- need[!need %in% rownames(installed.packages())]
if (length(to_install) > 0) {
  install.packages(to_install, repos = "https://cloud.r-project.org")
}
suppressPackageStartupMessages({
  library(dplyr)
  library(readr)
})

# Caminho do arquivo CSV (alterar)
csv_path <- "../exportcsv15092.csv" 

if (!file.exists(csv_path)) {
  stop(paste("Arquivo não encontrado:", csv_path))
}

# Ler dados
data <- read_csv(csv_path, show_col_types = FALSE)

# Conferir colunas obrigatórias
cols_needed <- c("cultura", "forma", "param1", "param2", "area_m2", "area_ha")
missing <- setdiff(cols_needed, names(data))
if (length(missing) > 0) {
  stop(paste("Colunas faltando:", paste(missing, collapse = ", ")))
}

# Calcular estatísticas
stats_cultura <- data %>%
  group_by(cultura) %>%
  summarise(
    n = n(),
    media_area = mean(area_m2, na.rm = TRUE),
    desvio_area = sd(area_m2, na.rm = TRUE),
    minimo_area = min(area_m2, na.rm = TRUE),
    maximo_area = max(area_m2, na.rm = TRUE),
    total_ha = sum(area_ha, na.rm = TRUE),
    .groups = "drop"
  )

print(stats_cultura)

# Salvar resultados em CSV
write_csv(stats_cultura, "estatisticas_por_cultura.csv")
