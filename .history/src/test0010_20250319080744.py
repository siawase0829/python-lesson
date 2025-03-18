from pathlib import Path

# /Users/aratakekouji/python実践レシピ/src/test005.pyを基準に考える
parent_dir = Path('/Users/aratakekouji/python実践レシピ/src')
file_name = 'test005.py'

# / 演算子を使ってパスを結合
file_path = parent_dir / file_name
print(file_path)  # 出力: /Users/aratakekouji/python実践レシピ/src/test005.py

# 複数のパスを結合
new_dir = parent_dir / 'new_folder' / 'sub_folder'
print(new_dir) # 出力: /Users/aratakekouji/python実践レシピ/src/new_folder/sub_folder
