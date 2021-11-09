import os,json
import yaml
from config import RunConfig

class Readyaml():

    def read(self):
        item = []
        with open('{}/config.yaml'.format(RunConfig.PRO_PATH), 'r',encoding="utf-8") as f:
            load_dict = f.read()
            f.close()
        load_dict = yaml.load(load_dict, Loader=yaml.FullLoader)
        return list(load_dict)