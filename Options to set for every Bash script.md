Last Updated: 2022-01-22
Type: #documentation 
Tags: [[bash]], [[flags]]

# Options to set for every Bash script
```bash
#!/bin/bash
set -x # Print every executed command
set -u # Fail on expanding undefined variable
set -e # Fail on command fail
set -o pipefail # Early fail for piped commands
```