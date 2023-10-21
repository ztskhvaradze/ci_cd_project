import pytest
import pyodbc

# Server and user information
MSSQL_SERVER = "EPGETBIW052E\\SQLEXPRESS"
MSSQL_USER = "test_user"
MSSQL_PASSWORD = "test_password"
MSSQL_DATABASE = "AdventureWorks2012"

# Connection string for the MSSQL server
con_str = (
    f"DRIVER={{ODBC Driver 17 for SQL Server}};"
    f"SERVER={MSSQL_SERVER};"
    f"DATABASE={MSSQL_DATABASE};"
    f"UID={MSSQL_USER};"
    f"PWD={MSSQL_PASSWORD}"
)


# Fixture for the database connection
@pytest.fixture(scope="function")
def db_connection():
    connection = pyodbc.connect(con_str)

    try:
        yield connection
    finally:
        connection.close()


# Test function using db_connection fixture
def test_example_function(db_connection):
    # Perform your query, e.g., SELECT * from Production.Document
    cursor = db_connection.cursor()
    cursor.execute("SELECT * FROM Production.Document")

    # Fetch and process rows in the table or do the necessary testing
    rows = cursor.fetchall()
    assert len(rows) > 0

    # Close the cursor
    cursor.close()
