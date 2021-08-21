import sys
sys.path.append(".")
from train_net import *

cfg=Config('volleyball')

cfg.device_list="1,2"
cfg.training_stage=2
# /media/a5/image3/lj/result/stage1/[Volleyball_stage1_stage1]<2020-10-21_09-58-30>
cfg.stage1_model_path='/media/a5/image3/lj/result/stage1/[Volleyball_stage1_stage1]<2020-10-21_09-58-30>/stage1_epoch128_90.50%.pth'  #PATH OF THE BASE MODEL
cfg.train_backbone=False

cfg.batch_size=1#32
cfg.test_batch_size=1#4
cfg.num_frames=10
cfg.train_learning_rate=2e-4
cfg.lr_plan={41:1e-4, 81:5e-5, 121:1e-5}
# 修改学习率
# cfg.train_learning_rate=2.5e-5
# cfg.lr_plan={41:1.25e-5, 81:6.125e-6, 121:1.25e-6}

cfg.max_epoch=150
cfg.actions_weights=[[1., 1., 2., 3., 1., 2., 2., 0.2, 1.]]  

cfg.exp_note='Volleyball_stage2'
train_net(cfg)