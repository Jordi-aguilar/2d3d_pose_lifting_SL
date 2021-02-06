# This function gives our structure of skeletal model


def getSkeletalModelStructure():
  # Definition of skeleton model structure:
  #   The structure is an n-tuple of:
  #
  #   (index of a start point, index of an end point, index of a bone) 
  #
  #   E.g., this simple skeletal model
  #
  #             (0)
  #              |
  #              |
  #              0
  #              |
  #              |
  #     (2)--1--(1)--1--(3)
  #      |               |
  #      |               |
  #      2               2
  #      |               |
  #      |               |
  #     (4)             (5)
  #
  #   has this structure:
  #
  #   (
  #     (0, 1, 0),
  #     (1, 2, 1),
  #     (1, 3, 1),
  #     (2, 4, 2),
  #     (3, 5, 2),
  #   )
  #
  #  Warning 1: The structure has to be a tree.  
  #
  #  Warning 2: The order isn't random. The order is from a root to lists.
  #

  pose = (
    # head
    (0, 1, 0),

    # left shoulder
    (0, 3, 1),

    # left arm
    (3, 4, 2),
    (4, 5, 3),

    # right shoulder
    (0, 9, 1), 

    # right arm
    (9, 10, 2),
    (10,11, 3),
    
    # spine
    (0, 2, 4),
    
    # left hip
    (2, 6, 5),
    
    # left leg
    (6, 7, 6),
    (7, 8, 7),
    
    # left foot
    (8, 21, 8),
    (8, 20, 9),
    (20, 19, 10),
    
    # right hip
    (2, 12, 5),
    
    # left leg
    (12, 13, 6),
    (13, 14, 7),
    
    # left foot
    (14, 24, 8),
    (14, 23, 9),
    (23, 22, 10),
    
    # left face,
    (1, 15, 11),
    (15, 16, 12),
    
    # right face,
    (1, 17, 11),
    (17, 18, 12)
)
    
  hands = (
    # right hand - wrist
    (11, 25, 13),
    
    # right hand - palm
    (25, 26, 14),
    (25, 30, 18),
    (25, 34, 22),
    (25, 38, 26),
    (25, 42, 30),
      
    # right hand - 1st finger
    (26, 27, 15),
    (27, 28, 16),
    (28, 29, 17),
      
    # right hand - 2nd finger
    (30, 31, 19),
    (31, 32, 20),
    (32, 33, 21),
      
    # right hand - 3rd finger
    (34, 35, 23),
    (35, 36, 24),
    (36, 37, 25),
      
    # right hand - 4th finger
    (38, 39, 27),
    (39, 40, 28),
    (40, 41, 29),
      
    # right hand - 5th finger
    (42, 43, 31),
    (43, 44, 32),
    (44, 45, 33),
      
    # left hand - wrist
    (5, 46, 13),
      
    # left hand - palm
    (46, 47, 14),
    (46, 51, 18),
    (46, 55, 22),
    (46, 59, 26),
    (46, 63, 30),
      
    # left hand - 1st finger
    (47, 48, 15),
    (48, 49, 16),
    (49, 50, 17),
      
    # left hand - 2nd finger
    (51, 52, 19),
    (52, 53, 20),
    (53, 54, 21),
      
    # left hand - 3rd finger
    (55, 56, 23),
    (56, 57, 24),
    (57, 58, 25),
      
    # left hand - 4th finger
    (59, 60, 27),
    (60, 61, 28),
    (61, 62, 29),
      
    # left hand - 5th finger
    (63, 64, 31),
    (64, 65, 32),
    (65, 66, 33)
)

  structure = pose + hands
    
  return structure


# Computing number of joints and limbs
def structureStats(structure):
    ps = {}
    ls = {}
    for a, b, l in structure:
        ps[a] = "gotcha"
        ps[b] = "gotcha"
        ls[l] = "gotcha"
    return len(ls), len(ps)
