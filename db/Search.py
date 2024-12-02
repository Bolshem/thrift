import datetime

from db.MariaDbConnector import connect, table_name
import json
import decimal

class Encoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, decimal.Decimal): return float(obj)
        if isinstance(obj, datetime.date): return obj.isoformat()


def search_by_field_name_pattern(field_name : str, pattern : str):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM `{table_name}` WHERE {field_name} LIKE %s", (f"%{pattern}%",))

    return format_all_rows(cursor)

def search_by_field_name_and_value(field_name : str, value):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM `{table_name}` WHERE {field_name} = %s", (value,))

    return format_all_rows(cursor)

def retrieve_all():
    conn = connect()
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM `{table_name}`")

    return format_all_rows(cursor)

def format_all_rows(rows):
    # Fetch column names
    columns = [desc[0] for desc in rows.description]

    # Combine column names and rows into a list of dictionaries
    result = [dict(zip(columns, row)) for row in rows]

    # Convert the list of dictionaries to a JSON string
    return json.dumps(result, cls=Encoder)