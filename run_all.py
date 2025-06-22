
"""
Run All Crypto Trading Steps
----------------------------
This script executes the entire workflow of the FinRL crypto trading project:
1. Download trade data
2. Download train/validation data
3. Optimize strategies
4. Validate strategy
5. Backtest
6. Probability of Backtest Overfitting (PBO)
"""

import os

scripts = [
    "0_dl_trade_data.py",
    "0_dl_trainval_data.py",
    "1_optimize_cpcv.py",  # You can change to optimize_kcv or optimize_wf
    "2_validate.py",
    "4_backtest.py",
    "5_pbo.py"
]

for script in scripts:
    print(f"Running {script} ...")
    exit_code = os.system(f"python {script}")
    if exit_code != 0:
        print(f"❌ Error running {script}")
        break
    print(f"✅ Finished {script}\n")
