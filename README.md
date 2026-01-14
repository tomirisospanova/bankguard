# BankGuard – Real-Time Anti-Fraud System

[![Python](https://img.shields.io/badge/Python-3.10-blue)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.100.0-green)](https://fastapi.tiangolo.com/)
[![Scikit-Learn](https://img.shields.io/badge/ML-scikit--learn-orange)](https://scikit-learn.org/)
[![Docker](https://img.shields.io/badge/Docker-20.10.0-blue)](https://www.docker.com/)

BankGuard – это гибридная система обнаружения мошеннических транзакций в реальном времени, объединяющая ML-модель и rule-based engine с API на FastAPI.

---

## Описание проекта

Система предназначена для банков и финансовых организаций и включает:

- ML-модель для оценки риска транзакций  
- Правила банка для дополнительной проверки (rule-based engine)  
- Реальное время через FastAPI API  
- Возможность интеграции с аналитическими панелями и сторонними сервисами  
- Docker-контейнеризацию для быстрого развертывания  

---

## Структура проекта

bankguard/
├── backend/ # FastAPI backend
│ ├── main.py # Основной API
│ ├── config.py # Настройки проекта
│ ├── schemas.py # Pydantic схемы
│ ├── fraud_engine.py # Главная логика anti-fraud
│ ├── rules.py # Rule-based scoring
│ └── ml_model.py # ML модель для scoring
├── ml/
│ └── train_model.py # Скрипт для обучения ML модели
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
└── README.md


---

## Установка и запуск

### 1. Клонирование репозитория
git clone https://github.com/YourUsername/bankguard.git
cd bankguard

### 2. Установка зависимостей
python -m pip install --upgrade pip
python -m pip install -r requirements.txt

### 3. Обучение модели
python ml\train_model.py

### 4. Запуск FastAPI
python -m uvicorn backend.main:app --reload

### 5. (Опционально) Запуск через Docker

docker-compose up --build
API будет доступен по адресу: http://localhost:8000/docs

