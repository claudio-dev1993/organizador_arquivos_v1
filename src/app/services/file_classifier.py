from pathlib import Path

from app.config.file_categories import FILE_CATEGORIES
from app.config.paths import PATH_HOME


def get_file_category(file: Path) -> dict | None:

    suffix = file.suffix.lower()

    for category, config in FILE_CATEGORIES.items():

        if suffix in config['suffixes']:
            return config

    return None


def get_destination_folder(category: str) -> Path:

    windows_folders = {
        'Documents': PATH_HOME / 'Documents',
        'Pictures': PATH_HOME / 'Pictures',
        'Music': PATH_HOME / 'Music',
        'Videos': PATH_HOME / 'Videos',
        'Downloads': PATH_HOME / 'Downloads',
    }

    return windows_folders[category]