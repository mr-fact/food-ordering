# food-ordering

Welcome to the Food Ordering Project! This project is designed to facilitate food ordering and management, consisting of two main apps: `food` and `account`.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Usage](#usage)

## Introduction

The Food Ordering Project aims to provide a platform for managing and ordering food items. It consists of two main apps:

- `food`: Handles food-related models, such as categories, food items, prices, packets, and orders.
- `account`: Manages user-related models, such as user accounts and authentication.

## Features

- Manage food categories and items.
- Set and manage prices for food items.
- Allow users to create packets with selected items.
- Process orders and track their status.
- User authentication and account management.

## Project Structure

The project is structured into two apps:

- `food`: Contains models and views related to food management.
- `account`: Manages user authentication and account information.
```
food_ordering_project/
|-- food/
|   |-- migrations/
|   |-- static/
|   |-- templates/
|   |-- __init__.py
|   |-- admin.py
|   |-- apps.py
|   |-- models.py
|   |-- serializers.py
|   |-- tests.py
|   |-- urls.py
|   |-- views.py
|-- account/
|   |-- migrations/
|   |-- static/
|   |-- templates/
|   |-- __init__.py
|   |-- admin.py
|   |-- apps.py
|   |-- models.py
|   |-- serializers.py
|   |-- tests.py
|   |-- urls.py
|   |-- views.py
|-- manage.py
|-- food_ordering_project/
|   |-- __init__.py
|   |-- settings.py
|   |-- urls.py
|   |-- asgi.py
|   |-- wsgi.py
|-- README.md
|-- requirements.txt
```

## Installation

To set up the Food Ordering Project locally, follow these steps:

1. Clone the repository:

```bash
git clone https://github.com/mr-fact/food-ordering.git
cd food-ordering
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Apply migrations:

```bash
python manage.py migrate
```

## Usage

To run the project locally, use the following command:

```bash
python manage.py runserver
```

Visit `http://127.0.0.1:8000/` in your web browser to access the application.
