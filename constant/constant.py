import subprocess
from os import path
import pathlib

home_path = subprocess.check_output(["pwd"], cwd=pathlib.Path.home()).decode("utf-8").strip()
subprocess.run(["mkdir", "-p", ".tmp"], cwd=home_path)
temp_path = path.join(home_path, ".tmp")
temp_obj = path.join(temp_path, "tmp.obj")
new_shape_net = path.join(home_path, "new_SN")
generation_path = path.join(home_path, "generated")
pivot_path = path.join(home_path, "pivots.npy")
refiner_path = path.join(home_path, "Manifold", "build")
