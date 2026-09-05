import logging
import shutil
from app.config.paths import PATH_HOME
from app.services.file_classifier import get_file_category


def move_files(files: list, log: logging.Logger):

    qty_files = len(files)
    moved_files = 0

    if qty_files == 0:
        log.info('Nenhum arquivo para movimentação.')
        return

    log.info(
        f'Movendo {qty_files} arquivos para pastas destino.'
    )

    for file in files:

        category = get_file_category(file)

        if category is None:

            log.warning(
                f'Arquivo sem extensão definida ou não suportado: '
                f'{file.name}'
            )

            base_dir = PATH_HOME / 'Downloads'

            no_extension_file_dir = (
                base_dir / 'nao_reconhecido'
            )

            no_extension_file_dir.mkdir(
                parents=True,
                exist_ok=True
            )

            shutil.move(
                str(file),
                str(no_extension_file_dir / file.name)
            )

            continue

        destination_folder = category['destination']

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
                f'Arquivo "{file.name}" '
                f'movido para "{destination_folder}".'
            )

        except PermissionError:

            log.error(
                f'O arquivo {file} não foi movido por estar aberto '
                f'ou em uso por outro programa.'
            )

            continue

        except FileNotFoundError:

            log.error(
                'O arquivo de origem não foi encontrado.'
            )

            continue

        except OSError as e:

            log.error(
                'Ocorreu um erro no sistema operacional '
                f'ao mover o arquivo: {e}'
            )

            exit(1)

    log.info(
        f'{moved_files} de {qty_files} arquivos '
        f'foram movidos com sucesso.'
    )