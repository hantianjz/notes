---
publish: true
review-frequency: normal
---
2022-07-04-Mo
Author:: ?
Date published: 2021-01-17
Type:: #notes #documentation 
Tags:: [[bash]], [[shell]], [[scripting]]
Link: https://cuddly-octo-palm-tree.com/

# Bash safety settings

## TLDR
```bash
#!/bin/bash
set -x # Print every executed command
set -u # Fail on expanding undefined variable
set -e # Fail on command fail
set -o pipefail # Early fail for piped commands
```

```bash
#!/bin/bash
set -o errexit
set -o nounset
set -o pipefail
set -o errtrace
```

# Error Trap
```bash
trap 'echo BOO!' ERR  # Execute trap command on error
```

# Template
```bash
#!/usr/bin/env bash

set -o errexit
set -o nounset
set -o pipefail
if [[ "${TRACE-0}" == "1" ]]; then
    set -o xtrace
fi

if [[ "${1-}" =~ ^-*h(elp)?$ ]]; then
    echo 'Usage: ./script.sh arg-one arg-two

This is an awesome bash script to make your life better.

'
    exit
fi

cd "$(dirname "$0")"

main() {
    echo do awesome stuff
}

main "$@"
```

---
# Ref
- https://cuddly-octo-palm-tree.com/posts/2021-01-24-bash-set-dash-u/