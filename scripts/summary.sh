#!/usr/bin/env bash

count=0
echo "$(date)" >  SUBMISSION
echo "Algorithms used for the submission:" >> SUBMISSION
for input in data/[a_,b_,c_,d_,e_,f_]*.txt;
do
    test_name=$(echo $input | cut -d'/' -f 2 | cut -d'.' -f 1)

    echo "======================================================"
    echo "Processing input $input"
    echo "======================================================"
    python3 scripts/dataset_summary.py --in $input
    if [[ $? -ne 0 ]]; then
        exit 1;
    fi
    (( count++ ));

done
