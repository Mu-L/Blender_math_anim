import bpy
import math
import bl_ext.user_default.blender_math_anim.variables as vb

scene = bpy.data.scenes["Scene"]
scene.math_anim_formula_props.formula_source = 'Optex_Code'
formula = ["x(t) = \cos(a*t + \phi)", "y(t) = \cos(b*t)"]
for i in range(len(formula)):
    if len(scene.math_anim_optexcode.paths) == 0:
        bpy.ops.math_anim.formula_addpath()
        scene.math_anim_optexcode.paths[0].path = f"{{\Yellow {formula[i]}}}"
    else:
        scene.math_anim_optexcode.paths[0].path = f"{{\Yellow {formula[i]}}}"

    bpy.ops.math_anim.create_formula("INVOKE_DEFAULT")
    obj = bpy.context.object
    suffix = obj["math_anim_obj"][obj["math_anim_obj"].find('Global'):]
    char_settings = bpy.data.node_groups.get(f"char_settings.{suffix}")
    radius_node = char_settings.nodes['Curve Radius']
    radius_node.inputs["Value"].default_value = 0.01

    scene.math_anim_formula_props.anim_style = 'TRANSFORM'
    bpy.ops.math_anim.add_formula_anim("INVOKE_DEFAULT")
    translate_node = vb.formula_anim_nodes[obj["math_anim_obj"]]['text_anim']['transform'][1]
    translate_node.inputs["Local Space"].default_value = False
    translate_node.inputs["Translation"].default_value[0] = 11.5
    translate_node.inputs["Translation"].default_value[1] = -i*7.0 - 2.0
    scale_node = vb.formula_anim_nodes[obj["math_anim_obj"]]['text_anim']['transform'][2]
    scale_node.inputs["Local Space"].default_value = False
    scale_node.inputs["Scale"].default_value = (2.0, 2.0, 2.0)
    scale_node.inputs["Center"].default_value = (11.5, -i*7.0-2.0, 0)
    rotate_node = vb.formula_anim_nodes[obj["math_anim_obj"]]['text_anim']['transform'][0]
    rotate_node.inputs["Local Space"].default_value = False
    rotate_node.inputs["Rotation"].default_value = (0, 0, -math.pi/2)

n_rows, n_cols = 8, 5 # different col for different phase, different row for different a,b
phi_values = ["0", "\pi/4", "\pi/2", "3\pi/4", "\pi"]
for j in range(n_cols):
    if len(scene.math_anim_optexcode.paths) == 0:
        bpy.ops.math_anim.formula_addpath()
        scene.math_anim_optexcode.paths[0].path = f"{{\White \phi = {phi_values[j]}}}"
    else:
        scene.math_anim_optexcode.paths[0].path = f"{{\White \phi = {phi_values[j]}}}"

    bpy.ops.math_anim.create_formula("INVOKE_DEFAULT")
    obj = bpy.context.object
    suffix = obj["math_anim_obj"][obj["math_anim_obj"].find('Global'):]
    char_settings = bpy.data.node_groups.get(f"char_settings.{suffix}")
    radius_node = char_settings.nodes['Curve Radius']
    radius_node.inputs["Value"].default_value = 0.01

    scene.math_anim_formula_props.anim_style = 'TRANSFORM'
    bpy.ops.math_anim.add_formula_anim("INVOKE_DEFAULT")
    translate_node = vb.formula_anim_nodes[obj["math_anim_obj"]]['text_anim']['transform'][1]
    translate_node.inputs["Local Space"].default_value = False
    translate_node.inputs["Translation"].default_value[0] = j*2.5 - 1.0
    translate_node.inputs["Translation"].default_value[1] = 1.0
    scale_node = vb.formula_anim_nodes[obj["math_anim_obj"]]['text_anim']['transform'][2]
    scale_node.inputs["Local Space"].default_value = False
    scale_node.inputs["Scale"].default_value = (1.5, 1.5, 1.5)
    scale_node.inputs["Center"].default_value = (j*2.5 - 1.0, 0, 0)
    rotate_node = vb.formula_anim_nodes[obj["math_anim_obj"]]['text_anim']['transform'][0]
    rotate_node.inputs["Local Space"].default_value = False
    rotate_node.inputs["Rotation"].default_value = (0, 0, 0)

