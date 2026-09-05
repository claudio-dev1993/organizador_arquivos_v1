from pathlib import Path


PATH_HOME = Path.home()

WINDOWS_FOLDERS = {
    'Downloads': PATH_HOME / 'Downloads',
    'Documents': PATH_HOME / 'Documents',
    'Pictures': PATH_HOME / 'Pictures',
    'Music': PATH_HOME / 'Music',
    'Videos': PATH_HOME / 'Videos',
}

APP_DATA_DIR = (
    PATH_HOME
    / 'AppData'
    / 'Roaming'
    / 'OrganizadorArquivos'
)

LOG_DIR = APP_DATA_DIR / 'logs_organizador_arquivos'


UNRECOGNIZED_DIR = WINDOWS_FOLDERS['Downloads'] / 'nao_categorizados'

