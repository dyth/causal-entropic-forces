# Causal Entropic Forces

This repository attempted to reimplement the particle in a box experiment as described
in Fig.2a of [Wissner-Gross & Freer, 2013](http://math.mit.edu/~freer/papers/PhysRevLett_110-168702.pdf) and pages 2-3 and 10-11 of [supplementary material](https://journals.aps.org/prl/supplemental/10.1103/PhysRevLett.110.168702).

The code does not work.
I am not sure why and would welcome any help!

The particle-in-a-box does not move towards the center of the plot.

![particle](https://raw.githubusercontent.com/dyth/causalEntropicForces/secondImplementation/images/particle.png)

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


## References

I highly recommend reading the following sources that helped me to
better understand this interesting work.

1. Causal Entropic Forces [[Wissner-Gross & Freer, 2013a]](http://math.mit.edu/~freer/papers/PhysRevLett_110-168702.pdf).
2. Supplementary Material to Causal Entropic Forces [[Wissner-Gross & Freer, 2013b]](https://journals.aps.org/prl/supplemental/10.1103/PhysRevLett.110.168702).
3. Comment: Causal entropic forces [[Kappen, 2013]](https://arxiv.org/abs/1312.4185).
4. Causal Entropic Forces: Intelligent Behaviour, Dynamics and Pattern Formation [[Hornischer, 2015]](https://pure.mpg.de/rest/items/item_2300851/component/file_2300850/content).
5. Fractal AI: A fragile theory of intelligence [[Cerezo & Ballester, 2018]](https://arxiv.org/abs/1803.05049).
