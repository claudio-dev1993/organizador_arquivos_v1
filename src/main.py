from datetime import datetime
from pathlib import Path
import logging
import shutil

PATH_HOME = Path.home()

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

def clear_logs(log_path: Path, file_limit: int):
        try:
            file_count = 0
            files = []
            for item in log_path.iterdir():
                if item.is_file():
                    file_count += 1
                    files.append(item)
                    if file_count < file_limit:
                        continue
                    elif file_count >= file_limit:
                        for file in files:
                            try:
                                file.unlink()
                            except PermissionError:
                                continue
                    break
        except TypeError as e:
            print(f'Failed to clear files: {e}')
        except AttributeError as e:
            print(f'Failed to clear files: {e}')

def setup_logger() -> logging.Logger:
    try:
        logger = logging.getLogger('ORGANIZADOR ARQUIVOS')
        logger.setLevel(logging.INFO)

        if not logger.handlers:
            base_dir = PATH_HOME / 'Downloads'
            log_dir = base_dir/ 'logs_organizador_arquivos'
            log_dir.mkdir(parents=True, exist_ok=True)
            log_filename = log_dir / f"{datetime.now().strftime('%d-%m-%Y_%H%M%S')}.log"

            formatter = logging.Formatter(fmt='%(asctime)s - [%(name)s] - %(levelname)s - %(message)s',
                                          datefmt='%Y-%m-%d %H:%M:%S')
            
            clear_logs(log_path=log_dir, file_limit=10)
            
            file_handler = logging.FileHandler(filename=log_filename, encoding='utf-8', mode='a')
            file_handler.setFormatter(formatter)
            logger.addHandler(file_handler)

            console_handler = logging.StreamHandler()
            console_handler.setFormatter(formatter)
            logger.addHandler(console_handler)

        return logger
    except PermissionError as e:
        print(f'Erro ao criar arquivo de log: {e}')
 
def get_files_from_origin(origin_path: str) -> list:
    inputs = PATH_HOME / origin_path
    if not inputs.exists():
        raise FileNotFoundError(f'Caminho de origem não encontrado: {inputs}')
    return [file for file in inputs.iterdir() if file.is_file()]

def move_files(files:list, log: logging.Logger):
            log = setup_logger()
            qty_files = len(files)
            moved_files = 0
            
            if qty_files == 0:
                log.info('Nenhum arquivo para movimentação.')
                return
            log.info(f'Movendo {qty_files} arquivos para pastas destino.')
    
            for file in files:
                category = get_file_category(file)

                if category is None:
                   log.warning(f'Arquivo sem extensão definida ou não suportado: {file.name}')
                   base_dir = PATH_HOME / 'Downloads'
                   no_extension_file_dir = base_dir/ 'nao_reconhecido'
                   no_extension_file_dir.mkdir(parents=True, exist_ok=True)
                   shutil.move(str(file),str(no_extension_file_dir / file.name))
                   continue
                
                destination_folder = category['destination']
                destination_folder.mkdir( parents=True, exist_ok=True)
                
                try:
                    shutil.move(str(file),str(destination_folder / file.name))
                except PermissionError as e:
                    log.error(f"O arquivo {file} Não foi movido por estar aberto ou em uso por outro programa.")
                    continue
                except FileNotFoundError:
                    log.error("O arquivo de origem não foi encontrado.")
                    continue
                except OSError as e:
                    log.error(f"Ocorreu um erro no sistema operacional ao mover o arquivo: {e}")
                    exit(1)
                    
                moved_files += 1
    
                log.info(f'Arquivo "{file.name}" movido para "{destination_folder}".')
                
            log.info(f'{moved_files} de {qty_files} arquivos foram movidos com sucesso.')

def main():
    try:
        log = setup_logger()
        log.info('Iniciando aplicação.')
        files = get_files_from_origin(origin_path='Downloads')
        move_files(files=files, log=log)
        log.info('Processo finalizado com sucesso.')
        
    except Exception as e:
        log.error(f'Erro global na aplicação: {e}')
        log.info('O processo encerrou com falha.')
        exit(1)

if __name__ == '__main__':
    main()