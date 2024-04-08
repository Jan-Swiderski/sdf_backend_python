# SDF Backend Project

## Overview
This project is a backend application designed to provide APIs for data manipulation and retrieval. It uses PostgreSQL as its database.

## Prerequisites
- Python 3.8 or higher
- PostgreSQL
- Conda environment or Virtualenv (depending on your preference)

## Installation

### Using Conda
To create a Conda environment, navigate to the project's root directory and run:
```
conda create --name myenv python=3.8
```
Activate the Conda environment:
```
conda activate myenv
```
Install the required packages from the `dependencies.txt` file using Conda:
```
conda install --file dependencies.txt
```
**Note:** If some packages are not available through Conda, you may need to use `pip` within the Conda environment.

### Using Virtualenv
If you prefer using `virtualenv` instead of Conda, follow these steps:

1. Install `virtualenv` if you haven't already:
```
pip install virtualenv
```
2. Create a virtual environment in the project directory:
```
virtualenv venv
```
3. Activate the virtual environment:
   - On Windows: `venv\Scripts\activate`
   - On Unix or MacOS: `source venv/bin/activate`
4. Install the required packages using `pip`:
```
pip install -r dependencies.txt
```

## Configuration

### Database Configuration
This project requires a PostgreSQL database. Set the following environment variables in a `.env` file in the project's root directory:
- `PSQL_USER_NAME`: Your database username
- `PSQL_USER_PASSWORD`: Your database password
- `PSQL_HOST`: Your database host (e.g., `localhost` for a local server)
- `PSQL_DB_NAME`: The name of the database to connect to

Example `.env` file content:
```
PSQL_USER_NAME=my_username
PSQL_USER_PASSWORD=my_password
PSQL_HOST=localhost
PSQL_DB_NAME=my_database
```
## Usage

To run the application, execute:
```
python myapp.py
```
Please note that running the application using `python myapp.py` will start it in debug mode, which is not intended for production use. This mode is beneficial for development, as it provides detailed error messages and automatically restarts the server upon code changes.
## License
This project is licensed under the MIT License - see the LICENSE file for details.