a_vals = [1.0,1.0,1.0,2.0,3.0,3.0,4.0,5.0]
b_vals = [1.0,2.0,3.0,3.0,4.0,5.0,5.0,6.0]
for i in range(n_rows):
    if len(scene.math_anim_optexcode.paths) == 0:
        bpy.ops.math_anim.formula_addpath()
        scene.math_anim_optexcode.paths[0].path = f"{{\Green a = {a_vals[i]}}}"
    else:
        scene.math_anim_optexcode.paths[0].path = f"{{\Green a = {a_vals[i]}}}"

    bpy.ops.math_anim.create_formula("INVOKE_DEFAULT")
    obj = bpy.context.object
    suffix = obj["math_anim_obj"][obj["math_anim_obj"].find('Global'):]
    char_settings = bpy.data.node_groups.get(f"char_settings.{suffix}")
    radius_node = char_settings.nodes['Curve Radius']
    radius_node.inputs["Value"].default_value = 0.01

    scene.math_anim_formula_props.anim_style = 'TRANSFORM'
    bpy.ops.math_anim.add_formula_anim("INVOKE_DEFAULT")
    translate_node = vb.formula_anim_nodes[obj["math_anim_obj"]]['text_anim']['transform'][1]
    translate_node.inputs["Local Space"].default_value = False
    translate_node.inputs["Translation"].default_value[0] = -1.5
    translate_node.inputs["Translation"].default_value[1] = -i*2.5 + 1.0
    scale_node = vb.formula_anim_nodes[obj["math_anim_obj"]]['text_anim']['transform'][2]
    scale_node.inputs["Local Space"].default_value = False
    scale_node.inputs["Scale"].default_value = (1.5, 1.5, 1.5)
    scale_node.inputs["Center"].default_value = (-1.5, -i*2.5+1.0, 0)
    rotate_node = vb.formula_anim_nodes[obj["math_anim_obj"]]['text_anim']['transform'][0]
    rotate_node.inputs["Local Space"].default_value = False
    rotate_node.inputs["Rotation"].default_value = (0, 0, -math.pi/2)
for i in range(n_rows):
    if len(scene.math_anim_optexcode.paths) == 0:
        bpy.ops.math_anim.formula_addpath()
        scene.math_anim_optexcode.paths[0].path = f"{{\Blue b = {b_vals[i]}}}"
    else:
        scene.math_anim_optexcode.paths[0].path = f"{{\Blue b = {b_vals[i]}}}"

    bpy.ops.math_anim.create_formula("INVOKE_DEFAULT")
    obj = bpy.context.object
    suffix = obj["math_anim_obj"][obj["math_anim_obj"].find('Global'):]
    char_settings = bpy.data.node_groups.get(f"char_settings.{suffix}")
    radius_node = char_settings.nodes['Curve Radius']
    radius_node.inputs["Value"].default_value = 0.01

    scene.math_anim_formula_props.anim_style = 'TRANSFORM'
    bpy.ops.math_anim.add_formula_anim("INVOKE_DEFAULT")
    translate_node = vb.formula_anim_nodes[obj["math_anim_obj"]]['text_anim']['transform'][1]
    translate_node.inputs["Local Space"].default_value = False
    translate_node.inputs["Translation"].default_value[0] = -2.0
    translate_node.inputs["Translation"].default_value[1] = -i*2.5 + 1.0
    scale_node = vb.formula_anim_nodes[obj["math_anim_obj"]]['text_anim']['transform'][2]
    scale_node.inputs["Local Space"].default_value = False
    scale_node.inputs["Scale"].default_value = (1.5, 1.5, 1.5)
    scale_node.inputs["Center"].default_value = (-2.0, -i*2.5+1.0, 0)
    rotate_node = vb.formula_anim_nodes[obj["math_anim_obj"]]['text_anim']['transform'][0]
    rotate_node.inputs["Local Space"].default_value = False
    rotate_node.inputs["Rotation"].default_value = (0, 0, -math.pi/2)
