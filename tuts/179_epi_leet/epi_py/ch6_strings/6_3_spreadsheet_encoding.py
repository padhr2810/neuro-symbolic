import functools

#from test_framework import generic_test


def ss_decode_col_id(col: str) -> int:
    print("##############################################")
    print(f"col = {col}")
    print(f"ord('A') + 1 = {ord('A') + 1}")
    print(f"ord('0') = {ord('0')}")
    
    res = 0 
    for c in col:
        res *= 26
        res = res + ord(c) - ord('A') + 1
    return res 
    #return functools.reduce(
    #    lambda result, c: result * 26 + ord(c) - ord('A') + 1, col, 0)


if __name__ == '__main__':
    print(ss_decode_col_id("A"))
    print(ss_decode_col_id("Z"))
    print(ss_decode_col_id("AB"))
    print(ss_decode_col_id("AZ"))
    
    #exit(
    #    generic_test.generic_test_main('spreadsheet_encoding.py',
    #                                   'spreadsheet_encoding.tsv',
    #                                   ss_decode_col_id))
