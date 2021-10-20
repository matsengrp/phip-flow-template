#!/bin/bash

set -eu

/usr/bin/time nextflow  \
  -C phipflow_docker.config \
  run matsengrp/phip-flow/PhIP-Flow.nf -r main\
  -with-report ./output/nextflow_report.html \
  -work-dir ./output/work/ \
  -resume
