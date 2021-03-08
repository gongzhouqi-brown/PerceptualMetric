import os

from module.Deformer import get_random_deformation
from pipeline.Pipeline import Pipeline

project_folder = "D:\\Graduate\\Master\\Projects\\Metric - Danial Ritchie"
output_model_folder = "PerceptualMetric\\sample_outputs"
tutorial_model_folder = "libigl-tutorial-data"


if __name__ == '__main__':
    in_path = os.path.join(project_folder, tutorial_model_folder, "decimated-max.obj")
    out_path = os.path.join(project_folder, output_model_folder, "test.obj")
