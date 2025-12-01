# Fintech Performance Analytics

**Demo**: análisis de cartera de préstamos con base simulada de 50.000 clientes, ETL en Python y artefactos para BI.

## Contenido
- /data : clientes.csv, prestamos.csv, pagos.csv
- /src  : main.py, generate_data.py, query.sql
- /docs : architecture.png
- requirements.txt

## Objetivo
Analizar morosidad, recupero y riesgo; generar KPIs y dashboards para priorizar cobranzas y optimizar políticas crediticias.

## Cómo ejecutar (local/Colab)
1. Clonar o descargar el repo.
2. En Google Colab: subir carpeta y ejecutar `src/generate_data.py` o los notebooks incluidos.
3. Ejecutar `src/main.py` para generar `prestamos_enriquecidos.csv`.
4. Conectar Power BI o Looker Studio a los CSV (o cargar `prestamos_enriquecidos.csv`).

## KPIs principales
- Morosidad (% préstamos en estado 'atrasado' o 'judicial')
- Saldo vivo
- Tasa de recupero (Total Pagado / Monto Otorgado)
- Top clientes por saldo
- Cohorts de pago por mes de otorgamiento

## Arquitectura
CSV → ETL (Python) → Vistas/Outputs → Power BI / Looker Studio

## Contacto
Jonathan Martínez — jonacba18@gmail.com
