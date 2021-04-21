import json
import os
from os import listdir
from os.path import join
import numpy as np

root = os.getenv("SHAPENET_HOME")
assert root is not None

MODEL_FOLDER = "models"
OBJECT_EXT = ".obj"
TAXONOMY = "taxonomy.json"

NOT_FOUND = "NO_OBJ_FILE_HERE"


def _get_lv1():
    ls = listdir(root)
    lv1 = [f for f in ls if os.path.isdir(join(root, f))]
    return lv1


def iterate_shape_net():
    lv1 = _get_lv1()
    for f1 in lv1:
        full_f1 = join(root, f1)
        lv2 = listdir(full_f1)
        for f2 in lv2:
            full_f2 = join(full_f1, f2, MODEL_FOLDER)
            lv3 = listdir(full_f2)
            for f3 in lv3:
                if f3.endswith(OBJECT_EXT):
                    yield join(full_f2, f3)


def random_shape_net_object():
    res = None
    while res is None:
        lv1 = _get_lv1()
        f1 = np.random.choice(lv1)
        full_f1 = join(root, f1)
        lv2 = listdir(full_f1)
        f2 = np.random.choice(lv2)
        full_f2 = join(full_f1, f2, MODEL_FOLDER)
        lv3 = listdir(full_f2)
        for f3 in lv3:
            if f3.endswith(OBJECT_EXT):
                res = join(full_f2, f3)
    return res


def _count_shape_net():
    total = 0
    nones = 0

    lv1 = _get_lv1()
    for f1 in lv1:
        full_f1 = join(root, f1)
        lv2 = listdir(full_f1)
        for f2 in lv2:
            full_f2 = join(full_f1, f2, MODEL_FOLDER)
            lv3 = listdir(full_f2)
            found = False
            for f3 in lv3:
                if f3.endswith(OBJECT_EXT):
                    found = True
                    break
            if found:
                total += 1
            else:
                nones += 1
    print(total)
    print(nones)


def _stat_taxonomy():
    total = 0
    with open(join(root, TAXONOMY)) as f:
        data = json.load(f)
    lv1 = _get_lv1()
    for d in data:
        if d["synsetId"] in lv1:
            total += d["numInstances"]
    print(total)


def _test_shape_net_complete():
    with open(join(root, TAXONOMY)) as f:
        data = json.load(f)
    exist = set()
    lv1 = _get_lv1()
    count = 0
    for d in data:
        for child in d["children"]:
            exist.add(child)
        if d["synsetId"] not in exist:
            exist.add(d["synsetId"])
            count += 1
            if d["synsetId"] in lv1:
                lv1.remove(d["synsetId"])
                tax_count = d["numInstances"]
                full_f1 = join(root, d["synsetId"])
                lv2 = listdir(full_f1)
                real_count = len(lv2)
                print(count, tax_count == real_count)
            else:
                print(d["synsetId"], d["name"])
    print(lv1)


if __name__ == '__main__':
    _count_shape_net()
    _stat_taxonomy()
    _test_shape_net_complete()
