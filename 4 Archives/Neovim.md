---
publish: false
reviewed: 
review-frequency: ignore
tags:
  - documentation
link:
  - "[[vim]]"
  - "[[learning]]"
---

# Lua
### [`runtime/doc/lua-guide.txt`](https://github.com/neovim/neovim/blob/28f54a78782318cb9c356a372b9e52a3a6b1f8dd/runtime/doc/lua-guide.txt#L4)
- Each `lua` command have it's own context, local variables are not accessible outside it
- `lua-heredoc` block allow lua code to be embedded in vimscript
```vimscript
lua << EOF
...
EOF
```

Variables can be set and read using the following wrappers, which directly
correspond to their |variable-scope|:

• |vim.g|:   global variables (|g:|)
• |vim.b|:   variables for the current buffer (|b:|)
• |vim.w|:   variables for the current window (|w:|)
• |vim.t|:   variables for the current tabpage (|t:|)
• |vim.v|:   predefined Vim variables (|v:|)
• |vim.env|: environment variables defined in the editor session

## runtimepath

## autocommand
An |autocommand| is a Vim command or a Lua function that is automatically
executed whenever one or more |events| are triggered, e.g., when a file is
read or written, or when a window is created. These are accessible from Lua
through the Nvim API.

# Pluggin
```
example-plugin/ 
    plugin/
        example-plugin.vim # Run on startup
    lua/ # Included in lua search scope
        example-plugin/
            init.lua
            util.lua
        example-plugin.lua
```

```
require("example-pluging") # Call into both type of lua file
require("example-pluging.util.lua") # Import 
```

```
package.loaded     # Table of module/package currently loaded
P(package.loaded)  # Print the package loaded table
```

### Typical module pattern
```
local M = {}

M.setup = function(opt)
    print("options: ", opt)
end

return M
```

# Misc
- client(s) control the Neovim `nvim` process via a msgpack-rpc API

---
# References
- Plugin video: https://www.youtube.com/watch?v=n4Lp4cV8YR0
- Lua Guide: https://neovim.io/doc/user/lua-guide.html#lua-guide