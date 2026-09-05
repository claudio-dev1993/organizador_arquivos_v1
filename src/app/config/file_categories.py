from app.config.paths import PATH_HOME


FILE_CATEGORIES = {

    'documents': {
        'suffixes': (
            '.pdf',
            '.txt',
            '.doc',
            '.docx',
            '.xls',
            '.xlsx',
            '.csv',
            '.md',
            '.rtf',
            '.odt',
        ),
        'destination': PATH_HOME / 'Documents',
    },

    'images': {
        'suffixes': (
            '.jpg',
            '.jpeg',
            '.png',
            '.gif',
            '.bmp',
            '.tiff',
            '.webp',
            '.svg',
        ),
        'destination': PATH_HOME / 'Pictures',
    },

    'audio': {
        'suffixes': (
            '.mp3',
            '.wav',
            '.flac',
            '.aac',
            '.ogg',
            '.m4a',
            '.wma',
        ),
        'destination': PATH_HOME / 'Music',
    },

    'videos': {
        'suffixes': (
            '.mp4',
            '.avi',
            '.mkv',
            '.mov',
            '.wmv',
            '.flv',
            '.webm',
        ),
        'destination': PATH_HOME / 'Videos',
    },

    'archives': {
        'suffixes': (
            '.zip',
            '.rar',
            '.7z',
            '.tar',
            '.gz',
            '.bz2',
        ),
        'destination': PATH_HOME / 'Downloads',
    },

    'executables': {
        'suffixes': (
            '.exe',
            '.msi',
            '.bat',
            '.cmd',
            '.com',
            '.ini',
        ),
        'destination': PATH_HOME / 'Downloads',
    },
}