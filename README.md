# Causal Entropic Forces

An attempt to reimplement the particle in a box experiment as described in Fig.2a of [Wissner-Gross & Freer, 2013](http://math.mit.edu/~freer/papers/PhysRevLett_110-168702.pdf) and pages 2-3 and 10-11 of [supplementary material](https://journals.aps.org/prl/supplemental/10.1103/PhysRevLett.110.168702).

The code in its current state does not reproduce the experiment reliably.

The agent in the experiment runs on an algorithm that three repeating steps.

1. Generate random walks throughout the environment from a start state.
![lightCone2D](https://raw.githubusercontent.com/dyth/causalEntropicForces/secondImplementation/images/particleBoxLightCone2D.png)

2. Use kernel density estimation to compute the likelihood of visiting a future state at the end of a random walk given the start state.
![path](https://raw.githubusercontent.com/dyth/causalEntropicForces/secondImplementation/images/density.png)

3. Update the start state to a new state in the direction towards the most-likely visited future state (given by black arrow).  As seen in the diagram above, the black arrow actually goes against the expected direction in the experiment, so there's an error with the code at the moment.

## Installation

Python 2.7 with the `numpy`, `matplotlib`, `scipy` libraries.

```
$ pip install numpy matplotlib scipy
```

## Run

Properties of the agent can be specified in `config.json`.

```
{
	"environment"      : "<name_of_python_file_with_environment_class>",
	"num_sample_paths" : 200, // number of paths to sample
	"plot"             : {true, false},
	"steps"            : 100, // number of steps within the policy
	"cur_macrostate"   : null // for use in plotting light cones
}
```

To design your own environment, ensure that it contains the same methods and variables as those in `particleBox.py`. The agent can then be run by the following command.

```
$ python agent.py
```
