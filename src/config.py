import yaml
from dataclasses import dataclass

@dataclass
class Config:
    prom_servers: list[object]

def load_config(path):
    config = Config(prom_servers=[])  # Initialize the Config instance with an empty list

    with open(path, "r") as config_file:
        config_yaml = yaml.safe_load(config_file)

    if "prom_instances" in config_yaml:
        config.prom_servers = config_yaml["prom_instances"]

    return config
