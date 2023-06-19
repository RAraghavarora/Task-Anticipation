#!/bin/bash
#SBATCH --time=72:00:00
#SBATCH --partition=long
#SBATCH --gres=gpu:1
#SBATCH -n 10
#SBATCH -J llama
#SBATCH --output=bob2.out
#SBATCH --error=bob2.err
#SBATCH --mail-type=all
#SBATCH --mail-user=reepicheep_logs@protonmail.com
#SBATCH --mem=50G
#SBATCH --reservation=rrc


source /home2/raghav.arora/miniconda3/etc/profile.d/conda.sh
conda activate habitat
torchrun try_llama.py
echo $?
