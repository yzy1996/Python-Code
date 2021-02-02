import yaml

with open('config.yaml') as f:
    config = yaml.safe_load(f)
    
print(config)
