from app.services.file_mover import move_files
from app.services.file_reader import get_files_from_origin
from app.utils.logger import setup_logger


def main():

    try:

        log = setup_logger()

        log.info('Iniciando aplicação.')

        files = get_files_from_origin()

        move_files(
            files=files,
            log=log
        )

        log.info('Processo finalizado com sucesso.')

    except Exception as e:

        log.error(
            f'Erro global na aplicação: {e}'
        )

        log.info('O processo encerrou com falha.')

        exit(1)


if __name__ == '__main__':
    main()