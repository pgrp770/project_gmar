from statistics_app.db.sql_db.repostiories.terror_attack_repository import get_all_terror_attacks
import toolz as tz

def foo():
    return tz.pipe(
        get_all_terror_attacks()[0],

    )



if __name__ == '__main__':
    print(foo())