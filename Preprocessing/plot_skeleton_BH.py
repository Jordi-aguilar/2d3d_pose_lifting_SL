import skeletalModel_new
import numpy as np
from mpl_toolkits import mplot3d
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d
import matplotlib.animation as animation
from IPython.display import HTML

# Function plot_3D_skeletons takes as inputs a np.array xyz_vec of shape [NUM_JOINTS, 3] (equivalent to one video frame)
# and returns an animated 3D plot of the skeleton in that frame

def plot_3D_skeleton(xyz_vec, show_animation = True, labels = True, hands = False):
    # Obtain the x_vec, y_vec and z_vec
    x_vec = xyz_vec[0::4]
    y_vec = xyz_vec[1::4]
    z_vec = xyz_vec[2::4]

    # Plot the Skeleton
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    
    
    def init():
        skeleton_parts = skeletalModel_new.getSkeletalModelStructure()
        for init, end, _ in skeleton_parts:
            hands_constraint = not hands or (hands and (init >= 25 or init in [5, 11]))
            if x_vec[init] != 999 and x_vec[end] != 999 and y_vec[init] != 999 and y_vec[end] != 999 and z_vec[init] != 999 and z_vec[end] != 999 and hands_constraint:
                ax.plot([x_vec[init], x_vec[end]], [y_vec[init], y_vec[end]], [z_vec[init], z_vec[end]])
        #for part in skeleton_parts:
        #    ax.plot([x_vec[i] for i in part], [y_vec[i] for i in part], [z_vec[i] for i in part])
        if labels:
            ax.set_xlabel('X axis')
            ax.set_ylabel('Y axis')
            ax.set_zlabel('Z axis')
        # ax.axis('equal')
        else:
            ax.set_yticklabels([])
            ax.set_xticklabels([])
            ax.set_zticklabels([])
        return fig,

    def animate(i):
        ax.view_init(elev=0, azim=3.6*i)
        return fig,
    
    # Animate
    if show_animation:
        ani = animation.FuncAnimation(fig, animate, init_func=init,
                                frames=100, interval=100, blit=True)
  
        return HTML(ani.to_html5_video())
    # Display the final result
    else:
        fig = init()
        return fig