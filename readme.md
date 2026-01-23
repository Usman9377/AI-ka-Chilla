# 🚀 AI ka Chilla Learning Journey (Codanics)

Welcome to my learning journey in **AI ka Chilla** by **Codanics** 🎓🤖  
This repository documents what I am learning, practicing, and implementing step-by-step as I build a strong foundation in **Python, Data, and AI**.

---

## 🌱 What I Have Learned So Far

### 📌 Portfolio Development
- Learned how to design and build a professional **portfolio website**
- 🔗 **Portfolio Link:** [My Portfolio](https://Usman9377.github.io/My-Portfolio/)

---

### 📊 Data Fundamentals
- Types of data (structured, unstructured, numerical, categorical)
- Importance of data in AI & Data Science

---

### 🐍 Python Programming Basics
- Python syntax & fundamentals
- Functions & reusable code
- Loops (`for`, `while`)
- Conditional statements (`if`, `elif`, `else`)
- Data structures:
  - Lists
  - Tuples
  - Sets
  - Dictionaries
- File handling in Python 📁

---

## 🌐 Data Fetching & APIs (Current Focus)

I am now learning **data fetching using Python libraries** for real-world datasets 🌍📈.

### 🧪 Conda Environment Setup
To keep things clean and reproducible, I created a separate environment:

```bash
conda create -n data_gathering python=3.10 -y
conda activate data_gathering
```
  - there are following libraries for data fetching
    - wbdata
```bash
    pip install wbdata
    pip install pandas
    pip install ipykernel
```
here is the link of documentation of wbdata library, https://wbdata.readthedocs.io/en/stable/
```python
import pandas as pd
import seaborn as sns
import wbdata
```
here is the link of documentation of eurostat library, https://pypi.org/project/eurostat/
### 📊 Dtale

**Dtale** is an interactive Python library for **Exploratory Data Analysis (EDA)** built on top of **Pandas**.  
It provides a **browser-based interface** that allows users to explore, visualize, and analyze DataFrames without writing extensive code.

**Key features:**
- 🧭 Interactive DataFrame viewer
- 🔍 Filtering, sorting, and searching data
- 📈 Built-in statistical summaries
- 🧪 Quick visualizations (histograms, correlations, charts)
- 🌐 Web-based UI launched directly from Python

**Use cases:**
- Rapid dataset inspection
- Interactive exploratory data analysis
- Debugging and validating datasets
- Data understanding before modeling
```bash
    pip install dtale
```
```python
import pandas as pd
import seaborn as sns
import dtale
```
### 🚶 Pygwalker

**Pygwalker** is a Python library for **no-code Exploratory Data Analysis (EDA)** and **interactive data visualization**.  
It turns a Pandas DataFrame into an **interactive visual interface**, similar to Tableau, directly inside Jupyter Notebook.

**Key features:**
- 📊 Drag-and-drop data exploration
- 🧠 No-code visual analytics
- 🔍 Automatic data type detection
- 📈 Interactive charts and dashboards
- 🧪 Works seamlessly with Pandas DataFrames

**Use cases:**
- Quick exploratory data analysis (EDA)
```bash
    pip install pygwalker
```
```python
import pandas as pd
import seaborn as sns
import pygwalker
```

### 🍬 Sweetviz

**Sweetviz** is a Python library used for **automatic Exploratory Data Analysis (EDA)**.  
It generates a **comprehensive, visually rich HTML report** from a Pandas DataFrame with minimal code.

**Key features:**
- 📊 Automatic analysis of numerical & categorical features
- 🔍 Detection of missing values and data distributions
- 🔗 Feature relationships and correlations
- 🎯 Target variable analysis for supervised learning
- 🌐 Interactive HTML reports
```bash
    pip install sweetviz
```
```python
import pandas as pd
import seaborn as sns
import sweetviz
```
### 🧾 Skimpy

**Skimpy** is a Python library for **quick and concise Exploratory Data Analysis (EDA)**.  
It provides a **compact summary of a dataset**, helping users rapidly understand data structure, data types, missing values, and basic statistics.

**Key features:**
- ⚡ Fast dataset overview
- 🧮 Summary statistics for numerical features
- 🔤 Categorical feature summaries
- ❓ Missing value analysis
- 📐 Data type detection
```bash
conda create -n skimpy_env python=3.10 -y
conda activate skimpy_env

pip install skimpy
pip install pandas seaborn ipykernel
python -m ipykernel install --user --name skimpy_env
```
**Use cases:**
- Rapid initial data inspection
- Understanding dataset structure
- Checking data quality before deeper analysis
- Lightweight EDA in notebooks and scripts

**Example usage:**
```python
import pandas as pd
import seaborn as sns
from skimpy import skim

skim(df)
```
## 🤖 LIDA Library in Python — Definition

**LIDA (Language-Integrated Data Analysis)** is a Python library that uses **Large Language Models (LLMs)** to automatically perform **data analysis and visualization** through natural language prompts. It allows users to explore datasets by simply **asking questions in plain English**, making data analysis more intuitive and interactive.

LIDA is especially useful for **EDA, automated chart generation, and insight discovery** without manually writing complex plotting or analysis code.

---

## ✨ Key Features

- 🗣️ **Natural language–based data analysis**
- 📊 **Automatic visualization generation**
- 🧠 **LLM-powered insights and summaries**
- 🔄 **Interactive and iterative analysis**
- 🧪 Works well with **Pandas DataFrames**
- ⚡ Rapid **Exploratory Data Analysis (EDA)**

---

## 🧩 Core Components

| Component | Description |
|---------|-------------|
| LLM Engine | Uses language models to understand user queries |
| Data Summarizer | Automatically summarizes dataset structure |
| Chart Generator | Creates suitable plots based on questions |
| Insight Engine | Produces human-readable insights |

---

## 📊 What LIDA Can Do

- Generate charts from text prompts  
- Explain trends, patterns, and outliers  
- Suggest meaningful visualizations  
- Summarize datasets automatically  
- Answer analytical questions like:
  - *“Show sales trend over tim*
```bash
pip install lida
```
```python
from lida import Manager, llm

lida = Manager(text_gen = llm("openai")) # palm, cohere ..
summary = lida.summarize("data/cars.csv")
goals = lida.goals(summary, n=2) # exploratory data analysis
charts = lida.visualize(summary=summary, goal=goals[0]) # exploratory data analysis
```

