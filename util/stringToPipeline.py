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


if __name__ == '__main__':
    s = r"running:  <class 'ARAPDeformer.ARAPDeformer'> {'t_x': 0.17452382898180496, 't_y': 0.9558142037374558, 't_z': 0.17554714089210588, 'theta': 0.3248054820202535, 'phi': 0.38593245151476946, 'pivots': 0.30801496618673907} <class 'ARAPDeformer.ARAPDeformer'> {'t_x': 0.9639162147961376, 't_y': 0.7045277010357479, 't_z': 0.446836720467392, 'theta': 0.33898987780096346, 'phi': 5.765834227010479, 'pivots': 0.6433526366636744} <class 'VoxelizeDeformer.VoxelizeDeformer'> {'cubes': 128.0} <class 'SubdivisionDeformer.SubdivisionDeformer'> {'steps': 1.0} <class 'BiharmonicDeformer.BiharmonicDeformer'> {'pivots': 2.0, 'first': 0.28020587801491104, 'second': 0.38496145693531647, 'third': 0.5286882267638572, 'fourth': 0.6751136390645117} <class 'SubdivisionDeformer.SubdivisionDeformer'> {'steps': 1.0} <class 'LengthDeformer.LengthDeformer'> {'x': 1.4089293164363927, 'y': 1.0340056369418966, 'z': 0.7306413257535977} "


    in_f = r"/home/zgong8/ShapeNetCore.v2/02747177/4117be347627a845ba6cf6cbb9f4c2bb/models/model_normalized.obj"
    out_f = r"/home/zgong8/PerceptualMetric/debug/out{}.obj"
    ps = string_to_pipelines(s)
    for i, p in enumerate(ps):
        p.process_shape_file(in_f, out_f.format(i))
        in_f = out_f.format(i)
        print(i, "done")