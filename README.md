# 🎸 Mayhem: Linhagem do Caos — Dashboard Analítico

Este projeto é uma aplicação de Business Intelligence (BI) imersiva dedicada à história e discografia da lendária banda de Black Metal norueguês, **Mayhem**. O dashboard combina engenharia de dados, visualizações interativas e uma atmosfera multimídia para explorar a linhagem do caos da banda.

---

## 🚀 Funcionalidades

- **Timeline Interativa:** Explore os eventos marcantes, desde a fundação em 1984 até os lançamentos mais recentes.
- **Análise Visual Sincronizada:** Gráficos de pizza e barras que mostram a distribuição de álbuns, EPs, demos e eventos, com um mapa de cores consistente (Black & Blood).
- **Filtro Inteligente ("Lupinha"):** Pesquisa em tempo real por palavras-chave na discografia e descrições históricas.
- **Atmosfera Multimídia:** Player de áudio integrado com o clássico *De Mysteriis Dom Sathanas (Live)* e identidade visual personalizada via CSS.
- **Design Customizado:** Interface "True Black" com cabeçalhos em vermelho sangue e linhas de dados em preto profundo.

---

## 🛠️ Tecnologias Utilizadas

- **Python 3.x**
- **Streamlit:** Framework principal para a interface web.
- **Pandas:** Manipulação e tratamento da base de dados.
- **Plotly Express:** Geração de gráficos dinâmicos e reativos.
- **CSS Injection:** Personalização avançada da interface (UI/UX).

---

## 📂 Estrutura do Projeto

- `app_mayhem.py`: O código-fonte da aplicação.
- `mayhem_timeline_FIXED.csv`: Base de dados tratada (derivada do Excel original).
- `logo.jpg`: Identidade visual da banda.
- `De Mysteriis Dom Sathanas (Live) - Mayhem (youtube).mp3`: Atmosfera sonora 
- `requirements.txt`: Lista de dependências para o deploy.

---

## 📜 Relatório de Engenharia (The Black Circle Library)

### Fase 1: Estruturação de Dados
Os dados brutos foram organizados cronologicamente no arquivo `Mayhem_Timeline_Black_Edition.xlsx`, categorizados por tipo de obra e impacto histórico (fundação, polêmicas, reformas da banda, etc.). Os dados foram coletados via pesquisa e Gemini. 

### Fase 2: Desenvolvimento do Core (Python)
Utilizou-se o Streamlit para transformar dados estáticos em uma ferramenta dinâmica. Implementou-se o tratamento de erros e cache de dados para garantir performance e estabilidade.

### Fase 3: Sincronia de Cores e UI
Foi criado um mapa de cores fixo (`color_map`) para garantir consistência visual entre diferentes tipos de gráficos. O design foi refinado com injeção de HTML/CSS para quebrar o padrão "claro" dos navegadores e manter a estética obscura.

### Fase 4: Refinamento de UX
Adição de filtros reativos e uma barra de busca para facilitar a navegação por décadas de história, garantindo que a informação seja acessível de forma rápida e intuitiva.

---

## 🔧 Como rodar o projeto

1. Clone o repositório:
   ```bash
  git clone https://github.com/BiaAbaaoud/mayhem-ritual-dash.git
