# for the butterfly effect in Blender, tiny changes in initial conditions can lead to vastly different outcomes.
import bpy
import math
import bl_ext.user_default.blender_math_anim.variables as vb

# general render settings
scene = bpy.data.scenes['Scene']
scene.render.film_transparent = True
bpy.ops.math_anim.add_bloom()
# two sets of variables for two different initial conditions
var_set1 = { "x": 1.000, "y": 0.0, "z": 0.0 } # var_name: initial_value
var_set2 = { "x0": 1.001, "y0": 0.0, "z0": 0.0 }  # tiny change in x
for i, var_set in enumerate([var_set1, var_set2]):
    x, y, z = var_set.keys()
    x0, y0, z0 = var_set.values()
    scene.math_anim_plotter_props.math_mode = 'ODEFUNCTION'
    scene.math_anim_plotter_props.ode_function_x = f"a*({y}-{x})"
    scene.math_anim_plotter_props.ode_function_y = f"{x}*(b-{z})-{y}"
    scene.math_anim_plotter_props.ode_function_z = f"{x}*{y}-c*{z}"
    scene.math_anim_plotter_props.ode_solver = "RK4"
    # set initial values of x0, y0, z0 and parameters a, b, c, along with t0, t1, dt
    params = { f"{x}0": x0, f"{y}0": y0, f"{z}0": z0, "a": 10, "b": 28, "c": 8/3, "t0": 0.0, "t1": 50.0, "dt": 0.01 }
    for param, value in params.items():
        setattr(scene, f"math_param_{param}", params[param])
    if i == 0:
        bpy.ops.math_anim.add_gp_obj("INVOKE_DEFAULT",obj_name="Plotter", geomd_category="plotter")
    bpy.ops.math_anim.create_plot('INVOKE_DEFAULT',update_tag=False)
    plotter_props = scene.math_anim_plotter_props
    plotter_props.plot_scale = (0.1, 0.1, 0.1)
    plotter_props.plot_translation = (0.0, i*10.0, 0.0)  # offset the two plots
    anim_type = 'writing_anim'
    bpy.ops.math_anim.add_gp_anim('INVOKE_DEFAULT',add_anim=anim_type, track_tag='plotter_anim')
    gpobjects = scene.math_anim_gpobjects
    gplayers  = scene.math_anim_gplayers
    gp_obj = bpy.data.objects.get(gpobjects.gp_object)
    gp_layer = gp_obj.data.layers.get(gplayers.gp_layer)
    anim_node = vb.formula_anim_nodes['plotter_anim'][gp_obj['math_anim_obj']][gp_layer.name][anim_type][0]
    anim_node.inputs['Anim Length'].default_value = 250
    anim_node.inputs['Local'].default_value = True
    anim_node.inputs['Local Writing Symbol Radius'].default_value = 0.05

# formula info
formula = ["Butterfly Effect", "\eqalign{dx/dt &= a(y-x) \cr dy/dt &= x(b-z)-y \cr dz/dt &= xy-cz}"]
param_values = ["\eqalign{a &= 10 & {\Red x_0 = 1.000} \cr b &= 28 & y_0 = 0.0 \cr c &= 8/3 & z_0 = 0.0}", "\eqalign{a &= 10 & {\Red x_0 = 1.001} \cr b &= 28 & y_0 = 0.0 \cr c &= 8/3 & z_0 = 0.0}"]
scene.math_anim_formula_props.formula_source = 'Optex_Code'
# display the formula
for i in range(len(formula)):
    if len(scene.math_anim_optexcode.paths) == 0:
        bpy.ops.math_anim.formula_addpath()
        scene.math_anim_optexcode.paths[0].path = f"{{\Yellow {formula[i]}}}"
    else:
        scene.math_anim_optexcode.paths[0].path = f"{{\Yellow {formula[i]}}}"
        scene.math_anim_optexcode.paths[0].selected = True
        for j in range(1, len(scene.math_anim_optexcode.paths)):
            scene.math_anim_optexcode.paths[j].selected = False
    if i == 0:
        scene.math_anim_optexcode.paths[0].math = False
    else:
        scene.math_anim_optexcode.paths[0].math = True
    bpy.ops.math_anim.create_formula("INVOKE_DEFAULT", color_strength=20, curve_radius=0.006)

    scene.math_anim_formula_props.anim_style = 'TRANSFORM'
    bpy.ops.math_anim.add_formula_anim("INVOKE_DEFAULT")
    obj = bpy.context.object
    translate_node = vb.formula_anim_nodes[obj["math_anim_obj"]]['text_anim']['transform'][1]
    translate_node.inputs["Local Space"].default_value = False
    translate_node.inputs["Translation"].default_value = (0, 4.0, 3.5 - i*0.5)
    rotate_node = vb.formula_anim_nodes[obj["math_anim_obj"]]['text_anim']['transform'][0]
    rotate_node.inputs["Local Space"].default_value = False
    rotate_node.inputs["Rotation"].default_value = (math.pi/2, 0, math.pi/2)
# for the initial condition display
for i in range(len(param_values)):
    scene.math_anim_optexcode.paths[0].path = f"{{\Green {param_values[i]}}}"
    bpy.ops.math_anim.create_formula("INVOKE_DEFAULT", color_strength=20, curve_radius=0.006)

    scene.math_anim_formula_props.anim_style = 'TRANSFORM'
    bpy.ops.math_anim.add_formula_anim("INVOKE_DEFAULT")
    obj = bpy.context.object
    translate_node = vb.formula_anim_nodes[obj["math_anim_obj"]]['text_anim']['transform'][1]
    translate_node.inputs["Local Space"].default_value = False
    translate_node.inputs["Translation"].default_value = (1, i*10+1.0, 0.0)
    rotate_node = vb.formula_anim_nodes[obj["math_anim_obj"]]['text_anim']['transform'][0]
    rotate_node.inputs["Local Space"].default_value = False
    rotate_node.inputs["Rotation"].default_value = (math.pi/6, 0, math.pi/2)
