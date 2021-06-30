import json
import logging
from datetime import datetime
from typing import List


def main():
    queries: List[str] = []
    input_file_name: str = input('\033[33;1mInput file name (without extension): \033[m').strip()

    try:
        with open('input/{}.sql'.format(input_file_name)) as in_file:
            input_query: str = in_file.read()
    except Exception as e:
        logging.error('Failed to access the input file: {}'.format(e))
        raise e

    output_file_name: str = input('\033[33;1mChoose a name to the output file (without extension): \033[m').strip()

    if output_file_name is None or output_file_name == '':
        output_file_name = 'query'

    try:
        with open('schemas.json') as file:
            schemas: List[str] = json.loads(file.read())

            for schema in schemas:
                queries.append(input_query.replace('per_unity', schema))

            with open('out/{}-{}.sql'.format(
                output_file_name, int(datetime.timestamp(datetime.now()))
            ), 'w') as out:
                out.write(''.join(queries))
    except Exception as e:
        logging.log('Failed to write file: {}'.format(e))
        raise e

    print('\033[32mDone!\033[m')


if __name__ == '__main__':
    main()
