from models import *
import cli
import monaco

data = {'abb': cli.get_file_content('data', 'abbreviations.txt'),
        'start': cli.get_file_content('data', 'start.log', True, '_', 3),
        'end': cli.get_file_content('data', 'end.log', True, '_', 3)}

report = monaco.build_report(data)


with db:
    db.create_tables([Racer])
    Racer.insert_many(report).execute()

print("DONE")
