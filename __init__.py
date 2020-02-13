# ##### BEGIN GPL LICENSE BLOCK #####
#
#  This program is free software; you can redistribute it and/or
#  modify it under the terms of the GNU General Public License
#  as published by the Free Software Foundation; either version 2
#  of the License, or (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software Foundation,
#  Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
#
# ##### END GPL LICENSE BLOCK #####

# ######### TOOL MADE FOR ###########
#    ___  __  ___  ____ __  ___  __  ___  ___  _________ 
#   / _ \/ / / / |/ / //_/ / _ \/ / / / |/ / |/ / __/ _ \
#  / ___/ /_/ /    / ,<   / , _/ /_/ /    /    / _// , _/
# /_/   \____/_/|_/_/|_| /_/|_|\____/_/|_/_/|_/___/_/|_|                                                      
#
# <pep8 compliant>


bl_info = {
    "name": "VoxelWorkflow",
    "author": "Pierre Fontaine",
    "version": (0, 0, 1),
    "blender": (2, 81, 0),
    "location": "View3D",
    "description": "various tools for voxel setup workflow",
    "warning": "in Dev",
    "wiki_url": "",
    "tracker_url": "",
    "category": "Mesh"}

import bpy

from . VW_op    import Vw_OT_Operator
from . VW_panel import Vw_PT_Panel 


classes = (Vw_OT_Operator, Vw_PT_Panel)

register, unregister = bpy.utils.register_classes_factory(classes)