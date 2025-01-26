import argparse

def main():
    parser = argparse.ArgumentParser(description='パラメタをargparseで定義するプログラム')
    parser.add_argument('--param1', type=int, help='整数型のパラメタ1')
    parser.add_argument('--param2', type=str, help='文字列型のパラメタ2')
    args = parser.parse_args()

    print(f'param1: {args.param1}')
    print(f'param2: {args.param2}')

if __name__ == '__main__':
    main()
