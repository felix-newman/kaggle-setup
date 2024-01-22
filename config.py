from pathlib import Path
import wandb


class CFG:
    # ============== comp exp name =============
    comp_name = 'comp_name'
    exp_name = 'experiment_name'

    train_batch_size = 8  # 32
    valid_batch_size = train_batch_size * 2

    epochs = 1  # 30

    max_lr = 3e-4

    weight_decay = 0

    seed = 42

    mode = "train"

    project_home = Path(__file__).parent
    comp_download_path = project_home / 'data'

    outputs_path = project_home / exp_name
    model_dir = outputs_path / "models"

    def __init__(self):
        wandb.init(project=self.comp_name)
        wandb.run.log_code(self.project_home)
        wandb_config = wandb.config

        # overwrite config values with wandb values, as those might come from a sweep
        wandb_attributes = wandb_config.as_dict()
        for key, value in wandb_attributes.items():
            setattr(self, key, value)

        # sync local config values to wandb
        config_attributes = filter(lambda x: not x.startswith('__'), dir(self))
        add_attrs_config = set(config_attributes) - set(wandb_attributes)
        for attr in add_attrs_config:
            value = getattr(self, attr)
            setattr(wandb_config, attr, value)


