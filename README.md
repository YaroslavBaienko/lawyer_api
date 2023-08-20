
# Lawyer API

A FastAPI project to manage and interact with data related to clients, judges, and users.

## Project Structure

```
.
├── api
│   ├── __init__.py
│   ├── clients.py
│   └── judges.py
├── app
│   ├── main.py
│   ├── static
│   │   ├── favicon.ico
│   │   └── main.js
│   ├── templates
│   │   └── index.html
│   └── test.db
├── db
│   ├── __init__.py
│   ├── database.py
│   └── models.py
├── judges.xlsx
├── README.md
├── schemas
│   ├── __init__.py
│   ├── clients.py
│   ├── judges.py
│   └── users.py
├── test.db
└── utils
    ├── __init__.py
    └── get_from_excel.py
```

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/lawyer_api.git
   ```

2. Navigate to the project directory:
   ```bash
   cd lawyer_api
   ```

3. Install the required packages (preferably in a virtual environment):
   ```bash
   pip install -r requirements.txt
   ```

## Running the Application

1. Navigate to the `app` directory:
   ```bash
   cd app
   ```

2. Run the FastAPI application:
   ```bash
   uvicorn main:app --reload
   ```

3. Visit `http://localhost:8000` in your browser to access the API documentation and test endpoints.

## Features

- **Clients Management**: Add, retrieve, update, and delete client data.
- **Judges Management**: Store and manage information related to judges. Includes features like updating a judge's phone based on their name.
- **Data Import**: Utility functions to extract judge data from Excel (`judges.xlsx`) and populate the database.

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

[MIT](https://choosealicense.com/licenses/mit/)
