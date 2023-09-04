---
publish: true
review-frequency: normal
---
Last Updated: 2022-10-18
Type:: #documentation 
Tags:: [[STM32]], [[build system]]

# How to build STM32IDE project from cmdline

```
$ /Applications/STM32CubeIDE.app/Contents/MacOS/STM32CubeIDE 
--launcher.suppressErrors 
-nosplash 
-application org.eclipse.cdt.managedbuilder.core.headlessbuild 
-data "$(pwd)/STM32CubeIDE/workspace_1.10.1/" 
-import "$(pwd)/STM32IDE_Project"
-build STM32IDE_Project
```

PS: Path argument is best using absolute path.

```
Usage: /Applications/STM32CubeIDE.app/Contents/MacOS/STM32CubeIDE -data <workspace> -application org.eclipse.cdt.managedbuilder.core.headlessbuild [ OPTIONS ]

   -data       {/path/to/workspace}
   -remove     {[uri:/]/path/to/project}
   -removeAll  {[uri:/]/path/to/projectTreeURI} Remove all projects under URI
   -import     {[uri:/]/path/to/project}
   -importAll  {[uri:/]/path/to/projectTreeURI} Import all projects under URI
   -build      {project_name_reg_ex{/config_reg_ex} | all}
   -cleanBuild {project_name_reg_ex{/config_reg_ex} | all}
   -markerType Marker types to fail build on {all | cdt | marker_id}
   -no-indexer Disable indexer
   -verbose    Verbose progress monitor updates
   -printErrorMarkers Print all error markers
   -I          {include_path} additional include_path to add to tools
   -include    {include_file} additional include_file to pass to tools
   -D          {prepoc_define} addition preprocessor defines to pass to the tools
   -E          {var=value} replace/add value to environment variable when running all tools
   -Ea         {var=value} append value to environment variable when running all tools
   -Ep         {var=value} prepend value to environment variable when running all tools
   -Er         {var} remove/unset the given environment variable
   -T          {toolid} {optionid=value} replace a tool option value in each configuration built
   -Ta         {toolid} {optionid=value} append to a tool option value in each configuration built
   -Tp         {toolid} {optionid=value} prepend to a tool option value in each configuration built
   -Tr         {toolid} {optionid=value} remove a tool option value in each configuration built
               Tool option values are parsed as a string, comma separated list of strings or a boolean based on the options type
```

---
# References
- [STM Forum](https://community.st.com/s/question/0D53W00001RL4l0SAD/how-do-i-build-my-stm32cubeide-code-via-the-command-line-on-linux) 
- [SO Example](https://stackoverflow.com/questions/68928393/stm32cubeide-headless-build-returns-no-project-matched-error)