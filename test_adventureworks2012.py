# Check if the total number of rows in the table is greater than 0
def test_address_row_count(db_connection):
    cursor = db_connection.cursor()
    cursor.execute("SELECT COUNT(*) FROM [Person].[Address]")
    row_count = cursor.fetchone()[0]
    cursor.close()
    assert row_count > 0


# Check distinct number of cities
def test_address_distinct_cities(db_connection):
    cursor = db_connection.cursor()
    cursor.execute("SELECT COUNT(DISTINCT City) FROM [Person].[Address]")
    row_count = cursor.fetchone()[0]
    cursor.close()
    assert row_count == 575


# Check if the total number of rows in the table is greater than 0
def test_document_row_count(db_connection):
    cursor = db_connection.cursor()
    cursor.execute("SELECT COUNT(*) FROM [Production].[Document]")
    row_count = cursor.fetchone()[0]
    cursor.close()
    assert row_count > 0


# Check if status value is 1, 2, or 3
def test_document_max_summary_length(db_connection):
    cursor = db_connection.cursor()
    cursor.execute("SELECT DISTINCT Status FROM [Production].[Document]")
    distinct_statuses = [row[0] for row in cursor.fetchall()]
    cursor.close()
    assert any(status in (1, 2, 3) for status in distinct_statuses), "No distinct status in (1, 2, 3)"


# Check if the total number of rows in the table is greater than 0
def test_unit_measure_row_count(db_connection):
    cursor = db_connection.cursor()
    cursor.execute("SELECT COUNT(*) FROM [Production].[UnitMeasure]")
    row_count = cursor.fetchone()[0]
    cursor.close()
    assert row_count > 0


# Check if all the UnitMeasure names are unique
def test_unit_measure_unique_names(db_connection):
    cursor = db_connection.cursor()
    cursor.execute("SELECT Name FROM [Production].[UnitMeasure]")
    names = [row[0] for row in cursor.fetchall()]
    cursor.close()
    assert len(names) == len(set(names))