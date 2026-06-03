-- Exibe todos os registros e colunas da tabela
SELECT * 
FROM tabelasensor;

-- Mostra apenas as colunas de tempo, umidade e pH
SELECT TIMESTAMP, UMIDADE, PH 
FROM tabelasensor;

-- Retorna apenas os registros em que o sistema está irrigando (valor 1)
SELECT * 
FROM tabelasensor 
WHERE IRRIGANDO = 1;

-- Mostra as leituras em que a umidade está abaixo de 2000
SELECT * 
FROM tabelasensor 
WHERE UMIDADE < 2000;

-- Ordena os resultados de forma crescente pelo valor de pH
SELECT * 
FROM tabelasensor 
ORDER BY PH ASC;

-- Ordena os resultados de forma decrescente pelo valor de umidade
SELECT * 
FROM tabelasensor 
ORDER BY UMIDADE DESC;

-- Conta o número total de registros na tabela
SELECT COUNT(*) AS total_linhas 
FROM tabelasensor;

-- Mostra o maior e o menor valor de umidade registrados
SELECT MAX(UMIDADE) AS umidade_maxima, MIN(UMIDADE) AS umidade_minima 
FROM tabelasensor;
