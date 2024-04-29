import open3d as o3d
import numpy as np
from pprint import pprint
import trimesh
import pickle
import os
from shutil import copyfile
import glob
import pyglet
import pandas as pd
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import pymeshlab
import json
import random
from pathlib import Path
import numpy as np
import os
import torch
import torch.utils.data as data
import trimesh
import copy
import csv

def clean_mesh(data_path, outputpath):
    ms = pymeshlab.MeshSet()
    ms.load_new_mesh(data_path)
    ms.meshing_remove_duplicate_faces()
    ms.meshing_remove_duplicate_vertices()
    ms.meshing_remove_unreferenced_vertices()
    ms.meshing_remove_folded_faces()
    ms.meshing_remove_null_faces()
    ms.meshing_repair_non_manifold_edges(method=0)
    ms.meshing_close_holes(maxholesize=3000000,selfintersection=False)
    ms.save_current_mesh(outputpath, save_face_color=False)

    return mesh

if __name__ == '__main__':
    root = 'C:/Users/boyua/PycharmProjects/MeshMAE-mesh/dataset/mesh'
    dataroot = Path(root)
    data_paths = list(glob.glob('D:/segment_res/*/*/whole.ply'))
    output_root_manifold = 'C:/Users/boyua/PycharmProjects/MeshMAE-mesh/dataset/mesh_manifold'
    output_root_simplify = 'C:/Users/boyua/PycharmProjects/MeshMAE-mesh/dataset/mesh_simplify'
    #for obj_path in dataroot.iterdir():
    
    for i,dp in enumerate(data_paths):
        dp=Path(dp)
        if dp.is_file() and str(dp)[-4:] == '.ply':
            idx = str(dp).split('\\')[-2]
            print('read', dp)
            mesh = trimesh.load_mesh(dp, process=False)
            output_path = str(output_root_simplify + '/' + idx + '.obj')
            directory = os.path.dirname(output_path)
            if not os.path.exists(directory):
                os.makedirs(directory)
            mesh = clean_mesh(str(dp), output_path)
