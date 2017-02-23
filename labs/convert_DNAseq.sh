#!/bin/sh

#This script updates the DNA sequence data to a modent format
cd Bioinformatics_Course/DNAseq
for ifile in original/*
do
    ofile=$(basename $ifile)
    qsub -q krt,krti,bio,pub64 -N convert_${ofile} ../../convert_seqtk.sh $ifile $ofile `pwd` 
done


