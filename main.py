from collections.abc import Generator
from pathlib import Path
from os import *



l_path = Path("G:\\")


def showStats(path_object: Path) -> Generator[Path, None, None]:
    print('The directory is block device? \n', path_object.is_block_device())
    yield listdir(path_object)

while True:
    for i in showStats(l_path):
        print(i,'\n')
    break