CUDA_VISIBLE_DEVICES=1 nohup python prompt1_7b.py > prompt1_7b_full.out 2>&1 &
CUDA_VISIBLE_DEVICES=2 nohup python prompt1_13b.py > prompt1_13b_full.out 2>&1 &
CUDA_VISIBLE_DEVICES=3 nohup python prompt2_7b.py > prompt2_7b_full.out 2>&1 &
CUDA_VISIBLE_DEVICES=4 nohup python prompt2_13b.py > prompt2_13b_full.out 2>&1 &