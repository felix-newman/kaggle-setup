import os
import torch

import pytorch_lightning as pl
from torch.utils.data import Dataset, DataLoader

import random

class VesuviusDataModule(pl.LightningDataModule):
    def __init__(self, config: CFG):
        super().__init__()
        self.config = config


    def prepare_data(self):
        if not self.config.comp_download_path.exists() and self.config.mode == "train":
            os.environ['KAGGLE_USERNAME'] = "felixmneumann"  # username from the json file
            api_key = input("Kaggle API Key")
            os.environ['KAGGLE_KEY'] = api_key  # key from the json file

            import kaggle
            kaggle.api.authenticate()
            self.config.comp_download_path.mkdir()

            raise Exception("Dataset missing")
            # kaggle.api.dataset_download_files("felixmneumann/vesuvius", path=self.config.comp_download_path, unzip=True)

    def setup(self, stage: str) -> None:
        if stage == "fit":

            self.train_dataset = #
            self.val_dataset = #

        if stage == "validate":
            self.val_dataset = #

        if stage == "predict":
            self.val_dataset = #


    def _get_num_workers(self):
        import sys

        # Get the operating system
        operating_system = sys.platform

        # Check if it's Linux
        if operating_system.startswith('linux'):
            return 8
        else:
            return 0

    def train_dataloader(self):
        num_workers = self._get_num_workers()
        if num_workers > 0:
            return DataLoader()
        else:
            return DataLoader()

    def val_dataloader(self):
        num_workers = self._get_num_workers()
        if num_workers > 0:
            return DataLoader()
        else:
            return DataLoader()

    def predict_dataloader(self):
        return DataLoader()
