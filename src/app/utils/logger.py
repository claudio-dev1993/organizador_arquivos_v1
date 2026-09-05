from datetime import datetime
from pathlib import Path
import logging

from app.config.paths import PATH_HOME


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

        logger = logging.getLogger(
            'ORGANIZADOR ARQUIVOS'
        )

        logger.setLevel(logging.INFO)

        if not logger.handlers:

            base_dir = PATH_HOME / 'Downloads'

            log_dir = (
                base_dir / 'logs_organizador_arquivos'
            )

            log_dir.mkdir(
                parents=True,
                exist_ok=True
            )

            log_filename = (
                log_dir /
                f"{datetime.now().strftime('%d-%m-%Y_%H%M%S')}.log"
            )

            formatter = logging.Formatter(
                fmt=(
                    '%(asctime)s - [%(name)s] - '
                    '%(levelname)s - %(message)s'
                ),
                datefmt='%Y-%m-%d %H:%M:%S'
            )

            clear_logs(
                log_path=log_dir,
                file_limit=10
            )

            file_handler = logging.FileHandler(
                filename=log_filename,
                encoding='utf-8',
                mode='a'
            )

            file_handler.setFormatter(formatter)

            logger.addHandler(file_handler)

            console_handler = logging.StreamHandler()

            console_handler.setFormatter(formatter)

            logger.addHandler(console_handler)

        return logger

    except PermissionError as e:
        print(f'Erro ao criar arquivo de log: {e}')