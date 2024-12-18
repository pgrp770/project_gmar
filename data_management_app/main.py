from data_management_app.db.sql_db.models import Region
from data_management_app.db.sql_db.repositories.postgres_repository.postgres_crud import insert_many_generic
from data_management_app.services.normalize_data_srevices.retype_and_clean_csv_service import main_flow_clean_csv
from data_management_app.services.normalize_data_srevices.split_big_csv_to_tables import normalize_region_table

if __name__ == '__main__':
    df = normalize_region_table(main_flow_clean_csv())
    print(df)
    print(insert_many_generic(

    ))

