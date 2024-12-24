from data_management_app.db.sql_db.repositories.postgres_repository.postgres_crud import get_all_generic


def get_map_id_from_models(model):
    l = get_all_generic(model)
    return {model.name: model.id for model in l}