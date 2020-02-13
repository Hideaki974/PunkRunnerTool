import bpy

class Vw_OT_Operator(bpy.types.Operator):
	bl_idname = "view3d.voxretopo_optimal"
	bl_label = "Vw optimal"
	bl_description = "optimise the LOD mesh for game"

	def execute(self,context):		
		#bpy.ops.object.modifier_add(type='REMESH')
		#bpy.context.object.modifiers["Remesh"].use_remove_disconnected = False
		bpy.ops.object.modifier_add(type='DECIMATE')
		bpy.context.object.modifiers["Decimate"].decimate_type = 'DISSOLVE'
		bpy.ops.object.modifier_add(type='TRIANGULATE')
		bpy.ops.object.convert(target='MESH')
		return{'FINISHED'}