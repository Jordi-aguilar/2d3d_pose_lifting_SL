from scipy.spatial.transform import Rotation as R
import numpy as np

# Function rotate_axes takes as inputs a np.array xyz_vec of shape [NUM_JOINTS, 3] (equivalent to one frame)
# and returns the rotated coordinates in a np.array of the same shape

def rotate_skeleton(vec_xyz):
    
    mid_hip_idx = 2
    neck_idx = 0
    nose_idx = 1
    
    # Translation so mid-hip is the origin of coordinates
    vec_MidHip = np.asanyarray([vec_xyz[mid_hip_idx] for i in range(0, 67)])
    vec_xyz_translated = vec_xyz - vec_MidHip

    # Rotation so the column is the y-axis
    column_vec = vec_xyz[neck_idx] - vec_xyz[mid_hip_idx]
    column_vec = column_vec / np.linalg.norm(column_vec)
    y_vec = np.asanyarray([0, 1, 0])
    y_angle = np.arccos(np.dot(column_vec, y_vec))
    normal_vec = np.cross(column_vec, y_vec)
    normal_vec = normal_vec / np.linalg.norm(normal_vec)

    rotation_vector = y_angle * normal_vec
    rotation = R.from_rotvec(rotation_vector)
    vec_xyz_rotated = rotation.apply(vec_xyz_translated)

    # Rotation so that the skeleton is facing forwards (YZ plane!!!!!!!!)
    face_vec = vec_xyz_rotated[nose_idx] - vec_xyz_rotated[neck_idx]
    face_vec = face_vec / np.linalg.norm(face_vec)
    face_vec_proj = np.asanyarray([face_vec[0], 0, face_vec[2]])
    face_vec_proj = face_vec_proj / np.linalg.norm(face_vec_proj)
    z_vec = np.asanyarray([0, 0, 1])
    z_angle = np.arccos(np.dot(face_vec_proj, z_vec))
    normal_vec = np.cross(face_vec_proj, z_vec)
    normal_vec = normal_vec / np.linalg.norm(normal_vec)

    rotation_vector = z_angle * normal_vec
    rotation = R.from_rotvec(rotation_vector)
    vec_xyz_rotated2 = rotation.apply(vec_xyz_rotated)

    return vec_xyz_rotated2
