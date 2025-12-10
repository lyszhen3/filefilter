import shutil
from pathlib import Path
from typing import Optional
# 包含文件夹名称向上翻找, 翻找层数
def file_up_show(currentPath:str,includeFolderName:str, upLayers:int):
    cp = Path(currentPath)
    print(cp)
    for i in cp.iterdir():
        print(i)
        
