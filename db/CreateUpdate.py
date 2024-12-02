from db.MariaDbConnector import connect, table_name
from db.Search import search_by_field_name_and_value


def create_item(item):
    conn = connect()
    cursor = conn.cursor()

    #change all keys to be lower case
    item = {k.lower(): v for k, v in item.items()}

    # check if id is present in the item, if yes - return error
    if 'id' in item:
        return {'error': 'id should not be specified'}

    # item should be a dictionary
    # extract keys and values and put them into sql query
    keys = ', '.join(item.keys())

    # all values should be in single quotes
    values = ', '.join([f"'{value}'" for value in item.values()])

    cursor.execute(f"INSERT INTO `{table_name}` ({keys}) VALUES ({values})")
    conn.commit()

    # return newly created item id
    return search_by_field_name_and_value('id', cursor.lastrowid)



def update_item(item):
    conn = connect()
    cursor = conn.cursor()

    #change all keys to be lower case
    item = {k.lower(): v for k, v in item.items()}

    # check if id is present in the item, if no - return error
    if 'id' not in item:
        return {'error': 'id should be specified'}

    # item should be a dictionary
    # extract keys and values and put them into sql query
    keys = ', '.join([f"{key} = '{value}'" for key, value in item.items()])

    cursor.execute(f"UPDATE `{table_name}` SET {keys} WHERE id = {item['id']}")
    conn.commit()

    # return newly created item id
    return search_by_field_name_and_value('id', item['id'])

