# Notes on Nathan Wiebe's Lecture on quantum Walks

These notes are based on [lecture 27](https://www.youtube.com/watch?v=fAHX-AI4XKs&ab_channel=NathanWiebe) and [lecture 28](https://www.youtube.com/watch?v=-6-xtwMHaGM&t=1358s&ab_channel=NathanWiebe) of Nathan Wiebes quantum computing lecture series on youtube. The first lecture introduces quantum walks and the second explores the application of Szegedy quantum walks to the search problem.


### The search problem

Suppose we are given a finite set of elements  $`V`$  in which there is a distinguished subset  $`M\subseteq V`$ . Furthermore, we aren't able to directly interact with  $`V`$  but instead with an oracle  $`P`$  that samples from  $`V`$  by some unknown distribution, and an oracle  $`O`$  that checks if an element is in the distinguished set. The goal of search is to find any element of  $`M`$ .

The restricted case, where  $`P`$  is the uniform distribution, is easily seen to be equivalent to unordered search for which the best classical algorithm runs in  $`O(N/M)`$  time in expectation and for which Grover's algorithm offers a quadratic speedup.

In the more general setting, we allow  $`P`$  to assume any distribution and for this distribution to change over time (i.e. after each sample) with the sole restriction that the distribution described by  $`P`$  at time  $`n+1`$  is only dependent on the outcome of the sample at time  $`n`$ . By also providing  $`\pi`$  to describe the distribution which we first sample from, we see that the pair  $`\pi, P`$  is a time homogenous Markov chain with  $`P`$  denoting the transition matrix. Note that the case where  $`\pi`$  and  $`P`$  are the uniform over all  $`n`$  reduces to unordered search.

### The transition matrix

We will restrict ourselves to considering irreducible, symmetric and aperiodic Markov chains and consider what the respective transition matrix looks like.

**An irreducible** Markov chain is one in which is there is exactly one communicating class, or in other words, where there is a path between any two pairs of vertices. Alternatively, we can say that the transition matrix  $`P`$  is irreducible if it does not act independently on any subspace spanned by any proper subset of the computational basis vectors. Consider, for example, the transition matrix

```math
P = 
\begin{pmatrix}
1/3 & 1/3 & 1/3\\
0 & 1 & 0\\
1/3 & 1/3 & 1/3 
\end{pmatrix}
```

In this case,  $`(1,0,0)`$  and  $`(0,0,1)`$  are right eigenvector of  $`P`$  with eigenvalue  $`2`$ . Thus  $`P`$  is reducible. 

Suppose a matrix  $`P \in \mathbb{R}^{n\times n}`$  has eigenvalues  $`\lambda_1 \ge \lambda_2 \ge ... \ge \lambda_n`$ , some of which may be repeating, and where  $`\max\{\lambda_1, |\lambda_n|\} \le r`$ . Then, if  $`P`$  is an irreducible non-negative matrix (such as an irreducible transition matrix) then by Peron Froebenius theorem
-  $`\lambda_1 = r`$  and  $`\lambda_1 > \lambda_2`$  (i.e.  $`\lambda_1`$  is non-repeating).
- The right eigenvector associated with  $`\lambda_1`$  is positive in the computational basis state and the only positive eigenvector
    - For a vector  $`\ket{\psi}`$  to be positive in basis  $`\ket{v_i}`$ , all its vector components in this basis must be positive.
    - Note that the left and right eigenvectors of a matrix share the same set of eigenvalues.
- If  $`P`$  is periodic with period  $`h`$  then there exists exactly  $`h`$  eigenvalues of the form  $`e^{i2\pi k/h}`$  for some integer  $`k`$ .

**A periodic** Markov chain is an irreducible Markov chain for which the greatest common denominator of the length of any cycle is greater than one. The period of a vertex is the greatest common denominator of the length of any cycle starting and ending at that vertex. Since the period of every vertex in a communicating class is the same every vertex in an irreducible Markov chain has the same period. It turns out that if this period is  $`h`$  then the transition matrix of the Markov chain has the property that  $`P^{h+1} = P`$ . The last condition of the Peron Froebenius theorem now makes sense since  $`e^{(h+1)(i2\pi k/h)}  = e^{i2\pi k/h}`$ .

**A symmetric** Markov chain is one where  $`P = P^T`$  so  $`P`$  is Hermitian and only has real eigenvalues. The only way for  $`P`$  to be periodic is if  $`h`$  is not one and evenly divides  $`2k`$  such that  $`e^{i2\pi k/h} = \pm 1`$ . Thus  $`h`$  must be even and the length of every cycle in the graph is even, which can only be true of bipartite graphs.

**An additonal useful result** is the Gershgorin circle theorem, which says that the value  $`r`$  (defined above) for any stochstic matrix is 1.

**The consequence** of these results is that a undirected, connected and non-bipartite Markov chain is symmetric, irreducible and aperiodic. By Gershgorin circle theorem, for any Markov chain, the upper bound on the maximum absolute value of the eigenvalues is one. Since the transition matrix is symmetric, its eigenvalues are real and therefore  $`1 \ge \lambda_1 \ge \lambda_2 ... \lambda_n \ge -1`$ . But by Froebenius statement 1, since the Markov chain is irreducible,  $`\lambda_1 = 1`$  and this is not repeated. Since the Markov chain is also aperiodic, by Froebenius statement 3,  $`\lambda_n > -1`$  (otherwise it would be a root of unity which implies periodicity). In all we have

```math
1 = \lambda_1 > \lambda_2 \ge \lambda_3 ... \lambda_n > -1.
```
 

Now it is convenient to define what's known as the spectral gap, which is  $`\delta = \lambda_1 - `$