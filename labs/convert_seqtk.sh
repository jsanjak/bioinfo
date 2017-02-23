#!/bin/sh

cd $3

${HOME}/bin/seqtk seq -Q64 -V $1 | gzip -c > ${3}/${2} 
