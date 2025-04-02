# Notes on 'Grand Unification of Quantum Algorithms'

This paper presents a pedagogical review of the QSVT. It is pedagogical in the sense that it aims to teach rather than present new knowledge. The work is structured to first introduce quantum signal processing (QSP), which is a 2-dimensional restriction of the QSVT, before lifting it to its generalisation. The reader of this work will come away with a clearer understanding of how the QSVT works and how it can generalise various important quantum algorithms including amplitude amplification, phase estimation and Hamiltonian simulation. The reader will not, however, gain a complete understanding of why the QSVT works mainly because, in formulating quantum signal processing (QSP), the main theorem presented (Theorem 1) is stated without proof. Further details of the proof are given in Gilyen's thesis 'Quantum Singular Value Transform and Its Algorithmic Applicaitons'


## Quantum Signal Processing

QSP is founded on the following idea.\
**Theorem 1.** *For any tuple of phases  $`\vec{\phi} = (\phi_0, \phi_1 ... \phi_d) \in \mathbb{R}^{d+1}`$  and a rotation operator*

```math
W(a) = 
\begin{pmatrix}
a & i\sqrt{1-a^2}\\
i\sqrt{1-a^2} & a
\end{pmatrix},
```

*which is an  $`x`$  rotation by angle  $`-2\cos^{-1}(a)`$ , we get*

```math
U_{\phi} = e^{i\phi_0 Z}\prod_{j=1}^{d}W(a)e^{i\phi_j Z} = 
\begin{pmatrix}
P(a) & iQ(a)\sqrt{1-a^2}\\
iQ^*(a)\sqrt{1-a^2} & P^*(a)
\end{pmatrix}.
```


*The functions  $`P`$  and  $`Q`$  are polynomials satisfying*
1. * $`\text{deg}(P) \le d`$  and  $`\text{deg}(Q) \le d-1`$ *
2. * $`P`$  has parity  $`d \mod 2`$  (i.e.  $`P`$  and  $`d`$  are both even or both odd) and  $`Q`$  has parity  $`d-1 \mod 2`$ .*
3. * $`|P|^2 + (1-a^2)|Q|^2 = 1`$ *

The neat thing about this theorem is that it is basis independent. In particular, matrices  $`W(a)`$  can be written with respect to different input and output bases (see Nielsen and Chuang ch2.1.2 for more clarity). We could, for example, have  $`W: V\rightarrow U`$  and so   $`W(a)e^{i\phi Z}`$  repeatedly maps between  $`V`$  and  $`U`$  with the  $`z`$  rotation changing with basis it is defined on. We will exploit this in the next section.

By measuring in different bases we can extract different properties of  $`U_\phi`$ . For example,  $`\bra{0}U_\phi \ket{0} = P(a)`$  and  $`\bra{+} U_\phi \ket{+} = \text{Re}(P(a)) + i\text{Re}(Q(a))\sqrt{1-a^2}`$ . Moreover, it turns out that for any given polynomial  $`P`$ , the corresponding tuple of phases  $`\vec{\phi}`$  generating that polynomial in QSP is efficiently calculated by a classical calculator (by determining the roots of the polynomial).

## QSP for amplitude amplification

