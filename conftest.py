import pytest
import pymssql

# Server and user information
MSSQL_SERVER = "EPGETBIW052E\\SQLEXPRESS"
MSSQL_USER = "test_user"
MSSQL_PASSWORD = "test_password"
MSSQL_DATABASE = "AdventureWorks2012"

# Create a connection string for the MSSQL server
con_str = f"Server={MSSQL_SERVER};Database={MSSQL_DATABASE};User Id={MSSQL_USER};Password={MSSQL_PASSWORD};"

# Fixture for the database connection
@pytest.fixture(scope="function")
def db_connection():
    connection = pymssql.connect(con_str)

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
    
