from omegaconf import OmegaConf
import addict 

# class ConfigDict(addict.Dict):
#     # Borrowed from https://github.com/open-mmlab/mmcv/blob/master/mmcv/utils/config.py
#     def __missing__(self, name):
#         raise KeyError(name)
#     def __getattr__(self, name):
#         try:
#             value = super().__getattr__(name)
#         except KeyError:
#             ex = AttributeError(f"'{self.__class__.__name__}' object has no attribute '{name}'")
#         except Exception as e:
#             ex = e
#         else:
#             return value
#         raise ex

# def load_config(path: str):
#     cfg = OmegaConf.load(path)
#     cfg = ConfigDict(OmegaConf.to_container(cfg, resolve=True)) # Resolve in advance.
#     return cfg

conf = OmegaConf.load('config.yaml')

print(conf.s_val)

# print(load_config('config.yaml').s_val)