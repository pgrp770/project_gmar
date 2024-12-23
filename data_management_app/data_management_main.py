from data_management_app.services.insert_postgress_service.insert_connection_tables_to_sql import \
    main_flow_insert_connection_tables
from data_management_app.services.insert_postgress_service.insert_df_to_sql_service import main_flow_insert_tables


if __name__ == '__main__':
    main_flow_insert_tables()
    main_flow_insert_connection_tables()



