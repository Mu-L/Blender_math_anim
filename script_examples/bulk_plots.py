import bpy
import math
import bl_ext.user_default.blender_math_anim.variables as vb
n_rows, n_cols = 8, 5 # different col for different phase, different row for different a,b
param_a = [ f'a{i}' for i in range(n_rows * n_cols)]
param_b = [ f'b{i}' for i in range(n_rows * n_cols)]
param_phi = [ f'phi{i}' for i in range(n_cols)]
vars = {i:{j: {'var': 't', 'min': -math.pi, 'max': math.pi} for j in range(n_cols)} for i in range(n_rows)}
# adjust variables due to different ranges needed
for j in [0,4]:
    for i in range(n_rows):
        vars[i][j]['var'] = 't0'
        vars[i][j]['min'] = 0.0
        vars[i][j]['max'] = math.pi
for i in [4]:
    for j in [1]:
        vars[i][j]['var'] = 't1'
        vars[i][j]['min'] = -3*math.pi/4
        vars[i][j]['max'] = math.pi/4
for i in [1,4,7]:
    for j in [2]:
        vars[i][j]['var'] = 't2'
        vars[i][j]['min'] = -math.pi/2
        vars[i][j]['max'] = math.pi/2
for i in [4]:
    for j in [3]:
        vars[i][j]['var'] = 't3'
        vars[i][j]['min'] = -math.pi/4
        vars[i][j]['max'] = 3*math.pi/4
scene = bpy.data.scenes['Scene']
scene.render.film_transparent = True
bpy.ops.math_anim.add_bloom()
a_vals = [1.0,1.0,1.0,2.0,3.0,3.0,4.0,5.0]
b_vals = [1.0,2.0,3.0,3.0,4.0,5.0,5.0,6.0]
for j in range(n_cols):
    for i in range(n_rows):
        idx = j*8 + i
        scene.math_anim_plotter_props.math_mode = 'PARAFUNCTION'
        scene.math_anim_plotter_props.function_x = f"cos({param_a[idx]}*{vars[i][j]['var']}+{param_phi[j]})"
        scene.math_anim_plotter_props.function_y = f"cos({param_b[idx]}*{vars[i][j]['var']})"
        setattr(scene, f"math_var_{vars[i][j]['var']}_min", vars[i][j]['min'])
        setattr(scene, f"math_var_{vars[i][j]['var']}_max", vars[i][j]['max'])
        setattr(scene, f"math_param_{param_a[idx]}", a_vals[i])
        setattr(scene, f"math_param_{param_b[idx]}", b_vals[i])
        setattr(scene, f"math_param_{param_phi[j]}", j*math.pi/4)
        if j==0 and i==0:
            bpy.ops.math_anim.add_gp_obj("INVOKE_DEFAULT",obj_name="Plotter")
            bpy.ops.math_anim.create_plot('INVOKE_DEFAULT',update_tag=False)
        else:
            bpy.ops.math_anim.add_gp_obj(obj_name="Plotter")
            bpy.ops.math_anim.create_plot(update_tag=False)
        bpy.ops.math_anim.add_gp_anim('INVOKE_DEFAULT',add_anim='transform', track_tag='plotter_anim')
        bpy.ops.math_anim.add_gp_anim('INVOKE_DEFAULT',add_anim='writing_anim', track_tag='plotter_anim')
        gpobjects = scene.math_anim_gpobjects
        gplayers  = scene.math_anim_gplayers
        gp_obj = bpy.data.objects.get(gpobjects.gp_object)
        gp_layer = gp_obj.data.layers.get(gplayers.gp_layer)
        anim_node = vb.formula_anim_nodes['plotter_anim'][gp_obj['math_anim_obj']][gp_layer.name]['transform'][0]
        translate_node = anim_node.node_tree.nodes['Translate Instances']
        translate_node.inputs['Local Space'].default_value = False
        translate_node.inputs['Translation'].default_value[0] = j * 2.5
        translate_node.inputs['Translation'].default_value[1] = -i * 2.5
        writing_node = vb.formula_anim_nodes['plotter_anim'][gp_obj['math_anim_obj']][gp_layer.name]['writing_anim'][0]
        writing_node.inputs['Range Start'].default_value = 24
        writing_node.inputs['Start Frame'].default_value = 24
        writing_node.inputs['Anim Length'].default_value = 120
        writing_node.inputs['Local'].default_value = True

