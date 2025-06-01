# Singular Value Decomposition

### Theorem 1

Every linear operator has a singular value decomposition.

```math
A = U \Sigma V^\dagger
```
Where  $`U`$  and  $`V`$  are unitary and  $`\Sigma`$  is a semi-positive diagonal matrix, meaning its diagonal is populated with values  $`\sigma_i \in \mathbb{R}`$  where  $`\sigma_i \ge 0`$ . [This blog post](https://gregorygundersen.com/blog/2018/12/10/svd/) gives a geometric interpretation of the SVD, suggesting that, since unitaries correspond to rotations and diagonals correspond to stretching, compressing or reflecting along a particular axis (i.e. if  $`\sigma_1 = 1.5`$  then axis one is stretched to 1.5 times its original length) then SVD tells us that any linear transformation inlcuding shearing is composed of a rotation followed by stretching, compressing or reflecting followed by another rotation.

**Proof.** The same author offers a nice proof of SVD in [another blog post](https://gregorygundersen.com/blog/2018/12/20/svd-proof/#4-textbfu_i-is-a-unit-eigenvector-of-aatop) which takes a different approach to the one provided in Nielsen and Chuang but with the added benefit that it is applicable to any rectangular matrix.

### Theorem 2
Let  $`A`$  be a linear map between vector spaces of dimension  $`n`$  to  $`m`$  (i.e. a  $`m\times n`$  matrix). Its SVD can be written  $`A = \sum_i^d \sigma_i \ket{u_i}\bra{v_i}`$  where  $`d=\min(n,m)`$  and  $`\ket{u_i}`$  and  $`\ket{v_i}`$  are the eigenvectors of  $`U`$  and  $`V`$  respectively. 

**Proof.** From the proof of theorem 1, we know that the singular values of  $`A`$  are given by the square root of the eigenvalues of  $`A^\dagger A`$  whose dimension is  $`n\times n`$ , thus the dimensions of  $`\Sigma`$  must be  $`n\times n`$ ,  $`V`$  must be  $`n\times n`$  and  $`U`$  must be 
```math
U = 
\begin{bmatrix}
[u_1] & [u_2] &... & [u_n]
\end{bmatrix}\\
V = \begin{bmatrix}
[v_1] & [v_2] &... & [v_n]
\end{bmatrix}
```
### Theorem 3

For the singular value decomposition of a projected unitary,  $`P_1 U P_2 = \sum_i^d \sigma_i \ket{u_i} \bra{v_i}`$ , the singular vectors  $`\ket{u_i}`$  and  $`\ket{v_i}`$  can be extended (if needed) to span the sub spaces projected to by  $`P_1`$  and  $`P_2`$  respectively.

**Proof.** 

### Theorem 4

The singular values of a projected unitary are in the range  $`[0, 1]`$ 

### Theorem 5 

The number of non-zero singular values of an operator is equal to its rank.

**Proof.** From [stack exchange](https://math.stackexchange.com/questions/3967922/singular-values-and-matrix-rank). First observe that  $`\text{rank}(AB) \le \text{rank}(A)`$ . This is because the rank of an operator is the dimensions of its image and  $`\text{img}(AB)`$  is a sub-space of  $`\text{img}(A)`$  (clearly from the fact that the operator  $`A`$  gets applied last in both cases). Thus for the decomposition  $`A = U\Sigma V^\dagger`$ ,  $`\text{rank}(A) = \text{rank}(U\Sigma V^\dagger) \le \text{rank}(U\Sigma) = \text{rank}(U\Sigma V^\dagger V) \le \text{rank}(U\Sigma V^\dagger)`$  and therefore  $`\text{rank}(A) = \text{rank}(U\Sigma)`$ .

Furthermore, the row rank and column rank of a matrix are equal which suggests that  $`\text{rank}(A) = \text{rank}(A^\dagger)`$ . We can therefore apply a similar sequence of steps to show that  $`\text{rank}(A) = \text{rank}(\Sigma^\dagger U^\dagger) = \text{rank}(\Sigma)`$ . Since  $`\Sigma`$  is diagonal, its rank equals the number of non-zero values it contains, i.e. the number of non zero singular values.

