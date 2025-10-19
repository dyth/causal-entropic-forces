# Causal Entropic Forces

This repository reimplements the particle in a box experiment as described by Wissner-Gross & Freer [[2013a, Fig.2a](http://math.mit.edu/~freer/papers/PhysRevLett_110-168702.pdf), [2013b, pp. 2-3, 10–11](https://journals.aps.org/prl/supplemental/10.1103/PhysRevLett.110.168702)].

The code does not work.

The particle-in-a-box does not move towards the center of the plot.

![particle](https://raw.githubusercontent.com/dyth/causalEntropicForces/secondImplementation/images/particle.png)

I welcome any help!

See `tutorial.ipynb`.



## Installation

```commandline
conda create --name entropica python=3.13.4
conda activate entropica
pip install notebook==7.2.2 ipython==8.29.0 numpy==2.1.2 matplotlib==3.9.2 scipy==1.14.1
```

[//]: # (```commandline)
[//]: # (nohup jupyter notebook > log.txt 2>&1 &)
[//]: # (```)

A nice way to run the jupyter notebook from a remote server is using the command
```commandline
nohup jupyter notebook --no-browser --ip 0.0.0.0 &
```
