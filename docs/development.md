# sz-sdk-errors development

The following instructions are used when modifying and generating source code.

## Prerequisites for development

:thinking: The following tasks need to be complete before proceeding.
These are "one-time tasks" which may already have been completed.

1. The following software programs need to be installed:
    1. [git](https://github.com/senzing-garage/knowledge-base/blob/main/WHATIS/git.md)
    1. [make](https://github.com/senzing-garage/knowledge-base/blob/main/WHATIS/make.md)

## Clone repository

For more information on environment variables,
see [Environment Variables](https://github.com/senzing-garage/knowledge-base/blob/main/lists/environment-variables.md).

1. Set these environment variable values:

    ```console
    export GIT_ACCOUNT=senzing-garage
    export GIT_REPOSITORY=sz-sdk-errors
    export GIT_ACCOUNT_DIR=~/${GIT_ACCOUNT}.git
    export GIT_REPOSITORY_DIR="${GIT_ACCOUNT_DIR}/${GIT_REPOSITORY}"
    ```

1. Using the environment variables values just set, follow steps in [clone-repository](https://github.com/senzing-garage/knowledge-base/blob/main/HOWTO/clone-repository.md) to install the Git repository.

## Update master list of Senzing engine errors

1. Make modifications to
   [szerrors.json](../szerrors.json)

## Generate source code

1. Generate source code.

    ```console
    make build
    ````

   This will create new files in the `go`, `java`, and `python` directories.
