#!/bin/sh

export PATH=hercules/linux/64/bin:$PATH
export LD_LIBRARY_PATH=hercules/linux/64/lib:hercules/linux/64/lib/hercules:$LD_LIBRARY_PATH

python3 patch_cckd.py $GZCTF_FLAG
export GZCTF_FLAG=""
./mvs