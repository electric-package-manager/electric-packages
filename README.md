<h1 align="center">Electric Packages</h1>

<p align="center">
<img src="https://img.shields.io/tokei/lines/github/electric-package-manager/electric-packages?style=plastic"> <img src="https://img.shields.io/github/repo-size/electric-package-manager/electric-packages?style=plastic">
</p>

The official electric package repository. All manifests that [electric](https://www.github.com/electric-package-manager/electric) can install are here.

--------------------------------

*Important*: If you would like to **suggest a package** that you want to add to electric, make sure you post it at this [issue](https://github.com/electric-package-manager/electric-packages/issues/1) 

If you want to **upload a package yourselves**, make sure you go to https://www.electric.sh/request-package

## Instructions

#### Commands:
Get a list of commands electric can execute by typing `electric` in your shell.
```ps1
> electric
Electric Package Manager v1.0.0 Beta Build
Copyright (c) Electric Inc.

Usage: electric <command> [<options>]

Commands:
  Software Management
    * install
    * uninstall
    * update
    * bundle
  Explore Packages
    * list
    * search
    * show
  Configuration Development And Management
    * new
    * config
    * generate
    * sign
  Customization And Cleanup
    * settings
    * cleanup
```

### Install A Package
```ps1
electric install <package-name>
```

### Uninstall A Package
```ps1
electric uninstall <package-name>
```

### Update A Package
```ps1
electric update <package-name>
```
