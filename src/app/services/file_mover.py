import shutil
import logging

from ..config.settings import get_category_destination
from .file_classifier import get_file_category


def move_files(files: list, log: logging.Logger):
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
            destination_folder = get_category_destination('unrecognized')
        else:
            destination_folder = get_category_destination(category)

        destination_folder.mkdir(
            parents=True,
            exist_ok=True
        )

        try:
            shutil.move(
                str(file),
                str(destination_folder / file.name)
            )

            moved_files += 1

            log.info(
                f'Arquivo "{file.name}" movido para '
                f'"{destination_folder}".'
            )

        except PermissionError:
            log.error(
                f'O arquivo {file} não foi movido '
                f'por estar aberto ou em uso por outro programa.'
            )

        except FileNotFoundError:
            log.error(
                'O arquivo de origem não foi encontrado.'
            )

        except OSError as e:
            log.error(
                f'Ocorreu um erro no sistema operacional '
                f'ao mover o arquivo: {e}'
            )

    log.info(
        f'{moved_files} de {qty_files} arquivos '
        f'foram movidos com sucesso.'
    )