#!/bin/bash
#SBATCH --job-name=zrb2-slab-001-o-array
#SBATCH --partition=normal_q
#SBATCH --account=aiaa2026
#SBATCH --array=1-24
#SBATCH --nodes=1
#SBATCH --ntasks=64
#SBATCH --time=24:00:00
#SBATCH --mail-user=cganley2@vt.edu
#SBATCH --mail-type=END,FAIL
#SBATCH --output=slurm-%j.out
#SBATCH --error=slurm-%j.err

module load QuantumESPRESSO/7.4-foss-2024a

ls -d **/* > dir-list.txt
# Get the directory for this task
DIR=$(sed -n "${SLURM_ARRAY_TASK_ID}p" dir-list.txt)

cd "$DIR"

mpirun -np 64 pw.x -npool 2 -in pw.in > pw.out