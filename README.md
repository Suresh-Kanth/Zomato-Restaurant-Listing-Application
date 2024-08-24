# Zomato Restaurant Listing Application

This project is a simple web application to list and view details of restaurants using data from Zomato. It includes features like filtering by country, average spend for two people, and cuisines, as well as search functionality.

## Features

- List of restaurants with pagination
- View details of a specific restaurant
- Filter by country, average spend, and cuisines
- Search for restaurants by name or description

## Setup Instructions

### Prerequisites

- Python 3.x installed on your machine
- `pip` package installer

### Step-by-Step Guide

1. **Clone the Repository**

   ```bash
   git clone https://github.com/e42-typeface-ai/iiitk-Suresh-Kanth.git
   cd iiitk-Suresh-Kanth
   ```

2. **Create a Virtual Environment (or you can enter the already created one)**

   - **Windows**:
     ```bash
     python -m venv venv
     venv\Scripts\activate
     ```
   - **macOS/Linux**:
     ```bash
     python3 -m venv venv
     source venv/bin/activate
     ```

3. **Install Dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Load Zomato Data into SQLite Database**

   Ensure you have the Zomato data in `zomato.csv` file. Run the following script to load data into an SQLite database that is present in WEB API Service folder:

   ```bash
   python load.py
   ```

5. **Run the Flask Application**

   Start the Flask API service present in WEB API Service folder:

   ```bash
   python api.py
   ```

   In a separate terminal, start the Flask frontend application present in Ui folder:

   ```bash
   python app.py
   ```

6. **Access the Application**

   Open your web browser and navigate to:
   ```
   http://127.0.0.1:5001
   ```

## API Endpoints

- **Get Restaurant by ID**
  ```
  GET /restaurant/<id>
  ```

- **Get List of Restaurants**
  ```
  GET /restaurants?page=<page>&country=<country>&avg_spend=<avg_spend>&cuisines=<cuisines>&search=<search>
  ```

## File Structure

```
.
├── README.md
├── requirements.txt    # Python dependencies
├── venv                # Virtual environment
├── WEB_API_Service
│   ├── api.py              # Backend Flask API service
│   ├── load_data.py        # Script to load data into SQLite database
│   ├── zomato.csv          # Zomato dataset
└── UI
    ├── app.py              # Frontend Flask application
    └── templates           # HTML templates
        ├── restaurant_detail.html
        ├── restaurant_list.html
