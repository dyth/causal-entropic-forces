# Causal Entropic Forces

An attempt to reimplement the particle in a box experiment as described
in Fig.2a of [Wissner-Gross & Freer, 2013](http://math.mit.edu/~freer/papers/PhysRevLett_110-168702.pdf) and pages 2-3 and 10-11 of [supplementary material](https://journals.aps.org/prl/supplemental/10.1103/PhysRevLett.110.168702).

The code in its current state cannot reproduce the experiment reliably.
I am not sure why and would welcome any help!

Currently, the particle-in-a-box behaves as below and does not move
towards the center of the plot.

![particle](https://raw.githubusercontent.com/dyth/causalEntropicForces/secondImplementation/images/particle.png)

The algorithm works first by generating many random-walk paths through
the state-space -- here is a "light cone" plot of these random walks with
time on the vertical axis.

[//]: # (edited from https://stackoverflow.com/a/14747656)
<img src="https://raw.githubusercontent.com/dyth/causalEntropicForces/secondImplementation/images/lightcone.png" width="512" class="center"/>

I then perform PCA to reduce the dimensionality of the array formed from
concatenating the states of the random walk through time, and then perform
KDE (kernel density estimation) on these dimensionality-reduced random
walks.

Then, I compute the probability density of each random walk and normalize
them by their sum (ie a sum over samples) to produce volume fractions,
which can then be used in the algorithm on page 11 of the supplementary
material.



## Installation

```commandline
conda create --name entropica python=3.12
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
