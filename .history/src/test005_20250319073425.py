from configparser import ConfigParser

config = ConfigParser()

# セクションとキーを指定して値を設定
config['section1'] = {'key1': 'value1', 'key2': '123'}
config['section2'] = {'flag': 'True'}

# 設定ファイルを書き込み
with open('config.ini', 'w') as configfile:
    config.write(configfile)
    
# 設定ファイルを読み込み
config.read('config.ini')

# セクションとキーを指定して値を取得
print(config['section1']['key1'])   # value1
print(config['section1']['key2'])   # 123
print(config['section2']['flag'])   # True  
print(config.sections())             # ['section1', 'section2']
print(config.options('section1'))    # ['key1', 'key2']
print(config.get('section1', 'key1'))# value1       
print(config.getint('section1', 'key2'))# 123

import time

def timer(func):
    """関数の実行時間を計測するデコレーター"""
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"関数 {func.__name__} の実行時間: {end_time - start_time:.4f} 秒")
        return result
    return wrapper

@timer
def slow_function(n):
    """時間がかかる関数"""
    time.sleep(n)
    return n * 2

@timer
def fast_function(n):
    """すぐに終わる関数"""
    return n * 2

# 関数の実行
slow_function(2)
fast_function(3)
