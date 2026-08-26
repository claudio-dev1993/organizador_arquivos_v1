from datetime import datetime
import os
from pathlib import Path
import logging
import shutil

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
            base_dir = Path(__file__).resolve().parent
            log_dir = base_dir.parent / 'logs'
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
 

def main():
    try:
        log = setup_logger()
        log.info('Iniciando aplicação.')
        
        src_dir = Path(__file__).parent.resolve()
        inputs = src_dir.parent / 'inputs'
        outputs = src_dir.parent / 'outputs'
        files = os.listdir(inputs)
        qty_files = len(files)
        
        if not inputs.exists():
            log.error('Erro ao acessar pasta de origem.')
            raise Exception('Caminho de origem não encontrado')
        
        if qty_files > 0:
            log.info(f'Movendo {qty_files} arquivos para pastas destino.')
            doc_file_suffixes = ('.pdf', '.txt', '.xlsx', '.md')
            img_file_suffixes = ('.jpeg', '.jpg')
            
            
            for file in files:
                
                if file.endswith(doc_file_suffixes):
                    shutil.move(inputs/file,outputs/'docs')
                    log.info(f'Arquivo: {file} movido para docs.')
                elif file.endswith(img_file_suffixes):
                    shutil.move(inputs/file,outputs/'img')
                    log.info(f'Arquivo: {file} movido para img.')
                    
            log.info(f'{len(files)} arquivos foram movidos com sucesso.')
        else:
            log.info('Nenhum arquivo para movimentação.')
            exit(0)
            
    except Exception as e:
        print(f'Erro global na aplicação: {e}')
        exit(1)


if __name__ == '__main__':
    main()