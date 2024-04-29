python3.9 train_rgs.py test \
	--dataroot ./datasets/mesh_simplify/ \
	--batch_size 32 --augment_scale --n_classes 40 \
	--channels 10 --patch_size 64 \
  --n_epoch 1 --name "manifoldBase" \
	--lr_milestones "30 60"  --optim "adamw" \
	--weight_decay 0.1 \
	--lr 1e-4 \
	--depth 12 \
	--heads 12 \
	--encoder_depth 12 \
	--decoder_depth 6 \
	--decoder_dim 512 \
	--decoder_num_heads 16 \
  --checkpoint "./checkpoints/Body.pkl" \
	--num_warmup_steps "2" \
	--dim 768
