## Notes on Fixed Point Obvlious Amplitude Amplification

The statement of the amplitude amplification problem is as follows. We are given access to a state preparation unitary  $`A`$  such that  $`A\ket{0} = \ket{s}`$  and a state checking unitary  $`U`$  such that, for a target state  $`\ket{T}`$ ,  $`U\ket{v}\ket{0} = \ket{v}\ket{0 \oplus(v=T)}`$ . We are promised that  $`\ket{s}`$  has some overlap with  $`T`$ , specifically, 

```math
\braket{T|s} = \sqrt{\lambda}e^{i \omega}
```

for  $`\lambda > 0`$ . Given parameter  $`\delta`$ , the goal is to construct a circuit with complexity  $`L \in O(\log(1/\delta)/\sqrt{\lambda})`$ , denoted  $`S_L`$ , such that the probability of measuring  $`\ket{T}`$ , which we denote  $`P_L`$ , is given by 

```math
P_L = |\bra{T} S_L \ket{s}|^2 \ge 1-\delta^2.
```


A key issue in regular amplitude amplification is that  $`L' > L`$ , can lead to the souffle problem, where we overcook the state such that it reverts back to having low overlap with the target. To avoid this problem we either have to know  $`\delta`$  exactly or resort to trial and error techniques like expenonentially increasing the number of iterates. The promise of oblvious amplitude amplification is that there exists a circuit of (any cost)  $`L`$  such that


```math
P_L(\lambda) = 1-\delta^2 T_L(T_{1/L}(1/\delta)\sqrt{1-\lambda})^2
```

where  $`T_k`$  is the  $`k`$ -degree Chebyshev polynomial of the first kind satisfying  $`T_k(\cos(x)) = \cos(k x)`$ . We've now made explicit a dependence on  $`\lambda`$ . It turns out that if the above is achievable then we have that 
-  $`L \in O(\log(1/\delta)/\sqrt{\lambda})`$ ,  $`P_L(\lambda) \ge 1-\delta^2`$ , **and** 
- for  $`L'>L`$ ,  $`P_{L'}(\lambda) \ge 1-\delta^2`$ . 

We thus entirely avoid the souffle problem. The algorithm is oblvious because it doesn't need prior knowledge of  $`\delta`$ , rather, a lower bound suffices.

We first assume that we have access to such an  $`S_L`$ . We show that  $`P_L(\lambda)`$  satisfies the properties in the dot points. Note that the Chebyshev property ensures that so long as  $`|x| \le 1`$  then  $`|T_k(x)| \le 1`$ . Hence, as long  $`\sqrt{1-\lambda}|T_{1/L}(1/\delta)| \le 1`$  then  $`|T_L(T_{1/L}(1/\delta)\sqrt{1-\lambda})| \le 1`$  and therefore  $`P_L \ge 1-\delta^2`$ . Denoting  $`w = 1-T_{1/L}(1/\delta)^{-2}`$ , its clear that this happens if  $`\lambda \ge w`$ .

It turns out that for large  $`L`$  and small  $`\delta`$  we have that 

```math
w \approx \left(\frac{\log(2/\delta)}{L}\right)^2
```
 
and from the condition  $`\lambda \ge w`$  we have

```math
L \ge \frac{\log(2/\delta)}{\sqrt{\lambda}} \in O(\log(1/\delta)/\sqrt{\lambda})
```

completing the first claim. The second claim easily follows from the fact that as we continue to increase  $`L`$ ,  $`w`$  decreases and  $`\lambda \ge w`$  still holds. In fact the range of  $`\lambda`$ 's that are amplified by the circuit broadens to include smaller and smaller values. It is for this reason that the authors refer to  $`w`$  as the *width* of the algorithm, since it directly determines the range of viable  $`\lambda`$  values.


What remains is the harder problem of constructing  $`S_L`$ . First, for simplicity, define states 


```math
\ket{t} = e^{-i\omega}\ket{T}
```
 
and 

```math
\ket{t^\perp} = \frac{1}{\sqrt{1-\lambda}}(\ket{s} - \sqrt{\lambda}\ket{t})
```

So that we can write

```math
\ket{s} = 
\begin{pmatrix}
\sqrt{1-\lambda}\\
\sqrt{\lambda}
\end{pmatrix}
```

in the  $`\ket{t}, \ket{t^\perp}`$  basis. The goal will be to construct a generalised grover iterate which constructs the so-called Chebyshev state


```math
S_L\ket{s} = \ket{C_L} = \sqrt{1-P_L(\lambda)}\ket{t^\perp} + \sqrt{P_L(\lambda)}e^{i\chi}\ket{t}
```

for some relative phase  $`\chi`$ , up to a possible global phase.
To build a generalised Grover iterate we construct the following generalised reflections.


```math
S_s(\alpha) = I - (1-e^{-i\alpha})\ket{s}\bra{s}
```

and similarly,

```math
S_t(\beta) = I-(1-e^{-i \beta})\ket{t}\bra{t}.
```

Setting  $`\alpha = \pm \pi`$  and  $`\beta = \pm \pi`$  reduces  $`S_t`$  and  $`S_s`$  to the standard reflections seen in Grover's. Each reflection can be built in query complexity  $`O(1)`$  to the unitaries  $`A`$  and  $`U`$  and their adjoints respectively. \
![image](images/generalised_grovers.png)
The generalised Grover's iterate is thus


```math
G(\alpha, \beta) = S_s(\alpha)S_t(\beta)
```


and we have 


```math
S_L = \prod_{j=1}^L G(\alpha_j, \beta_j)
```
