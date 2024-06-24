Este é um projeto fictício. O contexto e as perguntas de negócios não são reais. Este projeto foi feito com base na playlists do Programador Lhama (Rafael Ferreira)

# Problema de Negócio: Extração de Dados de Artistas do Site da Galeria Nacional de Arte dos EUA

Você é um analista de dados em uma empresa de consultoria cultural. Um cliente importante, interessado em tendências artísticas ao longo do tempo, solicitou um estudo abrangente sobre os artistas cujas obras estão disponíveis na Galeria Nacional de Arte dos EUA. O cliente deseja uma análise detalhada dos nomes dos artistas presentes na coleção disponível no site da galeria.

## Objetivo:

Extrair os nomes dos artistas listados na página da Galeria Nacional de Arte dos EUA, acessando o seguinte [link:](https://web.archive.org/web/20121007172955/https://www.nga.gov/collection/anZ1.htm)

Realizar o processo de ETL (Extração, Transformação e Carga) para obter os dados de forma estruturada e pronta para análise.

## Requisitos Técnicos:

Extração (Extract): Implementar um script ou programa para acessar o conteúdo HTML da página web especificada e extrair os nomes dos artistas listados.

Transformação (Transform): Limpar e formatar os dados extraídos, removendo quaisquer caracteres indesejados, espaços adicionais ou tags HTML que não sejam relevantes para os nomes dos artistas.

Carga (Load): Armazenar os dados transformados em um formato adequado para análise posterior, como um arquivo CSV ou uma tabela de banco de dados, garantindo que a estrutura dos dados seja consistente e acessível.

## Considerações Adicionais:

Verificar a integridade dos dados extraídos para garantir que todos os nomes de artistas sejam capturados de forma completa e precisa.
Automatizar o processo de extração para que possa ser reutilizado periodicamente, mantendo a análise de dados atualizada conforme novos artistas são adicionadas à coleção da galeria.
Benefícios Esperados:

Fornecer ao cliente uma base de dados atualizada e organizada dos artistas representados na Galeria Nacional de Arte dos EUA.

## Instruções de Uso

Este banco de dados foi configurado usando contêineres Docker. Para começar, certifique-se de ter o Docker instalado e execute o seguinte comando:

```bash
docker compose up
```

Após a execução deste comando, você poderá iniciar o arquivo `run.py` na raiz do projeto com o seguinte comando:

```bash
python run.py
```
