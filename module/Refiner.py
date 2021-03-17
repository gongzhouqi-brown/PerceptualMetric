import igl
import trimesh
import bpy

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
    T = trimesh.Trimesh(v, f)
    num_of_components = len(components)
    num_of_vertices = v.shape[0]
    map_v2subv = [-1] * num_of_vertices # old vid to component id
    map_vid = [-1] * num_of_vertices # old vid to new vid
    faces = [[] for i in range(num_of_components)]
    vertices = [[-1 for j in range(len(components[i]))] for i in range(num_of_components)]
    
    for i in range(num_of_components):
        for newvid, oldvid in enumerate(components[i]):
            map_vid[oldvid] = newvid
            map_v2subv[oldvid] = i
            vertices[i][newvid] = v[oldvid]
            
    for (a, b, c) in f:
        cid = map_v2subv[a]
        faces[i].append([map_vid[a], map_vid[b], map_vid[c]])
            
    meshes = [trimesh.Trimesh(v = vertices[i], f = faces[i]) for i in range(num_of_components)]

    newmesh = trimesh.boolean.union(meshes, engine="blender")
    return newmesh.vertices, newmesh.faces