The problem of amplitude amplification, in its most general form, can be stated as follows. Given unitaries  $`U`$ ,  $`U^\dag`$ ,  $`e^{i\phi \ket{A_0}\bra{A_0}}`$  and  $`e^{i\phi \ket{B_0} \bra{B_0}}`$  (which can greater than two dimensions) construct an efficient circuit  $`Q`$  so that  $`\bra{A_0}Q\ket{B_0} \rightarrow 1`$ , assuming the matrix element  $`\bra{A_0}U\ket{B_0} \neq 0`$ . I'll also include the additional assumption that  $`\bra{A_0}U\ket{B_0} \in \mathbb{R}`$  since we can always absorb any complex phase into  $`\ket{B_0}`$  e.g. by defining  $`\ket{B_0}' = \frac{\bra{A_0}U\ket{B_0}^*}{|\bra{A_0}U\ket{B_0}|}\ket{B_0}`$ .

First, we can consider the vectors  $`\ket{A_{\perp}}`$ , orthogonal to  $`\ket{A_0}`$ , and  $`\ket{B_\perp}`$ , orthogonal to  $`\ket{B_0}`$ . These are defined


```math
U\ket{B_0} = a\ket{A_0} + \sqrt{1-a^2}\ket{A_\perp}\\
U\ket{B_\perp} = -a\ket{A_\perp} + \sqrt{1-a^2}\ket{A_0}
```


For the above construction, we've used the fact that for any two vectors  $`\ket{u}`$  and  $`\ket{v}`$  we can find a  $`\ket{v_\perp}`$  orthogonal to  $`\ket{v}`$  such that  $`\ket{u} = a\ket{v} + b\ket{v_\perp}`$ . Note  $`\ket{A_\perp}`$  is defined so that its amplitude is real when  $`U\ket{B_0}`$  is decomposed. Its clear that, with respect to the input basis  $`\{\ket{B_0}, \ket{B_\perp}\}`$  (the  $`B`$  basis) and the output basis  $`\{\ket{A_0}, \ket{A_\perp}\}`$  (the  $`A`$  basis), the action of  $`U`$  is given by


```math
U = 
\begin{pmatrix}
a & \sqrt{1-a^2}\\
\sqrt{1-a^2} & -a
\end{pmatrix}
```


i.e.  $`U`$  acts on the  $`\ket{B_0}`$  and  $`\ket{B_\perp}`$  components of any vector in the vector space that  $`U`$  acts on, whose basis is the Gram-Schmidt extension of the  $`B`$  basis vectors, by the above and stores it in the  $`\ket{A_0}`$  and  $`\ket{A_\perp}`$  component of the same vector space (since unitary matrices are square) spanned by the Gram-schmidt extension of the  $`A`$  basis. We can write  $`U`$  as


```math
U = -ie^{i\pi/4 Z} W(a) e^{i\pi/4 Z}
```


Where the left and write  $`z`$  rotation operators are rotations in the  $`A`$  and  $`B`$  axes respectively. Moreover,  $`e^{i\phi \ket{A_0}\bra{A_0}}`$  and  $`e^{i\phi \ket{B_0}\bra{B_0}}`$  are also  $`z`$  rotations along their respective axes.


```math
\begin{align}
e^{i\phi \ket{A_0}\bra{A_0}} &= \exp \left(i\phi\ket{A_0}\bra{A_0} + 0\ket{A_\perp}\bra{A_\perp} \right)\\
&= I - (1-e^{i\phi})\ket{A_0}\bra{A_0}\\
& = 
\begin{pmatrix}
1 & 0\\
0 & 1
\end{pmatrix}
-(1-e^{i\phi})
\begin{pmatrix}
1 & 0\\
0 & 0
\end{pmatrix}\\
& = e^{i \phi/2}
\begin{pmatrix}
e^{i\phi/2} & 0\\
0 & e^{-\phi/2}
\end{pmatrix}
\end{align}
```

and symmetrically for  $`e^{i\phi \ket{B_0}\bra{B_0}}`$ . Thus


```math
\bra{A_0}\left(\prod_{k=1}^{d/2}Ue^{i\phi_{2k-1}\ket{B_0}\bra{B_0}}U^\dag e^{i\phi_{2k}\ket{A_0}\bra{A_0}}\right)U\ket{B_0} \\
= \bra{A_0}\left( e^{i\phi'_0Z}\prod_{k=1}^dW(a)e^{i\phi'_k Z}\right)U\ket{B_0}\\
=\text{Poly}(a)\cdot a = \text{Poly}(a)
```


where  $`\phi'_k`$  is a linear combination of  $`\phi_k`$ . So far, I've had difficulty discovering what the exact relationship between  $`\phi'_k`$  and  $`\phi_k`$  is. Grover's original formulation for the search problem has,  $`U = H^{\otimes n}`$ ,  $`\ket{B_0} = \ket{0}^{\otimes n}`$ ,  $`\ket{A_0} = \ket{s}`$  is the marked state and  $`\phi_k = \pi`$  for all  $`k`$ .



