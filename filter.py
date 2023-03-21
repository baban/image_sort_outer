import os
import glob
import shutil
from pprint import pprint

base_path = "/mnt/e/cg/"
script_path = os.path.dirname(os.path.abspath(__file__))
folder_txt_path = os.path.join(script_path, "folder.txt")

# Read folder.txt to get folder names and corresponding tags
def create_dic():
  folder_tags = {}
  with open(folder_txt_path, 'r') as f:
    lines = f.readlines()
    for line in lines:
      folder, tags = line.strip().split(':')
      folder_tags[folder] = [tag.strip() for tag in tags.split(',')]
  return folder_tags

folder_tags = create_dic()
pprint(folder_tags)

# Get all txt and image files in the base directory
txt_files = glob.glob(os.path.join(base_path, '*.txt'))

# 保存先のフォルダを決定する
# 引数folder_tags以下は、以下の形式のハッシュになっている
# { "フォルダ名1" => ["tag1","tag2","tag3"], "フォルダ名2" => ["tag4","tag5"] }
# txt_fileの中身はカンマ(,)区切りのタグ一覧
# 変数folder_tagsのもっているタグと、txt_fileの中のタグを見て、最初に一致するものを返す、見つからなかった場合nullを返す
def find_folder_by_tag(txt_file, folder_tags):
    tags = []
    with open(txt_file, "r") as f:
      tags = f.read().split(",")
      tags.reverse()
    for folder_name, folder_tags_list in folder_tags.items():
        for tag in tags:
            tag = tag.lower().strip()
            folder_tags_list = [t.lower().strip() for t in folder_tags_list]
            if tag in folder_tags_list:
                print("hit")
                return folder_name
    return None

def find_image_file(txt_file_path):
    # ファイル名を取得
    base_name = os.path.basename(txt_file_path)
    
    # 拡張子を変えたファイル名を生成
    name_without_ext, _ = os.path.splitext(base_name)
    image_file_name = name_without_ext + ".png"
    
    # 同じディレクトリにあるpngファイルを探す
    file_dir = os.path.dirname(txt_file_path)
    image_file_path = os.path.join(file_dir, image_file_name)
    
    if os.path.exists(image_file_path):
        return image_file_path
    
    # pngファイルがなければ、jpgファイルも探す
    image_file_name = name_without_ext + ".jpg"
    image_file_path = os.path.join(file_dir, image_file_name)
    
    if os.path.exists(image_file_path):
        return image_file_path
    
    # pngファイルがなければ、jpgファイルも探す
    image_file_name = name_without_ext + ".jpeg"
    image_file_path = os.path.join(file_dir, image_file_name)
    
    if os.path.exists(image_file_path):
        return image_file_path

    # 見つからなかった場合はNoneを返す
    return None

# 移動させる
for txt_file in txt_files:
  print(txt_file)
  folder = find_folder_by_tag(txt_file, folder_tags)
  print(folder)
  img_file = find_image_file(txt_file)
  print(img_file)
  if None == folder:
     folder = 'other'
  target_folder = os.path.join(base_path, folder)
  if not os.path.exists(target_folder):
    os.makedirs(target_folder)
  print(target_folder)
  shutil.move(img_file, os.path.join(target_folder, os.path.basename(img_file)))
  shutil.move(txt_file, os.path.join(target_folder, os.path.basename(txt_file)))
