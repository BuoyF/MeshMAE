import subprocess
import os

# # Construct the command with flags
command = [
    "python", "train_rgs.py", "train", 
    '--dataroot', './dataset/mesh_simplify/', 
    '--batch_size', '16', 
    '--augment_scale', 
    '--n_classes', '40', 
    '--channels', '10',
    '--patch_size', '64',
    '--n_epoch', '100',
    '--name', 'manifoldBase',
    '--lr_milestones', '30',
    '--optim', 'adamw',
    '--weight_decay','0.1',
    '--lr', '1e-4',
    '--depth', '12', 
    '--heads', '12', 
    '--encoder_depth', '12', 
    '--decoder_depth', '6', 
    '--decoder_dim', '512', 
    '--decoder_num_heads', '16', 
    '--checkpoint', 'none', 
    '--num_warmup_steps', '2',
    '--dim', '768'
    ]


result = subprocess.run(command, capture_output=True, text=True)
print("Output from train_rgs.py:")
print(result.stdout)
print(result.stderr)

# os.system("python train_rgs.py train --dataroot ./datasets/mesh_simplify/ --batch_size 32 \
#           --augment_scale --n_classes 40 --channels 10 --patch_size 64 --n_epoch 100 \
#           --name manifoldBase --lr_milestones 30 --optim adamw --weight_decay 0.1 \
#           --lr 1e-4 --depth 12 --heads 12 --encoder_depth 12 --decoder_depth 6 --decoder_dim 512 \
#           --decoder_num_heads 16 --checkpoint none --num_warmup_steps 2 --dim 768")