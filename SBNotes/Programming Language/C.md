# Asserts

```c
#include <assert.h>
#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>
#include <stdio.h>

/*
Define to disable assert at compile time.
#define NDEBUG
*/

int main(int argc, char* argv[]) {
  (void)argc;
  (void)argv;

  assert(false);
  return 0;
}
```