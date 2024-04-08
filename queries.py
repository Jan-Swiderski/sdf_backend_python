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

@db_access.connection_handler
def get_pois_by_serv_proj_id(cursor, serv_proj_id):
    query = f"""
        SELECT
        pois.id AS poi_id,
        pois.served_project_id AS poi_serv_proj_id,
        pois.description AS poi_description,
        pois.number AS poi_number        
        FROM points_of_interest AS pois
        WHERE served_project_id = {serv_proj_id};
        """
    cursor.execute(query)
    result = cursor.fetchall()
    return result

@db_access.connection_handler
def get_sub_pois_by_poi_id(cursor, poi_id):
    query = f"""
        SELECT
        sub_pois.id AS sub_poi_id,
        sub_pois.point_of_interest_id AS sub_poi_poi_id,
        sub_pois.description AS sub_poi_description,
        sub_pois.number AS sub_poi_number
        FROM sub_points_of_interest AS sub_pois
        WHERE sub_pois.point_of_interest_id = {poi_id};
        """
    cursor.execute(query)
    result = cursor.fetchall()
    return result

@db_access.connection_handler
def get_sub_pois_events_by_sub_poi_id(cursor, sub_poi_id):
    query = f"""
        SELECT
        sub_poi_events.id AS sub_poi_event_id,
        sub_poi_events.date_time AS sub_poi_event_date_time,
        sub_poi_events.user_id AS sub_poi_events_user_id
        FROM sub_points_of_interest_events AS sub_poi_events
        JOIN sub_points_of_interest_and_sub_points_of_interest_events_joins AS sub_poi_and_sub_poi_events_joins
            ON sub_poi_and_sub_poi_events_joins.sub_point_of_interest_event_id = sub_poi_events.id
        WHERE sub_poi_and_sub_poi_events_joins.sub_point_of_interest_id = {sub_poi_id};
        """
    cursor.execute(query)
    result = cursor.fetchall()
    return result

@db_access.connection_handler
def get_sub_pois_data_by_sub_poi_id(cursor, sub_poi_id):
    query = f"""
        SELECT
        sub_points_of_interest_data.data_content AS sub_pois_data_content,
        data_fields.description AS data_field_description
        FROM sub_points_of_interest
        RIGHT JOIN sub_points_of_interest_data
            ON sub_points_of_interest_data.sub_point_of_interest_id = sub_points_of_interest.id
        RIGHT JOIN data_fields
            ON data_fields.id = sub_points_of_interest_data.data_field_id
        WHERE sub_points_of_interest_data.sub_point_of_interest_id = {sub_poi_id};
        """
    cursor.execute(query)
    result = cursor.fetchall()
    return result

@db_access.connection_handler
def get_images_by_sub_poi_event_id(cursor, sub_poi_event_id):
    query = f"""
        SELECT
        id AS event_id,
        sub_point_of_interest_event_id AS sub_poi_event_id,
        image_address
        FROM sub_points_of_interest_events_images
        WHERE sub_point_of_interest_event_id = {sub_poi_event_id};
        """
    cursor.execute(query)
    result = cursor.fetchall()
    return result

@db_access.connection_handler
def get_all_images(cursor):
    query = f"""
        SELECT *
        FROM sub_points_of_interest_events_images;
        """
    cursor.execute(query)
    result = cursor.fetchall()
    return result
