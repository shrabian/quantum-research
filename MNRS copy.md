# Notes on 'Search via Quantum Walk'

## Preliminaries

For an irreducible and aperiodic Markov chain with finite state space  $`X`$  and transition matrix  $`P`$  we can apply the Perron-Frobenius theorem, in conjunction with the Gershgorin circle theorem to say that the eigenvalues of P,  $`\lambda_i`$ , satisfy  $`1 = \lambda_1 > \lambda_2 \ge \lambda_3 \ge ... \ge \lambda_n > -1`$  where  $`\lambda_1`$  has algebraic and geometric multiplicity  $`1`$  with a left normalised eigenvector  $`\vec{\pi}`$  (the equilibrium distribution) and right unnormalised eigenvector  $`\vec{1}`$ , which is the vector with one in every entry,. Details on what algebraic and geometric multiplicity mean are given [here](https://www.statlect.com/matrix-algebra/algebraic-and-geometric-multiplicity-of-eigenvalues). We denote  $`P^*`$  as the time reverse of  $`P`$  so  $`P^*_{x,y} = \pi_y P_{y,x}/\pi_x`$ . 


As we will see in the following sections, it will be useful for analysis to consider the matrix  $`D(P)`$  satisfying

```math
D(P)_{x,y} = \sqrt{P_{x,y}P^*_{y,x}} = \sqrt{\pi_x}P_{x,y}/\sqrt{\pi_y}\\
\implies D(P) = \text{diag}(\vec{\pi})^{1/2}P\text{diag}(\vec{\pi})^{-1/2} 
```


where  $`\text{diag}(\vec{\pi})`$  is a diagonal square matrix with the components of  $`\vec{\pi}`$  laid out along the diagonal. Notice that  $`D(P)`$  and  $`P`$  are [similar matrices](https://math.stackexchange.com/questions/8339/similar-matrices-have-the-same-eigenvalues-with-the-same-geometric-multiplicity) and therefore share the same eigenvalues with the same geometric multiplicity. Furthermore, its easy to see that  $`\sqrt{\vec{\pi}} = (\sqrt{\pi_x})`$  is also the unique left and right eigenvector of  $`D(P)`$  associated with eigenvalue  $`1`$ .

```math
D(P)\sqrt{\vec{\pi}} = \text{diag}(\pi)^{1/2}P\bar{1} = \text{diag}(\pi)^{1/2}\bar{1} = \sqrt{\vec{\pi}}
```

and

```math
\sqrt{\vec{\pi}}D(P) = \vec{\pi}P\text{diag}(\vec{\pi})^{-1/2} = \vec{\pi}\text{diag}(\vec{\pi})^{-1/2} = \sqrt{\vec{\pi}}
```

This implies that 
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

**(something about D(P) and P are in this basis).** Thus, Szegedy's theorem tells us that  $`\ket{\pi}`$  is a unique eigenvector of  $`W(P)`$  associated with phase  $`\theta = 0`$  (and we can verify this by checking  $`W(P)\ket{\pi} = \ket{\pi}`$ ) and that all other eigenvectors have phase  $`0 < \theta < \pi/2`$ , where the second equality comes from the fact that the phase factors are multiplied by two to get a final range of  $`[0,\pi]`$ . For analytical convenience, we denote  $`\Delta = 2\theta_s`$  where  $`\theta_s`$  is associated with the second largest singular value of  $`D(P)`$  (smallest non-zero phase).

## Assumptions of search and a classical algorithm

We assume in access to three oracles, each of which can be ascribed a cost and has a quantum and classical description.

(1) We assume accesss to an oracle that determines if a vertex is marked or not and that can be implemented (both classically and quantumly) at cost  $`\text{C}`$ . Classically this is given by a function

```math
f(x) = 
\begin{cases}
1 & \text{if } x \in M,\\
0 & \text{otherwise}
\end{cases} 
```

and the quantum analogue is

```math
U_f \ket{0}\ket{x} = 
\begin{cases}
\ket{1}\ket{x} & \text{if } x \in M,\\
\ket{0}\ket{x} & \text{otherwise}.
\end{cases}
```


We assume access to the walk operator which, in the classical case is  $`P`$  and in the quantum case is  $`W(P)`$ . We ascribe to each a cost  $`\text{C}`$ . Note that in the paper the authors actually assume the quantum walk operators are  $`U_A`$  and  $`U_B`$  each with cost  $`\text{C}`$  but since, clearly, we can build  $`W(P)`$  at cost  $`O(C)`$  we ignore this technicality.

The final assumption is access to the stationary distribution  $`\ket{\pi}`$  which, in the quantum case, is represented by  $`\ket{\sqrt{\pi}}`$ .

If we denote the hitting time of the set  $`M`$  from the initial state  $`\ket{\pi}`$  by  $`HT_{\pi, M}`$ , its clear that the classical search algorithm, which entails sampling from  $`\ket{\pi}`$  repeatedly walking with  $`P`$  while checking with  $`f`$  until a marked state is hit, runs in time

```math
O(S + HT_{\pi, M}(U + C))
```


## High level search algorithm

MNRS essentially is a Grover based search algorithm. We begin with the initial state 


```math
\ket{\sqrt{\pi}} = \sum_{x \in S} \sqrt{\pi_x} \ket{x}
```

which we can write

```math
\ket{\sqrt{\pi}} = \sqrt{p_M}\ket{m} + \sqrt{1-p_M}\ket{u}
```

where 

```math
\ket{m} = \frac{1}{\sqrt{p_M}}\sum_{x \in M} \sqrt{\pi_x} \ket{x},\\
\ket{u} = \frac{1}{\sqrt{1-p_M}}\sum_{x \in S/ M}\sqrt{\pi_x}\ket{x}
```

and 

```math
p_M = \sum_{x \in M} \pi_x.
```

We know from standard Grover's that if we are able to implement reflections

```math
R_m = 2\ket{m}\bra{m} - I\\
R_\pi = 2\ket{\sqrt{\pi}}\bra{\sqrt{\pi}} - I
```

and we start in an initial state  $`\ket{v} \in V`$  where  $`V = \text{span}(\ket{m}, \ket{u})`$  then repeated applications of  $`R_m`$  and  $`R_\pi`$  approximately produces  $`\ket{m}`$  in which case,  $`\ket{x}`$  for  $`x \in M`$  is measured with high probability. An important point to note here is that Grover's ensures that any state starting in  $`V`$  remains in  $`V`$  throughout.


We can build the reflection  $`R_m`$  in time  $`O(C)`$  with access to  $`U_f`$  simply by applying a  $`Z`$  rotation on the aniclliary state that  $`U_f`$  marks. The reflection  $`R_\pi`$  is harder to build and we dedicated the next two sections to its actualisation. We find that we can build  $`R_\pi`$  in time  $`O(1/\sqrt{\delta(P)}U)`$ . Therefore, supposing we know  $`p_M`$  exactly, the run time of the entire algorithm is


```math
O\left(S + \frac{1}{\sqrt{p_M}}\left(C + \frac{1}{\sqrt{\delta(P)}}U \right)\right)
```


If instead, a lower bound  $`\varepsilon \le p_M`$  is known then, we can use a variant of Grover's called randomised Grover's algorithm, where the number of iterations is randomly chosen from the range  $`[0, 1/\sqrt{\varepsilon}]`$ . It turns out that this variant does not change the correctness of Grover's search. It's time complexity is given by 


```math
O\left(S + \frac{1}{\sqrt{\varepsilon}}\left(C + \frac{1}{\sqrt{\delta(P)}}U \right)\right)
```



## A first pass at exacting search
Suppose we can introduce a new register such that the initial state of the system is given by 


```math
\ket{\sqrt{\pi}}\ket{\bar{0}}
```

We refer to the combined two register system as the target system. It is then easy to prepare the state 

```math
U_A\ket{\sqrt{\pi}}\ket{\bar{0}} = \ket{\sqrt{\pi}_p} 
```

which is in  $`A + B`$ . The goal is to effect repeated applications of  $`R_m`$  and  $`R_\pi`$  on the first register of this initial state which, by the properties of the Grover algorithm, ensure that the first register remains in the subspace  $`V`$ . This in turn implies the state of the system remains in  $`A+B`$ . To see why, define  $`\phi`$  consider an arbitrary state which is in  $`A+B`$  and whose first register is in  $`V`$ 

```math
\ket{v} = \frac{\sin \theta}{\sqrt{p_M}}\sum_{x \in M} \sqrt{\pi_x}\ket{x}\ket{p_x} + \frac{\cos \theta}{\sqrt{1-p_M}}\sum_{x \notin M}\sqrt{\pi_x}\ket{x}\ket{p_x}
```

we have

```math
R_m \ket{v} =  \frac{\sin \theta}{\sqrt{p_M}}\sum_{x \in M} \sqrt{\pi_x}\ket{x}\ket{p_x} - \frac{\cos \theta}{\sqrt{1-p_M}}\sum_{x \notin M}\sqrt{\pi_x}\ket{x}\ket{p_x}
```

and

```math
R_\pi \ket{v} = \frac{\sin(2\phi - \theta)}{\sqrt{p_M}}\sum_{x \in M}\sqrt{\pi_x}\ket{x}\ket{p_x} + \frac{\cos(2\phi - \theta)}{\sqrt{p_M}}\sum_{x \notin M}\sqrt{\pi_x}\ket{x}\ket{p_x}
```

where  $`\phi`$  is defined such that  $` \sin \phi = \sqrt{p_M}`$ . Clearly  $`R_m \ket{v}, R_\pi \ket{v}`$  are in  $`A+B`$  and their first register is in  $`V`$ . It follows that the state of the system is always in  $`A+B`$ . This is an important property because we know that, restricted to this subspace, the operator  $`W(P)`$  can be given the spectral decomposition

```math
W(P) = \ket{\sqrt{\pi}_p}\bra{\sqrt{\pi}_p} + \sum_{j} e^{2i \theta_j} \ket{+ w_j}\bra{+ w_j} + \sum_{j} e^{-2i \theta_j} \ket{-w_j}\bra{-w_j}
```

where  $`\theta_j > 0`$ . That is  $`\ket{\sqrt{\pi}_p}`$  is the unique eigenvector with phase  $`0`$ , which is only true if we are restricted to  $`A+B`$ . It follows that if we can apply QPE to estimate the phases of the eigenvalues of  $`W(P)`$  associated with the eigenvectors of  $`W(P)`$  that span  $`A+B`$  (and consequently makeup  $`\ket{v}`$ ) then the ancilliary control register we introduce should be in a superposition of these phases. Applying a zero controlled  $`Z`$  gate reflects along the  $`\ket{\sqrt{\pi}_p}`$  axis which effectively implements  $`-R_\pi`$  on the first target register. 

Let's be more specific. Suppose that at some given time we are in the state  $`\ket{v} \in V \subseteq A+B`$ . We know that  $`\ket{v}`$  can be decomposed into the eigenvectors of  $`W(P)`$  such that


```math
\ket{v} = a_0\ket{\sqrt{\pi}_p} + \sum_{j} a^+_j \ket{+w_j} + \sum_j + a^-_j\ket{-w_j}
```

We now introduce a second register such that the state of the composite system is given by

```math
\ket{v}\ket{0}^{ks}
```

where  $`k`$  is any integer and  $`s =\lceil{\log_2(\frac{2\pi}{\Delta(P)})\rceil}`$ . We start with the case where  $`k=1`$ . There is a well known algorithm called quantum phase estimation (QPE) which, given access to an eigenvector of  $`W(P)`$  in the first register and access to controlled  $`W(P)`$ , can encode the eigenphase of  $`W(P)`$  associated with the eigenvector onto the second register at cost  $`O(1/\Delta(P)U)`$ . Suppose,  $`\ket{v}`$  is an eigenvector of  $`W(P)`$  and  $`\ket{\omega}`$  is the state of the second register after QPE. QPE guarantees that, if  $`\ket{v} = \ket{\sqrt{\pi}_p}`$ , then  $`\ket{\omega} = \ket{0}^s`$  and if instead  $`\ket{v}`$  is some other eigenvector with phase  $`\theta > 0`$ , then 

```math
\braket{0^s|\omega} = \sin(2^s \theta)/2^s\sin(\theta)<1/2
```

where the second equality comes from the fact that  $`\Delta(P)/2 \le \theta \le \pi/2`$ . Rather unintuitively, phases closer to the zero phase produce  $`\ket{\omega}`$  more distinguished from  $`\ket{0}^s`$ . Consider the smallest phase factor  $`\Delta(P)/2`$ .

```math
\braket{0^s|\omega} = \sin\left(2^{\log_2(\frac{2\pi}{\Delta(P)})}\frac{\Delta(P)}{2}\right)/const = \sin \left(\frac{2\pi \Delta(P)}{2\Delta(P)}\right)/const = 0
```

And the largest possible phase factor

```math
\braket{0^s|\omega} = \sin\left(2^{\log_2(\frac{2\pi}{\Delta(P)})}\frac{\pi}{2}\right)/2^{\log_2(\frac{2\pi}{\Delta(P)})}\sin(\pi/2)=\frac{\Delta(P)\sin(\pi^2/\Delta(P))}{2\pi} < 1/2
```

where the inequality follows from the fact that  $`\Delta(P)<\pi/2`$  and therefore  $`\Delta(P)\sin(x) < \pi`$ . More generally,  $`\ket{v}`$  is a superposition of the eigenvectors of  $`W(P)`$  and so the state of the system after QPE can be written


```math
QPE\ket{v}\ket{0}^s = a_0\ket{\sqrt{\pi}_p}\ket{0^s} + \sum_{j} a^+_j \ket{+w_j}\ket{\omega_j} + \sum_j + a^-_j\ket{-w_j}\ket{\omega_j}
```

which can in turn be further decomposed

```math
QPE\ket{v}\ket{0}^s= a_0\ket{\sqrt{\pi}_p}\ket{0^s} + \sum_{\pm j} a^{\pm}_j\braket{0^s|\omega_j} \ket{w_j}\ket{0^s} + \sum_{\pm j} a^{\pm}_j(1-\braket{0^s|\omega_j}) \ket{w_j}\ket{{\not{0}}}\\

=: a_0\ket{\sqrt{\pi}_p}\ket{0^s} + \ket{v_0}\ket{0^s} + \ket{v_1}
```


Since each  $`\braket{0|\omega_j} < 1/2, \braket{0^s|v_0} < 1/2`$ . We now attempt to decrease  $`\braket{0|v_0}`$ . We do so by choosing a larger  $`k`$  such that we have  $`k`$  copies of  $`\ket{0}^s`$ . We can run QPE  $`k`$  many times, each time with the same first register and with a new second register. The fact that we reuse the first register in each application of QPE does not effect the output of the second register since the first register will only ever be changed by phase factors that we may absorb into the amplitudes without effecting measurement probabilities. The state of the system is thus

```math
QPE\ket{v}\ket{0}^{ks}= a_0\ket{\sqrt{\pi}_p}\ket{0^{ks}} + \sum_{\pm j} a^{\pm}_j\braket{0^{ks}|\omega_j} \ket{w_j}\ket{\omega^0_j} + \sum_{\pm j} a^{\pm}_j(1-\braket{0^{ks}|\omega_j}) \ket{w_j}\ket{\omega^{\not{0}}_j}\\

=: a_0\ket{\sqrt{\pi}_p}\ket{0^{ks}} + \ket{v_0} + \ket{v_1}
```

Since the contents of each of the  $`k`$  registers are independent of one another, it follows that  $`||\ket{v_0}|| \le 2^{-k}`$ . Thus we can approximate  $`R_\pi`$  by first applying QPE, then the reflection  $`2\ket{0^{ks}}\bra{0^{ks}} - I`$  on the  $`k`$  second registers, and finally reverse the phase estimation such that the second registers revert to all zeros. The total cost of this procedure is  $`O(kU/\Delta(P))`$ . Suppose we denote this circuit by  $`R(P)`$ . For any  $`\ket{v}`$  orthogonal to  $`\ket{\sqrt{\pi}_p}`$  its clear that 

```math
||(R(P)+I)\ket{v}|| = ||(R(P)+I)(\ket{v_0}+\ket{v_1})|| = ||\ket{v_0}-\ket{v_1} + \ket{v_0} + \ket{v_1}|| = 2||\ket{v_0}|| \le 2^{1-k}
```


Thus the algorithm described in the previous section reduces to iteratively applying  $`R(P)`$  and  $`R_m`$  as opposed to  $`R_\pi`$  and  $`R_m`$ . The question becomes whether this allows for arbitrary approximation of Grover's algorithm. We show by induction that at any time  $`i`$ , the state  $`\ket{\phi_i}`$  achieved after  $`i`$  iterations of exact Grover's and the state  $`\ket{\psi_i}`$  achieved after  $`i`$  iterations of approximate Grover's has overlap  $`||\ket{\psi_i} - \ket{\phi_i}|| \le i2^{1-k}`$ . Clearly this is true when  $`i = 0`$  since at this point both algorithms are in the initial state  $`\ket{\sqrt{\pi}_p}`$  in the first register. In the inductive case we have


```math
||\ket{\psi_{i+1}} - \ket{\phi_{i+1}}|| = ||R(P)R_m\ket{\psi_i}-R_\pi R_m \ket{\phi_i}||\\
= ||R(P)R_m(\ket{\phi_i} + (\ket{\psi_i}-\ket{\phi_i}))-R_\pi R_m \ket{\phi_i}||\\
=||R(P)R_m\ket{\phi_i} - R_\pi R_m \ket{\phi_i} + R(P)R_m(\ket{\psi_i}- \ket{\phi_i})|| \\
\le ||R(P)R_m\ket{\phi_i} - R_\pi R_m \ket{\phi_i}|| + ||R(P)R_m(\ket{\psi_i}- \ket{\phi_i})||\\
\le||R(P)R_m\ket{\phi_i} - R_\pi R_m \ket{\phi_i}|| + i2^{1-k}
```

where the last equality invokes the inductive hypothesis. Since  $`\ket{\phi_i} \in V`$  we have  $`R_m\ket{\phi_i} \in V`$  and this space is spanned by  $`\ket{\sqrt{\pi}_p}, \ket{\sqrt{\pi}_p^\perp}`$  so we can write

```math
R_m \ket{\phi_i} = a\ket{\sqrt{\pi}_p} + b\ket{\sqrt{\pi}_p^\perp}
```

It follows that

```math
||R(P)R_m\ket{\phi_i} - R_\pi R_m \ket{\phi_i}|| = ||R(P)(a\ket{\sqrt{\pi}_p} + b\ket{\sqrt{\pi}_p^\perp}) - R_\pi (a\ket{\sqrt{\pi}_p} + b\ket{\sqrt{\pi}_p^\perp})||\\
=||bR(P)\ket{\sqrt{\pi}_p^\perp} + b\ket{\sqrt{\pi}_p^\perp}|| = |b|||(R(P)+I)\ket{\sqrt{\pi}_p^\perp}|| \\
< |b|2^{1-k} < 2^{1-k}
```
.
Thus we have 

```math
||\ket{\psi_{i+1}} - \ket{\phi_{i+1}}|| \le 2^{1-k} + i2^{1-k} = (i+1)2^{1-k}
```


At time  $`1/\varepsilon`$  we have 

```math
||\ket{\psi_T} - \ket{\phi_T}||=2^{1-k}/\varepsilon
```

Clearly, if we choose  $`k = \log_2(1/\varepsilon) + c`$  this becomes  $`2^{1-c}`$  which we can make arbitrarily small with large enough  $`c`$ . Finally, using the fact that  $`\Delta(P) \in \Theta(\sqrt{\delta(P)})`$ , we have that


```math
O\left(S + \frac{1}{\sqrt{\varepsilon}}\left(C + \frac{\log T}{\sqrt{\delta(P)}}U \right)\right)
```


## A second pass at exacting search
This part is all about removing the  $`\log 1/\varepsilon`$  factor from the above time complexity.