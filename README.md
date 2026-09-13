# Causal Entropic Forces

_Causal Entropic Forces_ [[Wissner-Gross & Freer, 2013a]](http://math.mit.edu/~freer/papers/PhysRevLett_110-168702.pdf) is a 2013 paper by [Alexander Wissner-Gross](https://www.alexwg.org/) and [Cameron Freer](https://www.cfreer.org/). The paper describes an agent that acts to maximize causal entropy: a measure of the diversity of futures in an agent-environment system. The authors argue that such behavior mathematically formalizes the word "intelligence." They justify their argument with computer simulations showing that intelligent behaviors of tool use and multi-agent cooperation emerge from maximizing causal entropy.

This repository reimplements the simplest experiment (the particle in a box) in _Causal Entropic Forces_ [[2013a, Fig.2a](http://math.mit.edu/~freer/papers/PhysRevLett_110-168702.pdf), [2013b, pp. 2-3, 10–11](https://journals.aps.org/prl/supplemental/10.1103/PhysRevLett.110.168702)]. Under causal entropic forcing, a particle in a box (begins to) move towards the center of the box (more recent positions are shown in darker colors):

![particle](https://raw.githubusercontent.com/dyth/causal-entropic-forces/refs/heads/main/images/towards_center.png)
<!-- ![Simulation](https://raw.githubusercontent.com/dyth/causal-entropic-forces/refs/heads/main/images/particle-in-a-box.gif) -->

See https://github.com/dyth/causal-entropic-forces/blob/main/tutorial.ipynb for a detailed tutorial about the mathematics.

See https://github.com/dyth/causal-entropic-forces/blob/main/jax_cef_code_tutorial.ipynb for a high-level tutorial that givs some intuitions about the code.


## Installation

```commandline
conda create --name entropica python=3.14.7
conda activate entropica
pip install notebook==7.6.2 ipython==9.17.1 numpy==2.5.3 matplotlib==3.11.2 scipy==1.18.1 ipympl==0.10.0
```

To run the JAX notebook, JAX needs to be installed:
```commandline
pip install jax=0.10.2
```

On MacOS, `jax-mps` (https://github.com/tillahoffmann/jax-mps) speeds up JAX execution.
```commandline
pip install jax-mps==0.10.11
```

Test the JAX installation with
```
python -c "import jax; print(jax.default_backend())"
```

A nice way to run the jupyter notebook from a remote server is
```commandline
nohup jupyter notebook --no-browser --ip 0.0.0.0 &
```
