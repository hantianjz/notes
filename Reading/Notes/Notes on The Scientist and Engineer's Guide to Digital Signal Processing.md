---
publish: true
review-frequency: normal
reviewed: 2022-12-29
link:
- '[[DSP]]'
- '[[Algorithm]]'
- '[[math]]'
- '[[Reading/reading]]'
- '[[programming]]'
tags:
- notes
---
2022-04-30-Sa

# Notes on The Scientist and Engineer's Guide to Digital Signal Processing

# Mean and Standard Deviation
**Eq 2-1**: Mean value
$$
\mu = \frac{1}{N} \sum_{i=0}^{N-1} x_i
$$
**Eq 2-2**: Standard Deviation
$$
\sigma^2 = \frac{1}{N} \sum_{i=0}^{N-1} (x_i - \mu)^2
$$
$\mu$ from Eq. 2-1
$\sigma$ is the standard deviation.
$\sigma^2=$  variance or RMS (Root-Mean-Square)

**Eq 2-3**: Running statistics
$$
\sigma=\frac{1}{N-1} [ \sum_{i=0}^{N-1} x_i^2 - \frac{1}{N}(\sum_{i=0}^{N-1} x_i)^2 ]
$$

$$
\sigma=\frac{1}{N-1} [ Sum of square - \frac{sum^2}{N} ]
$$
- Greater computational efficiency

**3 Variable to track:**
- N
- Sum
- Sum of Squares

Standard deviation represents noise and interference. When compared to the mean, it give **signal-to-noise ratio (SNR)**. Mean divided by standard deviation.

**Coefficient of variation (CV)** Standard deviation divided by **mean**, multiplied by 100%. 

# Signal vs. Underlaying Process
The *probabilities* of underlying process are constant.
The *statistics* of the acquired signal change each time the experiment is repeated. **Statistical noise**.

The typical error between the mean of *N* points, and the mean of the underlaying process is:
**Eq 2-4**: 
Typical error $= \frac{\sigma}{N^\frac{1}{2}}$
Strong law of large numbers
Errors become zero a *N* approach $\infty$

