import ast
import csv
import random
import string


def parse_column_data(column_data: str):
    result = ast.literal_eval(column_data)
    if type(result) != list:
        raise ValueError('column_data must be a list')

    err_message = 'each element of column_data must be a tuple (field_name, field_type), where field_type = "string" ' \
                  'or "integer" '
    for i in result:
        if type(i) != tuple:
            raise ValueError(err_message)

        if len(i) != 2:
            raise ValueError(err_message)

        if (i[1] != 'integer') and (i[1] != 'string'):
            raise ValueError(err_message)
    return result


def make_row(column_data: list):
    result = []
    for record in column_data:
        match record[1]:
            case 'string':
                s = ''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase, k=random.randint(1, 10)))
                result.append(s)
            case 'integer':
                result.append(random.randint(0, 32767))
            case _:
                raise ValueError()
    return result


def write_table(rows: int, output_path: str, column_data: list):
    # TODO: check FS permissions
    # TODO: Ask to overwrite an old file?
    with open('{}/result.csv'.format(output_path), 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)

        header = map(lambda x: x[0], column_data)
        csvwriter.writerow(header)

        for r in range(rows):
            csvwriter.writerow(make_row(column_data))
