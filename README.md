# 📦 Retail Shelf Space Optimizer

> An End-to-End Retail Analytics Application that optimizes product shelf placement using **Association Rule Mining (FP-Growth)**, **Network Analysis**, and **Community Detection**.

![Python](https://img.shields.io/badge/Python-3.10-blue?logo=python)
![FastAPI](https://img.shields.io/badge/FastAPI-Backend-009688?logo=fastapi)
![Streamlit](https://img.shields.io/badge/Streamlit-Frontend-FF4B4B?logo=streamlit)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Processing-150458?logo=pandas)
![License](https://img.shields.io/badge/License-MIT-green)

---

# 📖 Project Overview

Retail Shelf Space Optimizer is an end-to-end analytics application designed to help retailers optimize shelf placement by analyzing customer transaction data.

The system discovers frequently purchased products using **FP-Growth**, generates **Association Rules**, builds a **Product Association Network**, detects product communities using **Greedy Modularity Community Detection**, and recommends optimized shelf layouts.

The application provides an interactive dashboard where users can upload transaction datasets, configure optimization parameters, visualize product relationships, and download the optimized shelf layout.

---

# ✨ Features

- 📁 Upload Retail Transaction Dataset (CSV)
- ✅ Automatic Dataset Validation
- 📊 Frequent Pattern Mining (FP-Growth)
- 🔗 Association Rule Generation
- 🌐 Product Association Network
- 🧩 Community Detection
- 📦 Shelf Space Optimization
- 📈 Interactive Network Visualization
- 📋 Shelf Layout Dashboard
- 📥 Download Optimized Shelf Layout
- ⚡ FastAPI REST Backend
- 🎨 Streamlit Frontend

---

# 🏗️ Project Architecture

The project consists of three major phases.

```
Retail Shelf Space Optimizer
│
├── 📊 Exploratory Data Analysis (EDA)
│
├── 🧠 Model Development
│
└── 💻 Full Stack Application
```

---

# 🔄 End-to-End System Workflow

```
User
   │
   ▼
Frontend (Streamlit)
   │
   │ HTTP POST
   ▼
FastAPI Backend
   │
   ▼
Validation Service
   │
   ├── Validate File
   ├── Validate Columns
   ├── Validate Data Types
   └── Validate User Parameters
   │
   ▼
Pipeline
   │
   ├── Transaction Processing
   ├── FP-Growth
   ├── Association Rules
   ├── Network Graph
   ├── Community Detection
   ├── Shelf Optimization
   └── Generate Interactive Graph
   │
   ▼
Response
   │
   ▼
Frontend Dashboard
```

---

# 📂 Project Structure

```
Retail_Shelf_Space_Optimizer
│
├── application
│   ├── backend
│   │   ├── app
│   │   ├── requirements.txt
│   │   └── ...
│   │
│   └── frontend
│       ├── assets
│       ├── components
│       ├── pages
│       ├── api.py
│       ├── app.py
│       ├── config.py
│       └── requirements.txt
│
├── data
│   ├── retail_dataset.csv
│   ├── retail_cleaned_dataset.csv
│   └── retail_data_interim.csv
│
├── EDA
│   ├── steps
│   └── EDA_notebook.ipynb
│
├── model
│   ├── steps
│   ├── shelf_optimization_engine.py
│   ├── pipeline_final_rules.csv
│   └── model_notebook.ipynb
│
└── README.md
```

---

# ⚙️ Tech Stack

## Programming Language

- Python

## Backend

- FastAPI
- Pydantic

## Frontend

- Streamlit

## Data Processing

- Pandas
- NumPy

## Machine Learning

- mlxtend (FP-Growth)
- Association Rules

## Graph Analytics

- NetworkX
- Greedy Modularity Community Detection
- PyVis

## Visualization

- Matplotlib
- Streamlit Components

---

# 🚀 Installation

## Clone Repository

```bash
git clone https://github.com/yourusername/Retail_Shelf_Space_Optimizer.git

cd Retail_Shelf_Space_Optimizer
```

---

## Backend Setup

```bash
cd application/backend

python -m venv venv

venv\Scripts\activate

pip install -r requirements.txt
```

Run Backend

```bash
uvicorn app.main:app --reload
```

Backend runs on

```
http://127.0.0.1:8000
```

---

## Frontend Setup

```bash
cd application/frontend

python -m venv venv

venv\Scripts\activate

pip install -r requirements.txt
```

Run Frontend

```bash
streamlit run app.py
```

Frontend runs on

```
http://localhost:8501
```

---

# 📡 API Endpoint

## POST

```
/run_pipeline
```

### Input

- CSV File
- Minimum Support
- Lift Threshold
- Confidence Threshold
- Shelf Capacity

### Output

```json
{
    "message": "Pipeline completed successfully",
    "summary": {
        "total_shelves": 18
    },
    "data": [
        {
            "Shelf": "Shelf 1",
            "Product": "Milk"
        }
    ]
}
```

---

# 📊 Pipeline Modules

The optimization pipeline consists of the following stages.

1. Data Validation
2. Transaction Processing
3. One-Hot Encoding
4. FP-Growth
5. Association Rule Mining
6. Product Network Construction
7. Community Detection
8. Shelf Optimization
9. Interactive Network Generation

---

# 📈 Dashboard Features

- Upload Retail Dataset
- Configure Optimization Parameters
- Run Optimization
- View KPI Cards
- View Shelf Layout
- Explore Product Association Network
- Download Shelf Layout

---

# 📸 Screenshots

## Dashboard

> Add dashboard screenshot here.

---

## Product Association Network

> Add interactive network screenshot here.

---

## System Workflow

> Add End-to-End System Workflow image here.

---

# 🔮 Future Improvements

- User Authentication
- Multiple Dataset Support
- Inventory Optimization
- Product Recommendation Engine
- Sales Forecasting
- Deployment on AWS / Azure
- Database Integration
- Real-time Analytics

---

# 👨‍💻 Author

**Manoj H C**

Information Science & Engineering Student

- Python
- Data Analytics
- Machine Learning
- FastAPI
- Streamlit

---

# ⭐ If you found this project useful

Please consider giving it a ⭐ on GitHub.

---

# 📄 License

This project is licensed under the MIT License.
