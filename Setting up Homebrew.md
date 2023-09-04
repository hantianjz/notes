---
publish: true
review-frequency: normal
---
Last Updated: 2022-03-05
Type:: #documentation 
Tags:: [[homebrew]], [[M1 Mac]], [[Apple]], [[Package Management]]

# Setting up Homebrew
Setting up homebrew on the recent M1 MacOS seem to land it in the `/opt/` folder. Where all the installed binary are not located in the `/usr/local/bin` anymore. Which is a none typical setup place.
I expect this is partly due to apple's SIP where the `/usr` folder is protected.

In any case running following seem to be enough to set the env variable
```
eval "$(/opt/homebrew/bin/brew)"
```
But this is also causing trouble for prezto, where it is unable to detect existence of brew, hence not correctly detecting the existence of brew command.