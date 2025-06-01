# Notes on 'Search via Quantum Walk'

## Preliminaries
In these notes I will use Dirac notation when referencing results in both Markov chain theory and quantum computing despite its use being unconventional in the former. I do this mainly because I find it easier to work in Dirac notation and because it will make the transition from Markov chain theory to quantum computing less jarring.

For a each element of the Markov chain with discrete and finite sample space  $`S`$ , we ascribe  $`x \in S`$  to a unit vector  $`\ket{x} \in \mathbb{R}^{|S|}`$  such that  $`b = \{\ket{x} : x \in S\}`$  forms an orthonormal basis of  $`\mathbb{R}^{|S|}`$ . All matrices will be written in this basis. Note that we are purely making a representational choice so this does not pose a restriction.


For a finite, irreducible and aperiodic Markov chain with transition matrix  $`P`$ , we can apply the Perron-Frobenius theorem in conjunction with the Gershgorin circle theorem to say that the eigenvalues of  $`P`$ ,  $`\lambda_i`$ , satisfy  $`1 = \lambda_1 > \lambda_2 \ge \lambda_3 \ge ... \ge \lambda_n > -1`$  where  $`\lambda_1`$  has algebraic and geometric multiplicity  $`1`$  with a left unnormalised eigenvector 

```math
\ket{\pi} = \sum_{x \in S} \braket{x | \pi}\ket{\pi}, \text{ s.t. } \sum_{x \in S} \braket{x|\pi} = 1 \text{ and } \forall x \text{ } 0 \le \braket{x|\pi} \le 1
```
 
