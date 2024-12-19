from data_management_app.db.sql_db.models import TerrorAttack, City
from data_management_app.db.sql_db.repositories.postgres_repository.postgres_crud import get_all_generic

a = [
    "country_txt",
    "region_txt",
    "city",
    "latitude",
    "longitude",
    "attacktype1_txt",
    "attacktype2_txt",
    "attacktype3_txt",
    "targtype1_txt",
    "targtype2_txt",
    "targtype3_txt",
    "targsubtype1_txt",
    "targsubtype2_txt",
    "targsubtype3_txt",
    "natlty1_txt",
    "natlty2_txt",
    "natlty3_txt",
    "gname",
    "gname2",
    "gname3",
    "weaptype1_txt",
    "weapsubtype1_txt",
    "weaptype2_txt",
    "weapsubtype2_txt",
    "weaptype3_txt",
    "weapsubtype3_txt",
    "weaptype4_txt",
    "weapsubtype4_txt",
]

def get_map_id_from_models(model):
    l = get_all_generic(model)
    return {model.city_name: model.id for model in l}

if __name__ == '__main__':
    print(get_map_id_from_models(City))