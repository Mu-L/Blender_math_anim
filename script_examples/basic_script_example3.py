# basic example to create plot using python script
import bpy
import math
import numpy as np
import bl_ext.user_default.blender_math_anim.variables as vb

# general render settings
scene = bpy.data.scenes['Scene']
scene.render.film_transparent = True
bpy.ops.math_anim.add_bloom()

func_type = ['EFUNCTION', 'IFUNCTION', 'ODEFUNCTION', 'POLARFUNCTION', 'PARAFUNCTION', 'FUNCDATA']
# for FUNCDATA
if True:
    scene.math_anim_plotter_props.math_mode = 'FUNCDATA'
    # for the function data plot, can pass the data directly to vb._x_vals, vb._y_vals, vb._z_vals; or load data files which will automatically fill these variables
    bpy.ops.math_anim.add_gp_obj("INVOKE_DEFAULT",obj_name="Plotter")
    x = np.arange(0, 2 * np.pi + 0.1, 0.1)  # include 2*pi
    y = np.cos(x)
    z = np.zeros_like(x)  # z = 0
    data = np.column_stack((x, y, z))
    vb._x_vals.append(data[:, 0].tolist())
    vb._y_vals.append(data[:, 1].tolist())
    vb._z_vals.append(data[:, 2].tolist())
    # can add multiple data sets
    y = np.sin(x)
    data = np.column_stack((x, y, z))
    vb._x_vals.append(data[:, 0].tolist())
    vb._y_vals.append(data[:, 1].tolist())
    vb._z_vals.append(data[:, 2].tolist())
    bpy.ops.math_anim.create_plot('INVOKE_DEFAULT',update_tag=False, use_data=True)

    # can also load data from files
    """
    funcdata_paths = scene.math_anim_func_datafile
    datafiles = [ "/path/to/your/datafile1.csv", "/path/to/your/datafile2.csv" ]
    for filepath in datafiles:
        new_item = funcdata_paths.paths.add()
        new_item.path = filepath
        new_item.delim = " "
    bpy.ops.math_anim.create_plot('INVOKE_DEFAULT',update_tag=False, use_data_file=True)
    """
