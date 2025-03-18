import configparser

config = configparser.ConfigParser()

# セクションとキーを指定して値を設定
config['section1'] = {'key1': 'value1', 'key2': '123'}
config['section2'] = {'flag': 'True'}

# 設定ファイルを書き込み
with open('config.ini', 'w') as configfile:
    config.write(configfile)