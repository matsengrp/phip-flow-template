# PhIP-Flow pipeline Template/Example

In this template we provide a template/example outlining the details of running the [PhIP-Flow](https://github.com/matsengrp/phip-flow) pipeline to obtain the alignments for a phip-seq experiment -- which is organized into the [xarray](http://xarray.pydata.org/en/stable/) format needed to run analysis using [phippery](https://github.com/matsengrp/phippery)

# Getting started

In order to run the example locally, you should first have [Docker](https://www.docker.com/products/docker-desktop) and [Nextflow](https://www.nextflow.io/docs/latest/getstarted.html) installed locally. This Example was generated with the following versions:

```bash
(base) ubuntu ~ » docker -v
Docker version 20.10.1, build 831ebea
(base) ubuntu ~ » nextflow -v
nextflow version 20.04.1.5335
```

Next, you will need to clone this repository (or use it's template to fork), making sure to grab the [phip-flow](https://github.com/matsengrp/phip-flow) pipeline submodule 

```bash
git clone git@github.com:matsengrp/phip-flow-template.git --recurse-submodules
cd phip-flow-template
``` 

Nextflow allows for the user to avoid mangling installs for all the various dependencies by using containers for each process. In the config script `phipflow.config.docker` a docker container has been specified for each processing step of the pipeline. Nextflow will automatically pull the containers and run the pipeline with the specified config file with the `nextflow` command

```bash
nextflow -C phipflow.config.docker run phip-flow/PhIP-Flow.nf
```

Where `phipflow.config.docker` are your configurations. This will produce something like

```bash
(base) ubuntu template-test/phip-flow-template ‹master*› » ./run_phip_flow.sh
N E X T F L O W  ~  version 20.04.1
Launching `phip-flow/PhIP-Flow.nf` [romantic_bohr] - revision: 44d57f9950
executor >  local (39)
[76/c6613f] process > generate_fasta_reference (1) [100%] 1 of 1 ✔
[01/2aaf25] process > generate_index (1)           [100%] 1 of 1 ✔
[13/e3f044] process > short_read_alignment (12)    [100%] 12 of 12 ✔
[a3/c87e4d] process > sam_to_stats (12)            [100%] 12 of 12 ✔
[2e/95d787] process > sam_to_counts (12)           [100%] 12 of 12 ✔
[51/5f9134] process > collect_phip_data (1)        [100%] 1 of 1 ✔

10.43user 3.81system 0:51.48elapsed 27%CPU (0avgtext+0avgdata 401948maxresident)k
0inputs+4536outputs (3major+807788minor)pagefaults 0swaps
```

and produce all intermediate file links and corresponding counts [xarray](http://xarray.pydata.org/en/stable/) dataset organized with the sample and peptide metadata tables.

If you have the [phippery](https://github.com/matsengrp/phippery) python package installed, you can take a look at the results of the example run

```python
>>> import phippery
>>> ds = phippery.load("simulation-run.phip")
>>> ds.counts
<xarray.DataArray 'counts' (peptide_id: 10, sample_id: 12)>
array([[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
       [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
       [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
       [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
       [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
       [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
       [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
       [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
       [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
       [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]])
Coordinates:
  * sample_id   (sample_id) int64 0 1 2 3 4 5 6 7 8 9 10 11
  * peptide_id  (peptide_id) int64 0 1 2 3 4 5 6 7 8 9
```

For more about using the python package to query the dataset and analyze the data using a range of methods, see the <TODO>

# Compute process configurations

Nextflow allows for users of a pipeline to avoid interaction with the actual .nf script being run. Rather, the users may generate a config file which allows for uniform process execuation accross compute platforms. While you may run this small simulated example on your laptop - it's often desireable to run the pipeline on a cluster. The `phipflow.config.gizmo` gives an example of how to run the same example on the local Fred Hutch gizmo cluster nodes. To learn more about how to tailor the the configuration script for you own compute system, see the [Nextflow documentation](https://www.nextflow.io/docs/latest/config.html). The should be no reason to seek out containers other than the ones in the config scripts provided here. Just be sure to comment out the `bowtie1.3` container and uncomment the `bowtie2` container address if you wish to switch the alignment tool being used (see below).

## Pipeline knobs

Currently, the pipeline expects the user to generate their alignment index as well as perform the actual short read alignment using either [Bowtie](http://bowtie-bio.sourceforge.net/index.shtml) or [Bowtie2](http://bowtie-bio.sourceforge.net/bowtie2/index.shtml). The alignment tool and arguments supplied to the alignment call are specified in the configuration file `params` block. When deciding on an alignment tool consider the implications of default behavior, and be sure to use a corresponding container - a public `bowtie2` container is commented out in the configurations files provided.


