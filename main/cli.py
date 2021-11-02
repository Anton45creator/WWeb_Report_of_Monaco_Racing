import click
import os
import monaco


def get_file_content(folder_path, filename, insert_char=False, char='', pos=0):
    """Get data from file"""

    file_path = os.path.join(os.path.abspath(folder_path), filename)
    with open(file_path, 'r') as f:
        if insert_char:
            lines = f.readlines()
            lines_new = []
            for line in lines:
                lines_new.append(f'{line[:pos]}{char}{line[pos:]}')
            content = ''.join(lines_new)
            return content
        else:
            content = f.read()
            return content


@click.command()
@click.option('--files', required=True, type=click.Path(
    exists=True, file_okay=False, dir_okay=True,
    readable=True, resolve_path=True), help='Path to folder with files')
@click.option('--driver', help='Driver name.')
@click.option('--desc', is_flag=True, help='Order desc.')
def main(files, driver, desc):
    """The program that print the report of Monaco 2018 Racing."""

    data = {'abb': get_file_content(files, 'abbreviations.txt'),
            'start': get_file_content(files, 'start.log', True, '_', 3),
            'end': get_file_content(files, 'end.log', True, '_', 3)}

    if not desc:
        report = monaco.build_report(data)
    else:
        report = monaco.build_report(data, False)

    monaco.print_report(report, driver)


if __name__ == '__main__':
    main()
