import db_access

@db_access.connection_handler
def get_all_serv_proj(cursor):
    query = f"""
        SELECT
        id AS serv_proj_id,
        description AS serv_proj_description,
        number AS serv_proj_number
        FROM served_projects;
        """
    cursor.execute(query)
    result = cursor.fetchall()
    return result
