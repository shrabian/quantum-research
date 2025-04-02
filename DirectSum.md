# Direct Sum

I've used chapters [1.8](https://opentext.uleth.ca/Math3410/sec-subspace-combine.html) and [5.4](https://opentext.uleth.ca/Math3410/sec-direct-sum.html) of Sean Fitzpatrick's online course on linear algebra, [this](https://people.maths.ox.ac.uk/flynn/genus2/alg0506/LALect02.pdf) set of Oxford lecture slides, and [this](https://planetmath.org/directsumofboundedoperatorsonhilbertspaces) planet math tutorial  to help understand the direct sum formalism better.

### Composing subspaces to form a subspace
Two ways to combine subspaces  $`U\subseteq V`$  and  $`W \subseteq V`$  together to form another subspace are intersection and addition, defined as follows.


```math
\begin{align}
U \cap W = \{\ket{x} : \ket{x} \in U \land \ket{x} \in W \}\\
U + W = \{\ket{u} + \ket{w} : \ket{u} \in U + \ket{w} \in W\}
\end{align}
```

A strategy to prove that each of (1) and (2) correspond to vector spaces is to apply the subspace test: check each have the  $`\boldmath{0}`$  vector and are closed under addition and scalar multiplication. 

 $`U + W`$   has the nice property that it is the smallest subspace for which  $`U`$  and  $`V`$  are both subspaces. That is, for any  $`X \subseteq V`$  satisfying  $`U, W \subseteq X`$ ,  $`U+W \subseteq X`$  (proven by showing that for all  $`\ket{u}, \ket{w} \in U,W`$ ,  $`\ket{u} + \ket{w} \in X`$ ). Additionally,  $`\text{dim}(U+W) = \text{dim}(U) + \text{dim}(W) - \text{dim}(U \cap W)`$  (proven by constructing a basis of  $`U+W`$  from the bases of  $`U, W`$  and  $`U\cap W`$ .)

### Direct sum of subpaces
For two subspaces where  $`U \cap W = \{\boldmath{0}\}`$ ,  $`U+W`$  is called the **direct sum** and given the notation  $`U\oplus W`$ . For all vectors  $`\ket{v}`$  in the composite subspace, there exists unique  $`\ket{u}, \ket{w} \in U, W`$  such that  $`\ket{v} = \ket{u} + \ket{w}`$ . Moreover, for any subspace  $`U`$ , there exists a subspace  $`W\subseteq V`$  such that  $`U\cap W = \{\boldmath{0}\}`$  and  $`U \oplus W = V`$ . This last fact can be proven by extending the basis of  $`U`$  to one that spans  $`V`$ . Finally,  $`\text{dim}(U\oplus W) = \text{dim}(U) + \text{dim}(W)`$ .

### Invariant subspaces
For a linear operator  $`T: V \rightarrow V`$ , a subspace  $`U \subseteq V`$  is  $`T`$ -invariant if for  $`\ket{u} \in U`$ ,  $`T\ket{u} \in U`$ . We can show the subspace is  $`T`$ -invariant if  $`T\ket{u_i} \in U`$  for all basis vectors  $`\boldmath{B}_U = \{\ket{u_i}\}`$  spanning  $`U`$ . If we denote  $`T_U`$  as the restriction of  $`T`$  on  $`U`$ , set  $`\boldmath{B}`$  to be the extension of  $`\boldmath{B}_U`$  to span  $`V`$  and define  $`M_{\boldmath{B}}(A)`$  to be the matrix representation of an operator  $`A`$  in basis  $`\boldmath{B}`$  then  


```math
M_{\boldmath{B}}(T) =
\begin{pmatrix}
M_{\boldmath{B}_U}(T_U) & \cdot &\\
\cdot & \cdot &
\end{pmatrix}
```


which gives a block encoding of  $`T_U`$ 

### Direct sum of operators
We call a linear operator,  $`T:V \rightarrow W`$  bounded if there is a non negative constant  $`c`$  such that  $`||T\ket{x}||_2 \le c||\ket{x}||_1`$  for all  $`\ket{x} \in V`$ . In quantum computing every operator we are concerned with will be bounded.

Consider the vector spaces  $`V = \bigoplus_i V_i`$  and  $`W = \bigoplus_i W_i`$ . The direct sum of the family of bounded operators  $`T_i : V_i \rightarrow W_i`$ . is given by


```math
T : V \rightarrow W = \bigoplus_i T_i : \bigoplus_i V_i \rightarrow \bigoplus_i W_i
```


For the bases  $`\boldmath{B}_V = \bigcup_i \boldmath{B}_{V_i}`$  and  $`\boldmath{B}_W = \bigcup_i \boldmath{B}_{W_i}`$  where  $`\boldmath{B}_{V_i}`$  and  $`\boldmath{B}_{W_i}`$  are bases of  $`V_i`$  and  $`W_i`$ 


```math
M_{\boldmath{B}_V, \boldmath{B}_W}(T) = 
\begin{pmatrix}
M_{\boldmath{B}_{V_1}, \boldmath{B}_{W_1}}(T_1) & 0 & 0 & \ldots\\
0 & M_{\boldmath{B}_{V_2}, \boldmath{B}_{W_2}}(T_2) & 0 & \ldots\\
0 & 0 & M_{\boldmath{B}_{V_3}, \boldmath{B}_{W_3}}(T_3)& \ldots\\
\vdots & \vdots & \vdots & \ddots
\end{pmatrix}
```



## Core Properties of the Direct Sum (From ChatGPT)
### **(i) Linearity**
The direct sum is **linear**, meaning:


```math
\bigoplus_{\lambda} (\alpha A_\lambda + \beta B_\lambda) = \alpha \bigoplus_{\lambda} A_\lambda + \beta \bigoplus_{\lambda} B_\lambda.
```


### **(ii) Behavior Under Addition**
For two direct sums:


```math
\bigoplus_{\lambda} A_\lambda + \bigoplus_{\lambda} B_\lambda = \bigoplus_{\lambda} (A_\lambda + B_\lambda).
```


This follows from the distributive property of matrix or operator addition.

### **(iii) Behavior Under Multiplication**
If  $` A = \bigoplus_{\lambda} A_\lambda `$  and  $` B = \bigoplus_{\lambda} B_\lambda `$ , then:


```math
AB = \bigoplus_{\lambda} (A_\lambda B_\lambda).
```


That is, multiplication acts component-wise in each direct sum block.

### **(iv) Identity Operator in Direct Sum Space**
The identity operator in a direct sum space is:


```math
I = \bigoplus_{\lambda} I_\lambda,
```


where  $` I_\lambda `$  is the identity operator on each subspace.

### **(v) Spectrum of a Direct Sum**
The spectrum (set of eigenvalues) of a direct sum operator is the **union** of the spectra of the individual operators:


```math
\sigma\left(\bigoplus_{\lambda} A_\lambda \right) = \bigcup_{\lambda} \sigma(A_\lambda).
```


This is useful in quantum mechanics when analyzing composite systems.

### **(vi) Kronecker Sum Relation**
In some cases, the **direct sum** of operators can be related to the **Kronecker sum**:


```math
A \oplus B = A \otimes I + I \otimes B.
```


However, this holds under specific tensor product structures.

### **(vii) Block Diagonal Matrix Representation**
If the direct sum is represented in matrix form, it corresponds to a **block diagonal matrix**:


```math
\bigoplus_{\lambda} A_\lambda = 
\begin{bmatrix}
A_1 & 0 & 0 & \dots \\
0 & A_2 & 0 & \dots \\
0 & 0 & A_3 & \dots \\
\vdots & \vdots & \vdots & \ddots
\end{bmatrix}.
```


This is crucial in practical calculations, where direct sum operators are often block-diagonal.