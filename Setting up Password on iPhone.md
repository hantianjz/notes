---
publish: true
review-frequency: normal
---
Last Updated: 2022-03-05
Type:: #documentation 
Tags:: [[iOS]], [[password-store]], [[gpg]]

# Setting up Password on iPhone
## Setting up SSH keys
- Standard ssh key gen in secure place
## Import Private/Public keys
- Refer to [[Open CryptLuks Master]] to get private keys

## Clone git repo
-   Git repository URL: `ssh://git@gitlab.com/passforios-demo/demo.git` (original is `git@gitlab.com:passforios-demo/demo.git`)
    -   remember to include username in the url
    -   remember to change ":" to "/"
-   Username: `git`
-   Supported authentication Method: SSH Keys, Password (only for self-built Git server, but note that GitHub, GitLab, etc. don't support password authentication.)
-   Remarks: Username should be specified _both_ in the "Git repository URL" field and in the "username" field

---
# Reference
- https://github.com/mssun/passforios/wiki#quick-start-guide-for-pass-for-ios