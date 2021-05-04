import igl
import trimesh
import numpy as np

from data.ShapeNet import iterate_shape_net


def refine(v, f):
    """
    Refine the object to ensure the whole object is connected and normalized
    :param v: vertices
    :param f: faces
    :return: refined vertices and faces
    """
    # TODO: Implement this
    return v, f

def connect_sperate_component(v, f):
    """
    Run a union operation if more than one sperated components has been found for a given mesh
    :param v: vertices
    :param f: faces
    :return: connected vertices and faces
    """ 
    T = trimesh.Trimesh(v, f)
    components = trimesh.graph.connected_components(T.edges, engine='scipy')
    num_of_components = len(components)
    if num_of_components > 1:
        num_of_vertices = v.shape[0]
        map_v2subv = [-1] * num_of_vertices # old vid to component id
        map_vid = [-1] * num_of_vertices # old vid to new vid
        faces = [[] for i in range(num_of_components)]
        vertices = [[None for j in range(len(components[i]))] for i in range(num_of_components)]
        
        for i in range(num_of_components):
            for newvid, oldvid in enumerate(components[i]):
                map_vid[oldvid] = newvid
                map_v2subv[oldvid] = i
                vertices[i][newvid] = T.vertices[oldvid]
                
        for (a, b, c) in T.faces:
            cid = map_v2subv[a]
            faces[cid].append([map_vid[a], map_vid[b], map_vid[c]])

        meshes = [trimesh.Trimesh(vertices[i], faces[i]) for i in range(num_of_components)]
        newmesh = trimesh.boolean.union(meshes, engine="blender")

        return newmesh.vertices, newmesh.faces
    else:
        return v, f


def count_shape_net_components():
    total = 0
    counter = 0
    for in_file in iterate_shape_net():
        v, f = igl.read_triangle_mesh(in_file, np.float64)

        tm = trimesh.Trimesh(v, f)

        components = trimesh.graph.connected_components(tm.edges, engine='scipy')
        num_of_components = len(components)

        if num_of_components > 1:
            counter += 1
        total += 1
    print(counter, "out of", total)
