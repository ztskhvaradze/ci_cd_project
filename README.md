# AdventureWorks2012 Pytest Project

This pytest project is designed to test a connection to the AdventureWorks2012 database using Python and the pyodbc library. It contains fixtures and test functions to verify the database's integrity and the correctness of its data. 

## Prerequisites

Before running the tests in this project, ensure you have the following prerequisites:

- Python 3.x installed on your system.
- The `pyodbc` library installed. You can install it using pip:

pip install pyodbc


## Configuration

Make sure to configure the following variables in the `conftest.py` file to match your SQL Server setup:

- `MSSQL_SERVER`: The SQL Server instance name.
- `MSSQL_USER`: The database user name.
- `MSSQL_PASSWORD`: The database user password.
- `MSSQL_DATABASE`: The name of the AdventureWorks2012 database.

## Running the Tests

To run the tests, use the following command:

pytest test_adventureworks2012.py


This will execute all the test functions defined in `test_adventureworks2012.py` using the configured database connection.

## Test Descriptions

Here are the tests included in this project:

1. `test_example_function`: Performs a basic test to ensure a connection to the database is established and data can be fetched.

2. `test_address_row_count`: Checks if the total number of rows in the [Person].[Address] table is greater than 0.

3. `test_address_distinct_cities`: Verifies that there are exactly 575 distinct cities in the [Person].[Address] table.

4. `test_document_row_count`: Ensures that the total number of rows in the [Production].[Document] table is greater than 0.

5. `test_document_max_summary_length`: Validates that the Status values in the [Production].[Document] table are 1, 2, or 3.

6. `test_unit_measure_row_count`: Checks if the total number of rows in the [Production].[UnitMeasure] table is greater than 0.

7. `test_unit_measure_unique_names`: Verifies that all UnitMeasure names in the [Production].[UnitMeasure] table are unique.


## Branching Strategy

Our project employs a simple two-branch strategy with `dev` and `main` branches to efficiently manage the development process.This strategy is effective for small development teams.

### Justification

1. **Clear separation of development and production:** The `dev` branch is used for ongoing development work, while the `main` branch represents the stable, production-ready code.
2. **Simplified merging process:** Merging mainly occurs between the `dev` and `main` branches, reducing the complexity and conflicts encountered in multi-branch strategies.
3. **Ease of use and understanding:** This straightforward strategy is easy to understand and manage for the entire team.
4. **Improved workflow and collaboration:** Developers can work in parallel on features in the `dev` branch and merge successful changes to the `main` branch, ensuring code goes through a standardized process such as code reviews and testing.
5. **Flexibility for growth:** If needed, this strategy can be expanded to include additional branches such as `qa` for quality assurance or individual feature branches.

This two-branch strategy provides a clear separation between development and production, an efficient workflow, code quality assurance, and the flexibility to adapt as the project grows.
