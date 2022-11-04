# File generation application
The program generate result.csv file with specified count of rows (default=50).

Column data must be specified via --column_data.

Each rows populate with random data.

## Usage
Generate _result.csv_ in local folder with 2 columns and 50 (default value) rows. 

The first column name is X.  Each rows will fill up by random **string** value.

The second column name is Y. Each rows will fill up by random **integer** value.
```shell
python gen.py --column_data="[('x', 'string'), ('y','integer')]"
```

Generate _/tmp/result.csv_ with 2 columns and 4 rows. 

The first column name is X.  Each rows will fill up by random **string** value.

The second column name is Y. Each rows will fill up by random **integer** value.

The third column name is Z. Each rows will fill up by random **integer** value.
```shell
python gen.py --column_data="[('x', 'string'), ('y','integer'),('z','integer')]" --rows=4 --output_path=/tmp
```

## Testing

```shell
python -m unittest tests/test_gen.py
```