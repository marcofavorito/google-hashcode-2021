#!/usr/bin/env bash

if [ "$#" -ne 1 ] && [ "$#" -ne 6 ]; then
    echo "Illegal number of parameters.";
    echo "Usage: $0 [ ALG | ALG_A ALG_B ALG_C ALG_D ALG_E ]";
    exit 1;
fi

if [ "$#" == 1 ]; then
    ALGS=("$1" "$1" "$1" "$1" "$1" "$1");
else
    ALGS=("$1" "$2" "$3" "$4" "$5" "$6");
fi

count=0
echo "$(date)" >  SUBMISSION
echo "Algorithms used for the submission:" >> SUBMISSION
for input in data/[a_,b_,c_,d_,e_,f_]*.txt;
do
    test_name=$(echo $input | cut -d'/' -f 2 | cut -d'.' -f 1)
    echo "- $test_name: ${ALGS[$count]}" >&1 | tee -a SUBMISSION
    output_filename="out/${test_name}.out"
    echo "Processing input $input, writing output in $output_filename"
    python3 -m hashcode --alg ${ALGS[$count]} < $input > $output_filename
    if [[ $? -ne 0 ]]; then
        exit 1;
    fi
    (( count++ ));

done

echo "Zipping the solution..."
./scripts/zipper.sh

#echo "The scores are:" >&1 | tee -a SUBMISSION;
#total_score=0;
#for f in $(find ./data/*.txt  -printf "%f\n" | cut -d'.' -f1);
#do
#    partial_score=$(./scripts/scorer --in data/$f.txt --solution out/$f.out)
#    total_score=$(echo "$total_score + $partial_score" | bc)
#    echo "- $f: $partial_score" >&1 | tee -a SUBMISSION
#done

echo "The total score of the submission is: ${total_score}" >&1 | tee -a SUBMISSION
echo "You can find a summary in the SUBMISSION file."