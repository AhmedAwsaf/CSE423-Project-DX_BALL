'''OpenGL extension OES.texture_cube_map

This module customises the behaviour of the 
OpenGL.raw.GLES1.OES.texture_cube_map to provide a more 
Python-friendly API

Overview (from the spec)
	
	This extension provides a new texture generation scheme for cube
	map textures.  Instead of the current texture providing a 1D, 2D,
	or 3D lookup into a 1D, 2D, or 3D texture image, the texture is a
	set of six 2D images representing the faces of a cube.  The (s,t,r)
	texture coordinates are treated as a direction vector emanating from
	the center of a cube.  At texture generation time, the interpolated
	per-fragment (s,t,r) selects one cube face 2D image based on the
	largest magnitude coordinate (the major axis).  A new 2D (s,t) is
	calculated by dividing the two other coordinates (the minor axes
	values) by the major axis value.  Then the new (s,t) is used to
	lookup into the selected 2D texture image face of the cube map.
	
	Unlike a standard 1D, 2D, or 3D texture that have just one target,
	a cube map texture has six targets, one for each of its six 2D texture
	image cube faces.  All these targets must be consistent, complete,
	and have equal width and height (ie, square dimensions).
	
	This extension also provides two new texture coordinate generation modes
	for use in conjunction with cube map texturing.  The reflection map
	mode generates texture coordinates (s,t,r) matching the vertex's
	eye-space reflection vector.  The reflection map mode
	is useful for environment mapping without the singularity inherent
	in sphere mapping.  The normal map mode generates texture coordinates
	(s,t,r) matching the vertex's transformed eye-space
	normal.  The normal map mode is useful for sophisticated cube
	map texturing-based diffuse lighting models.
	
	The intent of the new texgen functionality is that an application using
	cube map texturing can use the new texgen modes to automatically
	generate the reflection or normal vectors used to look up into the
	cube map texture.
	
	An application note:  When using cube mapping with dynamic cube
	maps (meaning the cube map texture is re-rendered every frame),
	by keeping the cube map's orientation pointing at the eye position,
	the texgen-computed reflection or normal vector texture coordinates
	can be always properly oriented for the cube map.  However if the
	cube map is static (meaning that when view changes, the cube map
	texture is not updated), the texture matrix must be used to rotate
	the texgen-computed reflection or normal vector texture coordinates
	to match the orientation of the cube map.  The rotation can be
	computed based on two vectors: 1) the direction vector from the cube
	map center to the eye position (both in world coordinates), and 2)
	the cube map orientation in world coordinates.  The axis of rotation
	is the cross product of these two vectors; the angle of rotation is
	the arcsin of the dot product of these two vectors.

The official definition of this extension is available here:
http://www.opengl.org/registry/specs/OES/texture_cube_map.txt
'''
from OpenGL import platform, constant, arrays
from OpenGL import extensions, wrapper
import ctypes
from OpenGL.raw.GLES1 import _types, _glgets
from OpenGL.raw.GLES1.OES.texture_cube_map import *
from OpenGL.raw.GLES1.OES.texture_cube_map import _EXTENSION_NAME

def glInitTextureCubeMapOES():
    '''Return boolean indicating whether this extension is available'''
    from OpenGL import extensions
    return extensions.hasGLExtension( _EXTENSION_NAME )

# INPUT glTexGenfvOES.params size not checked against 'pname'
glTexGenfvOES=wrapper.wrapper(glTexGenfvOES).setInputArraySize(
    'params', None
)
# INPUT glTexGenivOES.params size not checked against 'pname'
glTexGenivOES=wrapper.wrapper(glTexGenivOES).setInputArraySize(
    'params', None
)
# INPUT glTexGenxvOES.params size not checked against 'pname'
glTexGenxvOES=wrapper.wrapper(glTexGenxvOES).setInputArraySize(
    'params', None
)
# INPUT glGetTexGenfvOES.params size not checked against 'pname'
glGetTexGenfvOES=wrapper.wrapper(glGetTexGenfvOES).setInputArraySize(
    'params', None
)
# INPUT glGetTexGenivOES.params size not checked against 'pname'
glGetTexGenivOES=wrapper.wrapper(glGetTexGenivOES).setInputArraySize(
    'params', None
)
glGetTexGenxvOES=wrapper.wrapper(glGetTexGenxvOES).setOutput(
    'params',size=_glgets._glget_size_mapping,pnameArg='pname',orPassIn=True
)
### END AUTOGENERATED SECTION