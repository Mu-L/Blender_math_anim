import bpy
import math
import bl_ext.user_default.blender_math_anim.variables as vb
param_set1 = [ f'a{i}' for i in range(5)]
param_set2 = [ f'b{i}' for i in range(5)]
param_set3 = [ f'phi{i}' for i in range(5)]
vars = [f't{i}' for i in range(5)]
scene = bpy.data.scenes['Scene']
scene.render.film_transparent = True
bpy.ops.math_anim.add_bloom()
a_vals = [1.0,1.0,1.0,2.0,3.0,3.0,4.0,5.0,6.0]
b_vals = [1.0,2.0,3.0,3.0,4.0,5.0,5.0,6.0,7.0]
for i in range(5):
    scene.math_anim_plotter_props.math_mode = 'PARAFUNCTION'
    scene.math_anim_plotter_props.function_x = f"cos({param_set1[i]}*{vars[i]}+{param_set3[i]})"
    scene.math_anim_plotter_props.function_y = f"cos({param_set2[i]}*{vars[i]})"
    setattr(scene, f"math_param_{param_set3[i]}", i*math.pi/4)
    if i==0:
        bpy.ops.math_anim.add_gp_obj("INVOKE_DEFAULT",obj_name="Plotter")
        bpy.ops.math_anim.create_plot('INVOKE_DEFAULT',update_tag=False)
    else:
        bpy.ops.math_anim.add_gp_obj(obj_name="Plotter")
        bpy.ops.math_anim.create_plot(update_tag=False)
    if i==0 or i==4:
        setattr(scene, f"math_var_{vars[i]}_min", 0.0)
        setattr(scene, f"math_var_{vars[i]}_max", math.pi)
    bpy.ops.math_anim.add_gp_anim('INVOKE_DEFAULT',add_anim='transform', track_tag='plotter_anim')
    bpy.ops.math_anim.add_gp_anim('INVOKE_DEFAULT',add_anim='add_snapshot', track_tag='plotter_anim')
    gpobjects = scene.math_anim_gpobjects
    gplayers  = scene.math_anim_gplayers
    gp_obj = bpy.data.objects.get(gpobjects.gp_object)
    gp_layer = gp_obj.data.layers.get(gplayers.gp_layer)
    anim_node = vb.formula_anim_nodes['plotter_anim'][gp_obj['math_anim_obj']][gp_layer.name]['transform'][0]
    translate_node = anim_node.node_tree.nodes['Translate Instances']
    translate_node.inputs['Local Space'].default_value = False
    translate_node.inputs['Translation'].default_value[0] = i * 2.5
    snapshot_node = vb.formula_anim_nodes['plotter_anim'][gp_obj['math_anim_obj']][gp_layer.name]['add_snapshot'][0]
    snapshot_node.inputs['Snapshot Rate (frames)'].default_value = 24
    snapshot_node.inputs['Total Snapshots'].default_value = 9
    for j in range(9):
        frame = j * 24 + 5
        translate_node.inputs['Translation'].default_value[1] = -j * 2.5
        translate_node.inputs['Translation'].keyframe_insert(data_path="default_value", frame=frame, index=1)
        setattr(scene, f"math_param_{param_set1[i]}", a_vals[j])
        setattr(scene, f"math_param_{param_set2[i]}", b_vals[j])
        if b_vals[j] != getattr(scene, f"math_param_{param_set2[i]}"):
            setattr(scene, f"math_param_{param_set2[i]}", b_vals[j])
        scene.keyframe_insert(data_path=f"math_param_{param_set1[i]}", frame=frame)
        scene.keyframe_insert(data_path=f"math_param_{param_set2[i]}", frame=frame)

