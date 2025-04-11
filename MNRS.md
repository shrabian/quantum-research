# Notes on 'Search via Quantum Walk'

## Preliminaries

For an irreducible and aperiodic Markov chain with finite state space  $`X`$  and transition matrix  $`P`$  we can apply the Perron-Frobenius theorem, in conjunction with the Gershgorin circle theorem to say that the (possible repeated) eigenvalues of P,  $`\lambda_i`$ , satisfy  $`1 = \lambda_1 > \lambda_2 \ge \lambda_3 \ge ... \ge \lambda_n > -1`$  where  $`\lambda_1`$  has algebraic and geometric multiplicity  $`1`$  with a left normalised eigenvector  $`\vec{\pi}`$  (the equilibrium distribution) and right unnormalised eigenvector  $`\vec{1}`$  (which is the vector with one in every entry). Details on what algebraic and geometric multiplicity mean are given [here](https://www.statlect.com/matrix-algebra/algebraic-and-geometric-multiplicity-of-eigenvalues). We denote  $`P^*`$  as the time reverse of  $`P`$  so  $`P^*_{x,y} = \pi_y P_{y,x}/\pi_x`$ . 


As we will see in the following sections, it will be useful for analysis to consider the matrix  $`D(P)`$  satisfying

```math
D(P)_{x,y} = \sqrt{P_{x,y}P^*_{y,x}} = \sqrt{\pi_x}P_{x,y}/\sqrt{\pi_y}\\
\implies D(P) = \text{diag}(\vec{\pi})^{1/2}P\text{diag}(\vec{\pi})^{-1/2} 
```


where  $`\text{diag}(\vec{\pi})`$  is a diagonal square matrix with the components of  $`\vec{\pi}`$  laid out along the diagonal. Notice that  $`D(P)`$  and  $`P`$  are [similar matrices](https://math.stackexchange.com/questions/8339/similar-matrices-have-the-same-eigenvalues-with-the-same-geometric-multiplicity) and therefore share the same eigenvalues with the same geometric multiplicity. Furthermore, its easy to see that  $`\sqrt{\vec{\pi}} = (\sqrt{\pi_x})`$  is also the unique left and right eigenvector of  $`D(P)`$  associated with eigenvalue  $`1`$ .

```math
D(p)\sqrt{\vec{\pi}} = \text{diag}(\pi)^{1/2}P\bar{1} = \text{diag}(\pi)^{1/2}\bar{1} = \sqrt{\vec{\pi}}
```
 
and similarly for  $`\sqrt{\vec{\pi}}D(P)`$ . Although I'm unclear on why, this fact implies  $`\sqrt{\vec{\pi}}`$  is also a singular vector of  $`D(P)`$  associated with singular value  $`1`$ . Now from proposition 3 of this paper, it can be shown that all singular values of  $`D(P)`$  lie in the range  $`[0, 1]`$  and that  $`D(P)`$  has exactly one singular value equal to  $`1`$ , for which the associated unqiue singular vector is  $`\sqrt{\vec{\pi}}`$ . In the special case where  $`P`$  is reversible, then  $`P = P^*`$  in which case we have 

```math
D(P)_{x,y} = \sqrt{P_{x,y}P_{y,x}} = D(P)_{y,x} 
```
 
So  $`D(P)`$  is symmetric (Hermitian) and can be diagonalised. In this case the singular values of  $`D(P)`$  are just equal to the absolute value of the eigenvalues of  $`P`$  and so we can just use  $`P`$  in our analysis below.

## Szegedy's quantum walk operator
We assume throughout that we have access to a unitary  $`U_{R}`$  and  $`U_L`$  whose actions are given by

```math
U_A\ket{x}\ket{0} = \sum_{y \in X} \sqrt{P_{x,y}}\ket{x}\ket{y} = \ket{x}\ket{p_x},\\
U_B\ket{0}\ket{y} = \sum_{x\in X}\sqrt{P^*_{y,x}}\ket{x}\ket{y} = \ket{p^*_y}\ket{y}
```

for  $`x,y \in X`$ . Intuitively, we can view  $`U_A`$  as putting walker in state  $`x`$  of the Markov chain in a probability weighted superposition of the out edges of  $`x`$ . Similarly,  $`U_B`$  does the same for a walker in state  $`y`$  of the time reversed Markov chain and with end points flipped. We denote the cost of applying one of these unitaries by  $`T`$ . Defining the projections,  $`\Pi_A`$  and  $`\Pi_B`$ , as


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
= 2\sum_x U_A\ket{x}\ket{0}\bra{x}\bra{0} U_A^\dagger - I \\
= U_A(I\otimes (2\ket{0}\bra{0} - I))U_A^\dagger
```


where a reflection about the state  $`\ket{0}`$  in the second register can be implemented with the controlled  $`Z`$  operation. Since we can use a similar construction for the right reflection, the total cost of building  $`W(P)`$  is  $`4T`$ . Theorem 1 of Mario Szegedy's [original paper](https://ieeexplore.ieee.org/document/1366222) on quantum walks shows how useful  $`W(P)`$  is. From my understanding, the most important parts of this theorem are that, if we write the singular values of  $`D(P)`$  as  $`\cos \theta_1 ... \cos \theta_l`$  for  $`\theta \in [0, \pi/2)`$ , then 
- The subspace  $`A + B = \{\ket{x} + \ket{y} : \ket{x} \in A, \ket{y} \in Y\}`$  is  $`W(P)`$  invariant. 
- The eigenvalues of  $`W(P)`$  in this subspace are  $`e^{\pm2i\theta_1} ... e^{\pm2i\theta_l}`$  and share the same geometric multiplicity as  $`D(P)`$ .
- The eigenspace corresponding to  $`\theta = 0`$  is  $`A \cap B = \{\ket{x} : \ket{x} \in A, \ket{x} \in B\}`$ . In other words,  $`W(P)`$  acts as the identity on this subspace.
-  $`A\cap B`$  is spanned by the left (and right) singular vectors of  $`D(P)`$  associated with  $`\theta = 0`$ .

The third point is somewhat obvious: for any  $`\ket{v} \in A \cap B`$  

```math
W(P)\ket{v} = (2\Pi_A - I)(2\Pi_B - I)\ket{v} = (2\Pi_A - I)\ket{v} = \ket{v}.
```

Recall that the left singular vector of  $`D(P)`$  was  $`\sqrt{\vec{\pi}}`$ . This can equivalently be written


```math
\ket{\pi} = \sum_{x \in X} \sqrt{\pi_x} \ket{x}\ket{p_x} = \sum_{y\in X} \sqrt{\pi_y}\ket{p^*_y}\ket{y}
```

**(something about D(P) and P are in this basis).** Thus, Szegedy's theorem tells us that  $`\ket{\pi}`$  is a unique eigenvector of  $`W(P)`$  associated with phase  $`\theta = 0`$  (and we can verify this by checking  $`W(P)\ket{\pi} = \ket{\pi}`$ ) and that all other eigenvectors have phase  $`\theta > 0`$ . For analytical convenience, we denote  $`\Delta = 2\theta_s`$  where  $`\theta_s`$  is associated with the second largest singular value of  $`D(P)`$  (smallest non-zero phase).

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


