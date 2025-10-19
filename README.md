# Formula1-Data-Engineering-and-Analytics-Pipeline

## Project Overview

This project demonstrates an end-to-end data engineering pipeline built using Microsoft Azure, designed to extract, process, and visualize Formula 1 race data from the Ergast API.

## Architecture

- **Data Source:** Ergast API (Formula 1 datasets — drivers, constructors, races, results, pit stops, lap times, qualifying, etc.)

- **Storage:** Azure Data Lake Storage Gen2 with three containers — Raw, Processed, Presentation

- **Compute:** Azure Databricks (mounted ADLS containers, created clusters & notebooks)

- **Orchestration:** Azure Data Factory (ADF) pipelines for ingestion and transformation workflows

- **Visualization:** Power BI dashboards connected to the presentation layer

## End to End Data Flow

![image_alt](https://github.com/BhaskarKosala/Formula1-Data-Engineering-and-Analytics-Pipeline/blob/e422f33bfd617985ac601686d0ef7c18f0512f1a/F1_Flow%20(1).jpg)


## Implementation Steps

- Extracted CSV and JSON files from the Ergast API.

- Loaded them into the Raw layer of ADLS.

- Used PySpark DataFrame Reader APIs to ingest data into Databricks and define schemas.

- Applied data cleaning and transformations using PySpark and SQL; stored results in Delta format in the Processed layer.

- Created incremental loads organized by date folders and registered as managed & external tables.

- Built SQL queries and Python functions to compute race results, driver standings, and constructor standings.

- Developed ADF pipelines for both raw and transformed datasets, using Get Metadata, If Condition, and Execute Pipeline activities.

- Connected Power BI to the presentation layer for interactive reports and dashboards.

## Tools & Technologies

- **Azure Services:** Databricks, Data Factory, ADLS Gen2

- **Languages:** Python, SQL

- **Frameworks:** PySpark, Delta Lake

- **Visualization:** Power BI

- **API:** Ergast Developer API