which represents the stationary (and equilibiurm) distribution. There is also the right unnormalised eigenvector  $`\ket{\vec{1}}`$ , which is the vector with one in every entry. Details on what algebraic and geometric multiplicity mean are given [here](https://www.statlect.com/matrix-algebra/algebraic-and-geometric-multiplicity-of-eigenvalues). We denote  $`P^*`$  as the time reverse of  $`P`$  so  $`P^*_{x,y} = \pi_y P_{y,x}/\pi_x`$ . 


As we will see in the following sections, it will be useful for analysis to consider the matrix  $`D(P)`$  satisfying

```math
D(P)_{x,y} = \sqrt{P_{x,y}P^*_{y,x}} = \ket{\sqrt{\pi}}_xP_{x,y}/\ket{\sqrt{\pi}}_y\\
\implies D(P) = \text{diag}(\ket{\pi})^{1/2}P\text{diag}(\ket{\pi})^{-1/2} 
```


where  $`\text{diag}(\ket{\pi})`$  is a diagonal square matrix with the components of  $`\ket{\pi}`$  laid out along the diagonal. Notice that  $`D(P)`$  and  $`P`$  are [similar matrices](https://math.stackexchange.com/questions/8339/similar-matrices-have-the-same-eigenvalues-with-the-same-geometric-multiplicity) and therefore share the same eigenvalues with the same geometric multiplicity. Furthermore, its easy to see that  $`\ket{\sqrt{\pi}} = (\sqrt{\ket{\pi}_x})`$  is also the unique, normalised left and right eigenvector of  $`D(P)`$  associated with eigenvalue  $`1`$ .

```math
D(P)\ket{\sqrt{\pi}} = \text{diag}(\ket{\pi})^{1/2}P\ket{\bar{1}} = \text{diag}(\ket{\pi})^{1/2}\ket{\bar{1}} = \ket{\sqrt{\pi}}
```

and

```math
D(P)^\top\ket{\sqrt{\pi}} = \text{diag}(\ket{\pi})^{-1/2}P^\top \ket{\pi} = \text{diag}(\ket{\pi})^{-1/2}\ket{\pi} = \ket{\sqrt{\pi}}
```

This implies that  $`\ket{\sqrt{\pi}}`$  is a left and right singular vector of  $`D(P)`$  associated with singular value  $`1`$ . To see why, note that from [this tutorial](https://gregorygundersen.com/blog/2018/12/20/svd-proof/#4-textbfu_i-is-a-unit-eigenvector-of-aatop) on the SVD, the left and right singular vectors of a matrix  $`A`$  are the eigenvectors of  $`A^\top A`$  and  $`A A^\top`$  respectively. The associated singular values are the square root of the eigenvalues of  $`A^\top A`$ . In our case it's clear that  $`\ket{\sqrt{\pi}}`$  is an eigenvector of both  $`D(P)^\top D(P)`$  and  $`D(P)D(P)^\top`$  and their associated eigenvalue is  $`\sqrt{1} = 1`$ . 

From proposition 3 of this paper, it can be shown that all singular values of  $`D(P)`$  lie in the range  $`[0, 1]`$ . When  $`P`$  is reverisble, in which case  $`D(P)`$  is clearly symmetric and its singular values are the absolute of its eigenvalues. Since the eigenvalues of  $`D(P)`$  and  $`P`$  are equal, by the Gershgorin circle theorem which says that the singular values of  $`D(P)`$  lie in the range  $`[0,1]`$  *and*, the  $`1`$  singular value is unique with sinuglar vector  $`\ket{\sqrt{\pi}}`$ .


## Szegedy's quantum walk operator
The MNRS algorithm is entirely based on Szegedy's quantization of the classical random walk on a Markov chain. For each state  $`x \in S`$  we assign the corresponding quantum state  $`\ket{x}`$  such that, with the further inclusion of a reference state  $`\ket{\bar{0}}`$  the the set  $`b = \{\ket{x} : x \in S\} \cup \ket{\bar{0}}`$  forms an orthonormal basis of  $`\mathbb{C}^{|S|+1}`$ . If we duplicate this state space the set  $`b\times b`$  forms an orthonormal basis of the composite system. Szegedy quantizes the Markov chain by assuming access to the following oracles.

```math
U_A\ket{x}\ket{\bar{0}} = \sum_{y \in X} \sqrt{P_{x,y}}\ket{x}\ket{y} = \ket{x}\ket{p_x},\\
U_B\ket{\bar{0}}\ket{y} = \sum_{x\in X}\sqrt{P^*_{y,x}}\ket{x}\ket{y} = \ket{p^*_y}\ket{y}
```

for  $`x,y \in S`$ . Intuitively, the duplication of the state space can be viewed as transforming the Markov chain into a bipartite graph with duplicate vertices in each partition,  $`(S,S)`$ . Then  $`U_A`$  can be viewed as the unitary that maps a state in the left partition into a superposition of the edges from that state to states in the right parition with amplitudes dictated by  $`P`$ . And similarly for  $`U_B`$  but from right to left parition with edge weights dictated by  $`P^*`$   Defining the projections,  $`\Pi_A`$  and  $`\Pi_B`$ , as


```math
\Pi_A = \sum_x \ket{x}\ket{p_x}\bra{x}\bra{p_x},\\
\Pi_B = \sum_y \ket{p^*_y}\ket{y}\bra{p^*_y}\bra{y}
```


we have the walk operator


```math
W(P) = (2\Pi_A - I)(2\Pi_B - I)
```




which is a product of two reflections in the subspaces  $`A = \text{span}(\ket{x}\ket{p_x} : x \in X)`$  and  $`B = \text{span}(\ket{p^*_y}\ket{y} : y \in X)`$ . The left reflection can be built as


```math
2\Pi_A - I = 2\sum_x \ket{x}\ket{p_x}\bra{x}\bra{p_x} - I\\
= 2\sum_x U_A\ket{x}\ket{\bar{0}}\bra{x}\bra{\bar{0}} U_A^\dagger - I \\
= U_A(I\otimes (2\ket{\bar{0}}\bra{\bar{0}} - I))U_A^\dagger
```


where a reflection about the state  $`\ket{\bar{0}}`$  in the second register can be implemented with the controlled  $`Z`$  operation. Similarly for the right reflection. 

Theorem 1 of Mario Szegedy's [original paper](https://ieeexplore.ieee.org/document/1366222) on quantum walks shows how useful  $`W(P)`$  is. From my understanding, the most important parts of this theorem are that, if we write the singular values of  $`D(P)`$  as  $`\cos \theta_1 ... \cos \theta_l`$  for  $`\theta \in [0, \pi/2)`$ , then 
- The subspace  $`A + B = \{\ket{x} + \ket{y} : \ket{x} \in A, \ket{y} \in Y\}`$  is  $`W(P)`$  invariant. 
- The eigenvalues of  $`W(P)`$  in this subspace are  $`e^{\pm2i\theta_1} ... e^{\pm2i\theta_l}`$  and share the same geometric multiplicity as  $`D(P)`$ .
- The eigenspace corresponding to  $`\theta = 0`$  is  $`A \cap B = \{\ket{x} : \ket{x} \in A, \ket{x} \in B\}`$ . In other words,  $`W(P)`$  acts as the identity on this subspace.
-  $`A\cap B`$  is spanned by the left (and right) singular vectors of  $`D(P)`$  associated with  $`\theta = 0`$ .

The third point is somewhat obvious: for any  $`\ket{v} \in A \cap B`$  

```math
W(P)\ket{v} = (2\Pi_A - I)(2\Pi_B - I)\ket{v} = (2\Pi_A - I)\ket{v} = \ket{v}.
```

The fourth point is also easy to see. Consider the vector

```math
\ket{\sqrt{\pi}_p} = \sum_{x \in S} \sqrt{\ket{\pi}_x} \ket{x}\ket{p_x} = \sum_{y \in S} \sqrt{\ket{\pi}_y}\ket{p_y^*}\ket{y} 
```


Recall that the left singular vector of  $`D(P)`$  was  $`\ket{\sqrt{\pi}}`$ . Thus, Szegedy's theorem tells us that  $`\ket{\pi}`$  is a unique eigenvector of  $`W(P)`$  associated with phase  $`\theta = 0`$  (and we can verify this by checking  $`W(P)\ket{\pi} = \ket{\pi}`$ ) and that all other eigenvectors have phase  $`\theta > 0`$ . For analytical convenience, we denote  $`\Delta = 2\theta_s`$  where  $`\theta_s`$  is associated with the second largest singular value of  $`D(P)`$  (smallest non-zero phase).

## High level search algorithm

Our goal is to find an element of  $`M \subseteq X`$  which constitutes dome distinguished set. Consider the states


```math
\ket{u} = \frac{1}{\sqrt{p_M}}\sum_{x\in M}\sqrt{\pi_x}\ket{x}\ket{p_x},\\
\ket{u^\perp} = \frac{1}{\sqrt{1-p_M}}\sum_{x\notin M}\sqrt{\pi_x}\ket{x}\ket{p_x}
```


where  $`p_M = \sum_{x\in M} \pi_x`$  and  $`\pi_x`$  is the (non-zero) probability of sampling  $`x`$  from the stationary distribution. We have that


```math
\ket{\pi} = \sqrt{p_M}\ket{u} + \sqrt{1-p_M}\ket{u^\perp}
```


