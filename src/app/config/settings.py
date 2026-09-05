import json
from app.config.paths import WINDOWS_FOLDERS, APP_DATA_DIR,UNRECOGNIZED_DIR

SOURCE_FOLDER = 'Downloads'

CATEGORY_DESTINATIONS = {
    'documents': 'Documents',
    'images': 'Pictures',
    'audio': 'Music',
    'videos': 'Videos',
    'archives': 'Downloads',
    'executables': 'Downloads',
    'unrecognized': 'Downloads',
}

CONFIG_FILE = APP_DATA_DIR / 'config.json'

def get_category_destination(category: str):
    if category == 'unrecognized':
        return UNRECOGNIZED_DIR
    folder_name = CATEGORY_DESTINATIONS[category]
    return WINDOWS_FOLDERS[folder_name]

def get_source_folder():
    return WINDOWS_FOLDERS[SOURCE_FOLDER]

def load_config() -> dict:
    with open(
        CONFIG_FILE,
        'r',
        encoding='utf-8'
    ) as file:
        return json.load(file)
    
def save_config(config: dict):

    APP_DATA_DIR.mkdir(
        parents=True,
        exist_ok=True
    )

    with open(
        CONFIG_FILE,
        'w',
        encoding='utf-8'
    ) as file:

        json.dump(
            config,
            file,
            indent=4,
            ensure_ascii=False
        )