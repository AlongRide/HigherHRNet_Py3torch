# ------------------------------------------------------------------------------
# Copyright (c) Microsoft
# Licensed under the MIT License.
# Written by Bin Xiao (leoxiaobin@gmail.com)
# ------------------------------------------------------------------------------

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from yacs.config import CfgNode as CN


# pose_multi_resoluton_net related params
POSE_HIGHER_RESOLUTION_NET = CN()
POSE_HIGHER_RESOLUTION_NET.PRETRAINED_LAYERS = ['*']
POSE_HIGHER_RESOLUTION_NET.STEM_INPLANES = 64
POSE_HIGHER_RESOLUTION_NET.FINAL_CONV_KERNEL = 1

POSE_HIGHER_RESOLUTION_NET.STAGE1 = CN()
POSE_HIGHER_RESOLUTION_NET.STAGE1.NUM_MODULES = 1
POSE_HIGHER_RESOLUTION_NET.STAGE1.NUM_BRANCHES = 1
POSE_HIGHER_RESOLUTION_NET.STAGE1.NUM_BLOCKS = [4]
POSE_HIGHER_RESOLUTION_NET.STAGE1.NUM_CHANNELS = [64]
POSE_HIGHER_RESOLUTION_NET.STAGE1.BLOCK = 'BOTTLENECK'
POSE_HIGHER_RESOLUTION_NET.STAGE1.FUSE_METHOD = 'SUM'

POSE_HIGHER_RESOLUTION_NET.STAGE2 = CN()
POSE_HIGHER_RESOLUTION_NET.STAGE2.NUM_MODULES = 1
POSE_HIGHER_RESOLUTION_NET.STAGE2.NUM_BRANCHES = 2
POSE_HIGHER_RESOLUTION_NET.STAGE2.NUM_BLOCKS = [4, 4]
POSE_HIGHER_RESOLUTION_NET.STAGE2.NUM_CHANNELS = [24, 48]
POSE_HIGHER_RESOLUTION_NET.STAGE2.BLOCK = 'BOTTLENECK'
POSE_HIGHER_RESOLUTION_NET.STAGE2.FUSE_METHOD = 'SUM'

POSE_HIGHER_RESOLUTION_NET.STAGE3 = CN()
POSE_HIGHER_RESOLUTION_NET.STAGE3.NUM_MODULES = 1
POSE_HIGHER_RESOLUTION_NET.STAGE3.NUM_BRANCHES = 3
POSE_HIGHER_RESOLUTION_NET.STAGE3.NUM_BLOCKS = [4, 4, 4]
POSE_HIGHER_RESOLUTION_NET.STAGE3.NUM_CHANNELS = [24, 48, 92]
POSE_HIGHER_RESOLUTION_NET.STAGE3.BLOCK = 'BOTTLENECK'
POSE_HIGHER_RESOLUTION_NET.STAGE3.FUSE_METHOD = 'SUM'

POSE_HIGHER_RESOLUTION_NET.STAGE4 = CN()
POSE_HIGHER_RESOLUTION_NET.STAGE4.NUM_MODULES = 1
POSE_HIGHER_RESOLUTION_NET.STAGE4.NUM_BRANCHES = 4
POSE_HIGHER_RESOLUTION_NET.STAGE4.NUM_BLOCKS = [4, 4, 4, 4]
POSE_HIGHER_RESOLUTION_NET.STAGE4.NUM_CHANNELS = [24, 48, 92, 192]
POSE_HIGHER_RESOLUTION_NET.STAGE4.BLOCK = 'BOTTLENECK'
POSE_HIGHER_RESOLUTION_NET.STAGE4.FUSE_METHOD = 'SUM'

POSE_HIGHER_RESOLUTION_NET.DECONV = CN()
POSE_HIGHER_RESOLUTION_NET.DECONV.NUM_DCONVS = 2
POSE_HIGHER_RESOLUTION_NET.DECONV.NUM_CHANNELS = [32, 32]
POSE_HIGHER_RESOLUTION_NET.DECONV.NUM_BASIC_BLOCKS = 4
POSE_HIGHER_RESOLUTION_NET.DECONV.KERNEL_SIZE = [2, 2]
POSE_HIGHER_RESOLUTION_NET.DECONV.CAT_OUTPUT = [True, True]


MODEL_EXTRAS = {
    'pose_multi_resolution_net_v16': POSE_HIGHER_RESOLUTION_NET,
}
