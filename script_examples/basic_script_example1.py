# basic example to create plot using python script
import bpy
import math
import bl_ext.user_default.blender_math_anim.variables as vb

# general render settings
scene = bpy.data.scenes['Scene']
scene.render.film_transparent = True
bpy.ops.math_anim.add_bloom()

func_type = ['EFUNCTION', 'IFUNCTION', 'ODEFUNCTION', 'POLARFUNCTION', 'PARAFUNCTION', 'FUNCDATA']
# for POLARFUNCTION and PARAFUNCTION
if True:
    # for POLARFUNCTION
    scene.math_anim_plotter_props.math_mode = 'POLARFUNCTION'
    scene.math_anim_plotter_props.polar_function = "a*cos(b*θ)"
    # set variable range of θ and parameters a, b
    var_ids = { "math_var_θ_min": -math.pi, "math_var_θ_max": math.pi, "math_var_θ_resolution": 100 }
    param_ids = { "math_param_a": 2, "math_param_b": 2 }
    for prop_id, value in var_ids.items():
        setattr(scene, prop_id, value)
    for prop_id, value in param_ids.items():
        setattr(scene, prop_id, value)
    # with "INVOKE_DEFAULT" for the first time call the operators
    bpy.ops.math_anim.add_gp_obj("INVOKE_DEFAULT",obj_name="Plotter")
    # set update_tag=False to create new plots, update_tag=True and update_current_layer=True to update existing plots
    # for each plotting, there are 2 layers created, one is the plot itself, another is the axis, the current select layer will be the plot layer after new plotting created
    bpy.ops.math_anim.create_plot('INVOKE_DEFAULT',update_tag=False)
    # for plotting preset animations or settings, add_anim can be one of ['transform', 'writing_anim', 'wave_anim', 'grow_anim', 'flow_anim', 'add_snapshot', 'curve_normal_tangent']; track_tag should be 'plotter_anim'
    # note: the current selected layer is the plot layer
    bpy.ops.math_anim.add_gp_anim('INVOKE_DEFAULT',add_anim='transform', track_tag='plotter_anim')
    bpy.ops.math_anim.add_gp_anim('INVOKE_DEFAULT',add_anim='writing_anim', track_tag='plotter_anim')
    gpobjects = scene.math_anim_gpobjects
    gplayers  = scene.math_anim_gplayers
    gp_obj = bpy.data.objects.get(gpobjects.gp_object)
    gp_layer = gp_obj.data.layers.get(gplayers.gp_layer)
    # the track holder for the animation settings (nodes or nodegroup)
    anim_node = vb.formula_anim_nodes['plotter_anim'][gp_obj['math_anim_obj']][gp_layer.name]['transform'][-1]
    translate_node = anim_node.node_tree.nodes['Translate Instances']
    translate_node.inputs['Local Space'].default_value = False
    translate_node.inputs['Translation'].default_value[0] = 10
    writing_node = vb.formula_anim_nodes['plotter_anim'][gp_obj['math_anim_obj']][gp_layer.name]['writing_anim'][0]
    writing_node.inputs['Range Start'].default_value = 24
    writing_node.inputs['Start Frame'].default_value = 24
    writing_node.inputs['Anim Length'].default_value = 120
    # now for the axis layer, move to the same place as the plot
    gplayers.gp_layer = f"{gp_layer.name}.axis"
    gp_layer = gp_obj.data.layers.get(gplayers.gp_layer)
    if gp_obj.data.layers.get(gp_layer.name):
        bpy.ops.math_anim.add_gp_anim("INVOKE_DEFAULT",add_anim='transform', track_tag='plotter_anim')
        anim_node = vb.formula_anim_nodes['plotter_anim'][gp_obj['math_anim_obj']][gp_layer.name]['transform'][-1]
        translate_node = anim_node.node_tree.nodes['Translate Instances']
        translate_node.inputs['Local Space'].default_value = False
        translate_node.inputs['Translation'].default_value[0] = 10

    # for PARAFUNCTION
    scene.math_anim_plotter_props.math_mode = 'PARAFUNCTION'
    scene.math_anim_plotter_props.function_x = 'a*cos(a0*t)'
    scene.math_anim_plotter_props.function_y = 'c*sin(t+b0)'
    scene.math_anim_plotter_props.function_z = '0'
    # since a, b are already defined, change their values will update the polar plot too
    # only set lower range of variable t and parameter a0
    prop_ids = { "math_var_t_min": -math.pi/2 , "math_param_a0": 2 }
    for prop_id, value in prop_ids.items():
        setattr(scene, prop_id, value)
    bpy.ops.math_anim.create_plot('INVOKE_DEFAULT',update_tag=False)
