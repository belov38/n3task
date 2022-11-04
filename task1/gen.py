import argparse
from genlib.core import parse_column_data, write_table

parser = argparse.ArgumentParser(
    exit_on_error=False,
    usage='''
%(prog)s [--rows ROWS] [--output_path OUTPUT_PATH] --column_data COLUMN_DATA

examples:
%(prog)s --column_data="[('x', 'string'), ('y','integer'),('z','integer')]"
%(prog)s --column_data="[('x', 'string'), ('y','integer'),('z','integer')]" --rows=10
%(prog)s --column_data="[('x', 'string'), ('y','integer'),('z','integer')]" --rows=10 --output_path=/tmp
    '''
)
parser.add_argument("--rows", help="the number of rows in the output CSV file (default = 50)", type=int, default=50)
parser.add_argument("--output_path", help="path to the output CSV file (default = '.')", type=str, default=".")
parser.add_argument("--column_data", help="name and type definitions for the row. The type of the argument can be "
                                          "`integer` or `string`.", type=str, required=True)
args = parser.parse_args()

if __name__ == "__main__":
    try:
        column_data = parse_column_data(args.column_data)
        write_table(rows=args.rows, output_path=args.output_path, column_data=column_data)
        print('*' * 30)
        print('File {}/result.csv generated successfully'.format(args.output_path))
    except ValueError as e:
        print('Parameters error:', e)
        parser.print_help()
    except Exception as e:
        print('Error occurred:', e)
        parser.print_help()
