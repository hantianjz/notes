---
publish: false
reviewed: 
review-frequency: ignore
tags:
  - documentation
link:
  - "[[Algorithm]]"
  - "[[string]]"
---
# Hash of string for searching

The good and widely used way to define the hash of a string $S$ of length $n$ is

$$ 
hash(s) = \sum^{n-1}_{i=0} s[i] \cdot p^{i} \mod m
$$
Where $p$ and $m$ is some chosen positive number, this is called the **polynomial rolling hash function**.

$p$ should be a prime number close to the number of possible symbol in the alphabet of the hash string.
$m$ some large prime number to lower potential of hash collision.

## Fast hash calculation of substrings of string

By definition, we have:
$$
hash(s[i..j]) = \sum_{k=i}^{j} s[k] \cdot p^{k-i} \mod m
$$
Multiplying by $p^i$ gives:
$$
hash(s[i..j]) \cdot p^i = \sum_{k=i}^{j} s[k] \cdot p^k \mod m
$$
$$
= hash(s[0..j]) - hash(s[0..i-1]) \mod m
$$

# Hash of string for uniform distribution

---
# References
- https://cp-algorithms.com/string/string-hashing.html