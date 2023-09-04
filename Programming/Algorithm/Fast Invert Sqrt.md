---
publish: true
review-frequency: low
reviewed: 2023-04-09
---
2021-12-29-We
Type:: #notes
Tags:: [[C]], [[math]], [[Notes todo]]

# Fast Invert Sqrt

```c
#include <stdio.h>

float FastInvSqrt(float x) {
  float xhalf = 0.5f * x;
  int i = *(int*)&x;         // evil floating point bit level hacking
  i = 0x5f3759df - (i >> 1);  // what the fuck?
  x = *(float*)&i;
  x = x*(1.5f-(xhalf*x*x));
  return x;
}

int main(int argc, char* argv[]) {
    (void)argc;
    (void)argv;

    float in_val = 9.0;

    float out_val = FastInvSqrt(9.0);
    printf("invert sqrt of %f\n", out_val);
    return 0;
}
```
---
# References
- http://h14s.p5r.org/2012/09/0x5f3759df.html