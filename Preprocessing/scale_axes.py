import numpy as np

# Function scale_axes takes as inputs a np.array xyz_vec of shape [NUM_FRAMES,NUM_JOINTS, 3] (equivalent to one whole video)
# and returns the normalized coordinates in a np.array of the same shape

def scale_axes(xyz_vec):
    
    #print(xyz_vec.shape)
    
    nekc_idx = 0
    mid_hip_idx = 2
    
    # Translation so mid-hip is the origin of coordinates
    vec_MidHip = np.asanyarray([xyz_vec[mid_hip_idx] for i in range(0, 67)])
    xyz_vec_translated = xyz_vec - vec_MidHip
    
    torso = xyz_vec[nekc_idx] - xyz_vec_translated[mid_hip_idx]
    # print(torso, xyz_vec[nekc_idx], xyz_vec[mid_hip_idx])
    torso_len = np.linalg.norm(torso)
    # norm_xy_vec = np.empty(xy_vec.shape)
    # norm_z_vec = np.empty(z_vec.shape)
    
    norm_xyz_vec = xyz_vec_translated / torso_len

    # for i in range(0,67):
    #     x_vec = np.divide(xy_vec[i,:,0], torso_len)
    #     y_vec = np.divide(xy_vec[i,:,1], torso_len)
    #     norm_z_vec[i,:] = np.divide(z_vec[i,:], torso_len)
    #     norm_xy_vec[i,:,0] = x_vec
    #     norm_xy_vec[i,:,1] = y_vec

    # norm_z_vec = np.expand_dims(norm_z_vec, axis=2)

    # norm_xyz_vec = np.concatenate((norm_xy_vec, norm_z_vec), axis = 2)
    return norm_xyz_vec