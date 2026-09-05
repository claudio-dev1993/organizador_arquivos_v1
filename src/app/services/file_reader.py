from pathlib import Path

from ..config.settings import get_source_folder


def get_files_from_origin() -> list[Path]:
    inputs = get_source_folder()

    if not inputs.exists():
        raise FileNotFoundError(
            f'Caminho de origem não encontrado: {inputs}'
        )

    return [
        file
        for file in inputs.iterdir()
        if file.is_file()
    ]