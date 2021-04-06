# PhIP-Flow pipeline Template/Example

In this template we provide a template/example outlining the details of running the PhIP-Flow pipeline to obtain the alignments for a phip-seq experiment -- which is organized into the xarray-format needed to run analysis using [phippery](https://github.com/matsengrp/phippery)

# Getting started

In order to run the example locally, you should first have [Docker](https://www.docker.com/products/docker-desktop) and [Nextflow](https://www.nextflow.io/docs/latest/getstarted.html) installed locally. This Example was generated with the following versions:

```bash
(base) ubuntu ~ » docker -v
Docker version 20.10.1, build 831ebea
(base) ubuntu ~ » nextflow -v
nextflow version 20.04.1.5335
```

Next, you will need to either clone this repository, or use it's template to fork, making sure to grab the [phip-flow](https://github.com/matsengrp/phippery) pipeline submodule 

```bash
git clone git@github.com:matsengrp/phip-flow-template.git --recurse-submodules
cd phip-flow-template
``` 

Nextflow allows for the user to avoid mangling installs for all the various dependencies by using containers for each process. In the config script `phipflow.config.docker` a docker container has been specified for each processing step of the pipeline. Nextflow will automatically pull the containers and run the pipeline with the specified config file with a `nextflow call`

```bash
nextflow -C phipflow.config.docker run phip-flow/PhIP-Flow.nf
```

In the local docker example,
