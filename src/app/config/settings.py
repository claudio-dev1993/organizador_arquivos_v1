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
