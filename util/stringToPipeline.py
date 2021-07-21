import re
import json

from module.Deformer import name_to_deformation
from pipeline.Pipeline import Pipeline



def string_to_pipeline(string):
    each_deformation_finder = re.compile("<.*?}")
    deformation_strings = each_deformation_finder.findall(string)
    p = Pipeline(len(deformation_strings))
    for deformation_string in deformation_strings:
        p.plug(substring_to_deformation(deformation_string))
    return p


def string_to_pipelines(string):
    each_deformation_finder = re.compile("<.*?}")
    deformation_strings = each_deformation_finder.findall(string)
    pipelines = []
    for deformation_string in deformation_strings:
        p = Pipeline(1)
        p.plug(substring_to_deformation(deformation_string))
        pipelines.append(p)
    return pipelines


def substring_to_deformation(substring):
    class_name_finder = re.compile("<class '(.*)'> {.*}")
    config_finder = re.compile("{.*}")
    class_name = class_name_finder.findall(substring)[0].split(".")[0]
    config_str = config_finder.findall(substring)[0].replace("'", '"')
    configs = json.loads(config_str)
    return name_to_deformation(class_name, configs)
