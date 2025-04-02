# Notes on 'A case study against QSVT: assessment of quantum phase estimation improved by signal processing techniques'

As a recap: the quantum phase estimation problem is one where, given unitary  $`U`$  and its eigenvector  $`\ket{\psi}`$  with corresponding eigenvalue  $`e^{i2\pi \theta}`$ , estimate  $`\theta`$  to accuracy  $`\epsilon`$  with high probability. A core deterrant to this success probability, highlighted by the authors of the titled paper, is the bit discretisation error arising from the fact that a finite  $`m`$  number of qubits are used to represent  $`\theta`$ , which may require more bits to be represented or be irrational.

The paper introduces two algorithmic approaches for dealing with bit discretisation error: QSVT and window methods, with the objective of empirically evaluating their performance on toy QPE problems and, consequeuntly, make inferences about their quality when used in practice. I find that this paper presents strong evidence to suggest that QSVT significantly underperforms windowed methods and therefore does not serve a practical purpose for minimising bit discretisation error in QPE.

The paper provides a conceptual overview of the two algorithmic approaches in its main body and directs interested readers to its appendix for a more technical understanding. I was not one such interested reader.

### QSVT for QPE
The intended use of QSVT for the bit discretisation problem is to polynomially transform  $`U`$  (i.e. its eigenvalues) such that the corresponding phase is clipped to exactly  $`m`$  bits. The target transformation is given by 


```math
f(x) = \Theta\left(\frac{1}{\sqrt{2}}-x\right)
```


where  $`\Theta`$  is the sign function. Its not clear to me why this function works as intended. Since the function is not continuous, it is decomposed into a series of polynomial which I won't write down in these notes. This decomposition has two free papameters that control the quality of the approximation. The phase angles implementing this polynomial by QSP can then be found using classical methods and QSVT is implemented.

### Window methods
Traditionally, the QPE algorithm features Hadamard gates to prepare the initial superposition which is then used for phase kickback through controlled applications of  $`U`$ . We can replace this block of Hadamards with a window function, whose purpose is to reduce spectral leakage which is introduced when truncating a series in the time domain and in turn minimise bit discretisation error. To do so they require any number of auxiliary qubits - the higher the better the success probability. Honestly, not entirely clear on what a lot of this means.

In this paper, the two window methods used are the Cosine and Kaiser methods. 

## Results

The paper uses simulations of the above approaches for the simple phase gate 

```math
U = 
\begin{pmatrix}
1 & 0 \\
0 & e^{i2\pi \phi}
\end{pmatrix}
```

whose eigenvector,  $`\ket{1}`$ , can clearly be exactly implemented. Thus by allowing a sufficient number of bits  $`m`$  to achieve a desired accuracy  $`\epsilon`$ , the authors of the paper define the success probability of a QPE method to be the probability of measuring the two bins closest to the actual phase and measure the sucess probability of each method over the full range of possible phases  $`[0, 1]`$ . Taking the minimum of these they ask: how many resources (in terms of applications of  $`U`$ ) are used for the minimum success probability of an approach to be greater than 99%.

The paper finds that, to achieve a success probability of  $`10^{-2.28}`$  QSVT requires 1984 calls to  $`U`$ , to achieve  $`10^{-5.07}`$  the cosine window method uses 1023 calls to  $`U`$  and to achieve  $`10^{-7.28}`$  the Kaiser window method uses 127 calls to  $`U`$ . The difference in the number of unitary calls used by the two window methods is owed to the Kaiser method only requiring 4 auxiliary qubits as opposed to the 5 used by the cosine window. The authors suggest that QSVT's poor performance is related to the number of unitary calls required to implement the sign function, which was approximated by a 64 degree polynomial. To match the resource usage of the window method, QSVT would instead be restricted to a 16 degree polynomial, in which case the success probability would degrade further from the  $`10^{-7}`$  benchmark set by the Kaiser window. Thus, the authors contend that no amount of tweaking the parameters of the polynomial used in QSVT can make up for this difference and the QSVT implementation of QPE lacks practicality. 

The authors also consider the effect of increase the lower bound success probability form 99% for the two window methods and increasing the number of bits of precision required  $`m`$  for all approaches. In all, it finds the Kaiser window method to be the strongest deterrent of bit discretisation error among the three approaches.

As future work, the authors motivate further empirical analysis on the applications of QSVT. In my opinion, it stands to question whether QSVT has any practical application or if it is entirely a theoretical intrigue. A key question that crosses my mind is: how does QSVT empically compare to traditional quantum walk algorithms? It has been shown that QSVT generalises the quantum walk, but applied to specific quantum walk applications does it underperform?
