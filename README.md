# Causal Entropic Forces

_Causal Entropic Forces_ [[Wissner-Gross & Freer, 2013a]](http://math.mit.edu/~freer/papers/PhysRevLett_110-168702.pdf) is a 2013 paper by [Alexander Wissner-Gross](https://www.alexwg.org/) and [Cameron Freer](https://www.cfreer.org/). The paper describes an agent that takes actions to maximize the diversity of future paths in an environment. The authors argue that such behavior mathematically formalizes the word "intelligence"—and justify doing so with computer simulations showing that intelligent behaviors of tool use and multi-agent cooperation emerge from maximizing causal entropy.

This repository reimplements the particle in a box experiment as described by Wissner-Gross & Freer [[2013a, Fig.2a](http://math.mit.edu/~freer/papers/PhysRevLett_110-168702.pdf), [2013b, pp. 2-3, 10–11](https://journals.aps.org/prl/supplemental/10.1103/PhysRevLett.110.168702)].

Under causal entropic forcing, a particle in a box begins to move towards the center of the plot (I have not ran the simulation for sufficiently long timesteps for it to reach the center—the following plot took ~2 hours to generate on my laptop):

![particle](https://raw.githubusercontent.com/dyth/causal-entropic-forces/refs/heads/main/images/towards_center.png)



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
