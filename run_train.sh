python tools/dist_train.py \
    --cfg experiments/coco/higher_hrnet/w32_512_adam_lr1e-3.yaml \
    FP16.ENABLED True FP16.DYNAMIC_LOSS_SCALE True \
    MODEL.SYNC_BN True