## Quantum Eigenvalue Transform
In both the [original paper](https://arxiv.org/abs/1806.01838) and this one, direct sums are used in the proof for lifting the QSP. While this probably lead to a cleaner and more easily understood proof, I personally found it confusing because I don't have a strong understanding of the direct sum formalism. The following is a regular sum rendition of the proofs offered. I've also written some notes on the direct sum formalism [here](DirectSum.md).

We consider a block encoding of a Hamiltonian  $`H : W \rightarrow W`$  given by 


```math
U=
\begin{pmatrix}
H & \sqrt{I-H^2}\\
\sqrt{I-H^2} & -H
\end{pmatrix}
```

where we note the following.  $`U : V \rightarrow V`$  is unitary and  $`\mathbb{C}^2 \otimes W = W`$ . We've assumed  $`||H|| \le 1`$  so  $`H`$  can be encoded into a unitary. If not then we would have to appropriately rescale  $`H`$ . We've also selected a particular kind of block encoding since we've specified the elements of the second row and column. It can be shown that more general block encodings will resemble the above in the correct basis. Finally, the above matrix is represented in the computational basis so  $`\bra{0}U\ket{0}`$  indexes  $`H`$ ,  $`\bra{1}U\ket{0}`$  indexes  $`\sqrt{I-H^2}`$  and so on.

```math
\bra{0}\bra{\psi}U\ket{0}\ket{\psi} = \bra{\psi}H\ket{\psi} 
```


Now since  $`H`$  is Hermitian, it can be given a eigenvalue decomposition


```math
H = \sum_\lambda \lambda \ket{\lambda}\bra{\lambda}
```


where the basis set  $`\bm{B} = \{\ket{0}\ket{\lambda}, \ket{1}\ket{\lambda}\}_\lambda`$  spans  $`V`$ . The action of  $`U`$  on each of these basis vectors is


```math
\begin{align}
U\ket{0}\ket{\lambda} = \lambda\ket{0}\ket{\lambda} + \sqrt{1-\lambda ^2}\ket{1}\ket{\lambda}\\
U\ket{1}\ket{\lambda} = \sqrt{1-\lambda^2}\ket{0}\ket{\lambda} - \lambda\ket{1}\ket{\lambda}
\end{align}
```

Thus the action of  $`U`$  on  $`V`$  is governed by


```math
\sum_\lambda \begin{pmatrix}
\lambda & \sqrt{1-\lambda^2}\\
\sqrt{1-\lambda^2} & -\lambda
\end{pmatrix}
\otimes
\ket{\lambda}\bra{\lambda}\\
= \sum_\lambda R(\lambda)\otimes \ket{\lambda}\bra{\lambda}
```


The signal processing rotation can be imparted through exponentiating the projector  $`\Pi = \ket{0}\bra{0}\otimes I = \ket{0}\bra{0}\otimes\sum_\lambda \ket{\lambda}\bra{\lambda} `$  as follows.


```math
\exp(i\phi(2\Pi - I)) = \exp \left( i\phi \left(2\ket{0}\bra{0}\otimes\sum_\lambda \ket{\lambda}\bra{\lambda} - (\ket{0}\bra{0}+\ket{1}\bra{1})\otimes\sum_\lambda \ket{\lambda}\bra{\lambda}\right)\right)\\
= \exp\left(i\phi(\ket{0}\bra{0}-\ket{1}\bra{1})\otimes \sum_\lambda \ket{\lambda}\bra{\lambda}\right)\\
=\left(e^{i\phi}\ket{0}\bra{0} + e^{-i\phi}\ket{1}\bra{1}\right)\otimes\sum_\lambda \ket{\lambda}\bra{\lambda}\\
=  e^{i\phi Z}\otimes \sum_\lambda \ket{\lambda}\bra{\lambda}
```


where the last equality comes from the fact that each subspace  $`\mathbb{C}^2\otimes V_\lambda`$  is invariant to the transformation. Similar to the amplitude amplification derivation in the previous section, its easy to see the following for even  $`d`$ 


```math
U_{\vec{\phi}} = \prod_{k=1}^{d/2}\exp(i\phi_{2k-1}(2\Pi - I))U^\dag\exp(i\phi_{2k}(2\Pi - I)) U\\
=\prod_{k=1}^{d/2}\sum_{\lambda, \lambda', \lambda'', \lambda'''} e^{i\phi_{2k-1}Z}R(\lambda')e^{i\phi_{2k}Z}R(\lambda''')\otimes\ket{\lambda}\braket{\lambda | \lambda'}\braket{\lambda'|\lambda''}\braket{\lambda''|\lambda'''}\bra{\lambda'''}\\
=\prod_{k=1}^{d/2}\sum_\lambda e^{i\phi_{2k-1}Z}R(\lambda)e^{i\phi_{2k}Z}R(\lambda)\otimes\ket{\lambda}\bra{\lambda}\\
=\sum_\lambda \left[\prod_{k=1}^{d/2} e^{i\phi_{2k-1}Z}R(\lambda)e^{i\phi_{2k}Z}R(\lambda)\right]\otimes \ket{\lambda}\bra{\lambda} \text{ *}\\
=\sum_\lambda 
\begin{pmatrix}
\text{Poly}(\lambda) & \cdot &\\
\cdot & \cdot &
\end{pmatrix}
\otimes \ket{\lambda}\bra{\lambda}\\
= \begin{pmatrix}
\sum_\lambda\text{Poly}(\lambda)\ket{\lambda}\bra{\lambda} & \cdot &\\
\cdot & \cdot &
\end{pmatrix}\\
=\begin{pmatrix}
\text{Poly}(H) & \cdot &\\
\cdot & \cdot &
\end{pmatrix}
```

and similarly for odd  $`d`$ . \
*Used the fact that 

```math
(A_{1,\lambda}\otimes\ket{\lambda}\bra{\lambda} + A_{1,\lambda'}\otimes\ket{\lambda'}\bra{\lambda'})(A_{2,\lambda}\otimes\ket{\lambda}\bra{\lambda} + A_{2,\lambda'}\otimes\ket{\lambda'}\bra{\lambda'}) = A_{1,\lambda}A_{2,\lambda}\otimes\ket{\lambda}\bra{\lambda} + A_{1,\lambda'}A_{2,\lambda'}\otimes\ket{\lambda'}\bra{\lambda'}
```

and therefore 

```math
\prod_{k}\sum_\lambda A_{k, \lambda}\otimes\ket{\lambda}\bra{\lambda} = \sum_\lambda \prod_{k} A_{k, \lambda}\otimes \ket{\lambda}\bra{\lambda}
```


## Quantum Singular Value Transform
Now consider an operator  $`T`$  whose singular value decomposition is  $`T = \sum_k \sigma_k \ket{w_k}\bra{v_k}`$  where  $`\sigma_k \ge 0`$  and the set  $`\ket{w_k}`$  and  $`\ket{v_k}`$  span the Hilbert spaces  $`W`$  and  $`V`$  respectively. As before, we'll restrict ourselves to considering the following block encoding in the computational basis:


```math
U = 
\begin{pmatrix}
T & \sqrt{I-T^2}\\
\sqrt{I-T^2} & -T
\end{pmatrix}
```


where  $`T = \bra{0}U\ket{0}`$ . The vector space that that  $`U`$  acts on must be spanned by both  $`\bm{B}_V = \{\ket{0}\ket{v_k}, \ket{1}\ket{v_k}\}_k`$  and  $`\bm{B}_W = \{\ket{0}\ket{w_k}, \ket{1}\ket{w_k}\}_k`$ . Moreover, we see the action of  $`U`$  on each vector in  $`\bm{B}_V`$  is


```math
U\ket{0}\ket{v_k} = \sigma_k\ket{0}\ket{w_k}+\sqrt{1-\sigma_k^2}\ket{1}\ket{w_k}\\
U\ket{1}\ket{v_k} = -\sigma_k\ket{1}\ket{w_k} + \sqrt{1-\sigma_k^2}\ket{0}\ket{w_k}
```


The action of  $`U`$  on the vector it acts on is governed by

```math
\sum_k
\begin{pmatrix}
\sigma_k & \sqrt{1-\sigma_k ^2}\\
\sqrt{1-\sigma_k^2} & -\sigma_k
\end{pmatrix}
\otimes \ket{w_k}\bra{v_k}\\
=\sum_k R(\sigma_k)\otimes \ket{w_k}\bra{v_k}
```


We'll now introduce two  $`z`$  rotation operators  $`e^{i\phi (2\Pi-I)}`$  and  $`e^{i\phi (2\tilde{\Pi}-I)}`$ , where  $`\Pi = \ket{0}\bra{0}\otimes \sum_k \ket{v_k}\bra{v_k}`$  and  $`\tilde{\Pi} = \ket{0}\bra{0}\otimes \sum_k\ket{w_k}\bra{w_k}`$ , and we'll consider the product of operations for even  $`d`$ 


```math
U_\phi=\prod_{j=1}^{d/2}e^{i\phi_{2j-1}(2\Pi-I)}U^\dag e^{i\phi_{2j}(2\tilde{\Pi}-I)}U\\
=\prod_{j=1}^{d/2}\sum_{k,k',k'',k'''} e^{i\phi_{2j-1}Z}R(\sigma_{k'})e^{i\phi_{2j}Z}R(\sigma_{k'''})\otimes\ket{v_k}\braket{v_k|v_{k'}}\braket{w_{k'}|w_{k''}}\braket{w_{k''}|w_{k'''}}\bra{v_{k'''}} \text{ *}\\
=\prod_{j=1}^{d/2}\sum_k e^{i\phi_{2j-1}Z}R(\sigma_{k})e^{i\phi_{2j}Z}R(\sigma_{k})\otimes \ket{v_k}\bra{v_k}\\
=\sum_k \left[\prod_{j=1}^{d/2}e^{i\phi_{2j-1}Z}R(\sigma_{k})e^{i\phi_{2j}Z}R(\sigma_{k})\right]\otimes \ket{v_k}\bra{v_k}\\
=
\sum_k
\begin{pmatrix}
\text{Poly}(\sigma_k) & \cdot &\\
\cdot & \cdot &
\end{pmatrix}
\otimes \ket{v_k}\bra{v_k}\\
=
\begin{pmatrix}
\text{Poly}(T) & \cdot &\\
\cdot & \cdot &
\end{pmatrix}
```

Since the input and output basis of  $`U_\phi`$  is  $`\bm{B}_V`$ , it follows that  $`\text{Poly}(T) = \Pi U_\phi \Pi`$ . In the case where  $`d`$  is odd:

```math
U_\phi =  e^{i\phi_1 (2\tilde{\Pi}-I)}U\prod_{j=1}^{(d-1)/2}e^{i\phi_{2j}(2\Pi-I)}U^\dag e^{i\phi_{2j+1}(2\tilde{\Pi}-I)}U\\
=\left(\sum_{k'} e^{i\phi_1 Z}R(\sigma_{k'})\otimes \ket{w_{k'}}\bra{v_{k'}}\right) \sum_{k}\left[\prod_{j=1}^{(d-1)/2} e^{i\phi_{2j}Z}R(\sigma_{k})e^{i\phi_{2j+1}Z}R(\sigma_{k})\right]\otimes \ket{v_k}\bra{v_k}\\
=\sum_k\left[e^{i\phi_1 Z}R(\sigma_k)\prod_{j=1}^{(d-1)/2} e^{i\phi_{2j}Z}R(\sigma_{k})e^{i\phi_{2j+1}Z}R(\sigma_{k})\right]\otimes \ket{w_k}\bra{v_k}\\
=\sum_k
\begin{pmatrix}
\text{Poly}(\sigma_k) & \cdot & \\
\cdot & \cdot &
\end{pmatrix}
\otimes \ket{w_k}\bra{v_k}\\
=
\begin{pmatrix}
\text{Poly}(T) & \cdot & \\
\cdot & \cdot &
\end{pmatrix}
```

Now, since the input and output basis of  $`U_\phi`$  are  $`\bm{B}_V`$  and  $`\bm{B}_W`$  respectively,  $`\text{Poly}(T) = \tilde{\Pi}U_\phi \Pi`$ 