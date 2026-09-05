from app.config.paths import PATH_HOME


def get_files_from_origin(origin_path: str) -> list:

    inputs = PATH_HOME / origin_path

    if not inputs.exists():

        raise FileNotFoundError(
            f'Caminho de origem não encontrado: {inputs}'
        )

    return [
        file
        for file in inputs.iterdir()
        if file.is_file()
    ]