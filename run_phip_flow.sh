#!/bin/bash

set -e
source /app/lmod/lmod/init/profile

module load nextflow
module load Singularity
export PATH=$SINGULARITYROOT/bin/:$PATH

/usr/bin/time nextflow  \
    -C phipflow.config.best \
    run ../../../../phip-flow/PhIP-Flow.nf \
    -with-report output_local/nextflow_report.html \
    -work-dir /fh/scratch/delete30/matsen_e/jgallowa/temp/work/ \
