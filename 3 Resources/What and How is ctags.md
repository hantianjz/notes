---
publish: true
review-frequency: normal
link:
- '[[code tagging]]'
tags:
- idea
---
2021-12-29-We

# ctags

Downside is only symbol defines information, lack symbol reference info.

- List of symbol definition/declaration
- Each line a single symbol define
- Fields on each line is tab separated

**Tag Entry format:**

`{tagname}<Tab>{tagfile}<Tab>{tagaddress}[;"<Tab>{tagfield}..]`

- `{tagname}` Any identifier, not containing white space..
- `<Tab>` Exactly one TAB character (although many versions of Vi can handle any amount of white space).
- `{tagfile}` The name of the file where `{tagname}` is defined, relative to
   		the current directory
- `{tagaddress}` Any Ex command.  When executed, it behaves like 'magic' was
		not set.  It may be restricted to a line number or a search
		pattern (Posix).

**Optionally:**
   - `;"` *semicolon + doublequote*: Ends the tagaddress in way that looks
		like the start of a comment to Vi.
  - `{tagfield}` See below.

A tagfield has a name, a colon, and a value: "name:value".
- The name consist only out of alphabetical characters.  Upper and lower case
  are allowed.  Lower case is recommended.  Case matters ("kind:" and "Kind:
  are different tagfields).
  
- The value may be empty.<BR>
  It cannot contain a `<Tab>`.<BR>
  When a value contains a `"\t"`, this stands for a `<Tab>`. <BR>
  When a value contains a `"\r"`, this stands for a `<CR>`. <BR>
  When a value contains a `"\n"`, this stands for a `<NL>`. <BR>
  When a value contains a `"\\"`, this stands for a single `'\'` character. <BR>
  Other use of the backslash character is reserved for future expansion. <BR>
  Warning: When a tagfield value holds an MS-DOS file name, the backslashes
  must be doubled!

**Tagfield names:**

| FIELD NAME | DESCRIPTION                                                        |
|:---------- |:------------------------------------------------------------------ |
| arity      | Number of arguments for a function tag.                            |
| class      | Name of the class for which this tag is a member or method.        |
| enum       | Name of the enumeration in which this tag is an enumerator.        |
| file       | Static (local) tag, with a scope of the specified file. <sup>1</sup>        |
| function   | Function in which this tag is defined. <sup>2</sup>                          |
| kind       | Kind of tag.  The value depends on the language. <sup>3</sup> |
| struct     | Name of the struct in which this tag is a member.                  |
| union      | Name of the union in which this tag is a member.                   |
	
<sup>1</sup> When the value is empty, `{tagfile}` is used.

<sup>2</sup> Useful for local variables (and functions).  When functions nest (e.g., in Pascal), the function names are concatenated, separated with '/', so it looks like a path.

**<sup>3</sup>Kind tags table**

| KIND SYMBOL | DESCRIPTION                         |
|:------ |:----------------------------------- |
| c         | class name                          |
| d      | define (from \#define XXX)           |
| e      | enumerator                          |
| f      | function or method name             |
| F      | file name                           |
| g      | enumeration name                    |
| m      | member (of structure or class data) |
| p      | function prototype                  |
| s      | structure name                      |
| t      | typedef                             |
| u      | union name                          |
| v      | variable                            |
*When this field is omitted, the kind of tag is undefined.*

---
# References
[SO Post understanding ctags format](https://stackoverflow.com/a/42074202)
Format Doc: http://ctags.sourceforge.net/FORMAT