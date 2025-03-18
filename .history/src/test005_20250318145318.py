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
ptint(config.sections())             # ['section1', 'section2']
print(config.options('section1'))    # ['key1', 'key2']
print(config.get('section1', 'key1'))# value1       
print(config.getint('section1', 'key2'))# 123