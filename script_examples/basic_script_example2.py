# basic example to create plot using python script
import bpy
import math
import bl_ext.user_default.blender_math_anim.variables as vb

# general render settings
scene = bpy.data.scenes['Scene']
scene.render.film_transparent = True
bpy.ops.math_anim.add_bloom()

func_type = ['EFUNCTION', 'IFUNCTION', 'ODEFUNCTION', 'POLARFUNCTION', 'PARAFUNCTION', 'FUNCDATA']
# for ODEFUNCTION
if True:
    scene.math_anim_plotter_props.math_mode = 'ODEFUNCTION'
    scene.math_anim_plotter_props.ode_function_x = "a*(y-x)"
    scene.math_anim_plotter_props.ode_function_y = "x*(b-z)-y"
    scene.math_anim_plotter_props.ode_function_z = "x*y-c*z"
    scene.math_anim_plotter_props.ode_solver = "RK45"
    # set initial values of x0, y0, z0 and parameters a, b, c, along with t0, t1, dt
    params = { "x0": 0.1, "y0": 0.0, "z0": 0.0, "a": 10, "b": 28, "c": 8/3, "t0": 0.0, "t1": 50.0, "dt": 0.02 }
    for param, value in params.items():
        setattr(scene, f"math_param_{param}", params[param])
    bpy.ops.math_anim.add_gp_obj("INVOKE_DEFAULT",obj_name="Plotter")
    bpy.ops.math_anim.create_plot('INVOKE_DEFAULT',update_tag=False)
