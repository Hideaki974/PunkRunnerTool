import bpy

class Vw_PT_Panel(bpy.types.Panel):
	bl_idname = "Vw_PT_Panel"
	bl_label = "Vw Panel"
	bl_category = "PUNK RUNNER"
	bl_space_type = "VIEW_3D"
	bl_region_type = "UI"

	def draw(self, context):
		layout = self.layout

		row = layout.row()
		row.label(text="Geometry Tools", icon='SNAP_VOLUME')
		row = layout.row()
		row.operator('view3d.voxretopo_optimal', text="Optimize LOD",)