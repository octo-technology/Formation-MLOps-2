import logging
import os


def prepare_features_with_io(data_path: str, features_path: str, training_mode: bool = True) -> None:
    import pandas as pd

    from formation_mlops_2.feature_engineering import prepare_features

    data = pd.read_csv(data_path, sep=';')

    data = prepare_features(data, training_mode=training_mode)

    data.to_parquet(features_path)


def prepare_features_on_last_file_with_io(data_folder: str, features_path: str, training_mode: bool = True) -> None:
    last_file = max([file for file in os.listdir(data_folder) if file.startswith('2020')])
    logging.info(f"Preparing file {last_file}")
    prepare_features_with_io(os.path.join(data_folder, last_file), features_path, training_mode=training_mode)
