from models import *
from logic import monaco, cli

data = {'abb': cli.get_file_content('../data', 'abbreviations.txt'),
        'start': cli.get_file_content('../data', 'start.log', True, '_', 3),
        'end': cli.get_file_content('../data', 'end.log', True, '_', 3)}

report = monaco.build_report(data)


def create_tables():
    # Creates a table in the database.
    with db:
        db.create_tables([Racer])
        Racer.insert_many(report).execute()


if __name__ == '__main__':
    create_tables()
