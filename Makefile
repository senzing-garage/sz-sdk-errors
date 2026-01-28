# Makefile for Python project

# Detect the operating system and architecture.

include makefiles/osdetect.mk

# -----------------------------------------------------------------------------
# Variables
# -----------------------------------------------------------------------------

GIT_REPOSITORY_NAME := $(shell basename `git rev-parse --show-toplevel`)
GIT_VERSION := $(shell git describe --always --tags --long --dirty | sed -e 's/\-0//' -e 's/\-g.......//')

# -----------------------------------------------------------------------------
# The first "make" target runs as default.
# -----------------------------------------------------------------------------

.PHONY: default
default: help

# -----------------------------------------------------------------------------
# Operating System / Architecture targets
# -----------------------------------------------------------------------------

-include makefiles/$(OSTYPE).mk
-include makefiles/$(OSTYPE)_$(OSARCH).mk


.PHONY: hello-world
hello-world: hello-world-osarch-specific

# -----------------------------------------------------------------------------
# Dependency management
# -----------------------------------------------------------------------------

.PHONY: venv
venv: venv-osarch-specific


.PHONY: dependencies-for-development
dependencies-for-development: venv
	$(activate-venv); \
		python3 -m pip install --upgrade pip; \
		python3 -m pip install --group all .


.PHONY: dependencies
dependencies: venv
	$(activate-venv); \
		python3 -m pip install --upgrade pip; \
		python3 -m pip install -e .


.PHONY: install-prettier
install-prettier:
	@command -v npx >/dev/null 2>&1 || { echo "npm is required but not installed. Aborting." >&2; exit 1; }
	@npx prettier --version >/dev/null 2>&1 || npm install --save-dev --save-exact prettier

# -----------------------------------------------------------------------------
# Setup
# -----------------------------------------------------------------------------

.PHONY: setup
setup: setup-osarch-specific

# -----------------------------------------------------------------------------
# Lint
# -----------------------------------------------------------------------------

.PHONY: lint
lint: pylint

# -----------------------------------------------------------------------------
# Build
# -----------------------------------------------------------------------------

.PHONY: build-csharp
build-csharp:
	./bin/generate_csharp.py


.PHONY: build-go
build-go:
	./bin/generate_go.py
	gofmt -w go/szerrortypes.go


.PHONY: build-java
build-java:
	./bin/generate_java.py


.PHONY: build-python
build-python:
	./bin/generate_python.py


.PHONY: build
build: build-csharp build-go build-java build-python

# -----------------------------------------------------------------------------
# Clean
# -----------------------------------------------------------------------------

.PHONY: clean
clean: clean-osarch-specific

.PHONY: restore
restore:
	@git restore \
		csharp/SzExceptionMapper.cs \
		go/szerrortypes.go \
		java/SzExceptionMapper.java \
		python/szerror.py


# -----------------------------------------------------------------------------
# Utility targets
# -----------------------------------------------------------------------------

.PHONY: help
help:
	$(info Build $(PROGRAM_NAME) version $(BUILD_VERSION)-$(BUILD_ITERATION))
	$(info Makefile targets:)
	@$(MAKE) -pRrq -f $(firstword $(MAKEFILE_LIST)) : 2>/dev/null | awk -v RS= -F: '/^# File/,/^# Finished Make data base/ {if ($$1 !~ "^[#.]") {print $$1}}' | sort | egrep -v -e '^[^[:alnum:]]' -e '^$@$$' | xargs


.PHONY: print-make-variables
print-make-variables:
	@$(foreach V,$(sort $(.VARIABLES)), \
		$(if $(filter-out environment% default automatic, \
		$(origin $V)),$(info $V=$($V) ($(value $V)))))

# -----------------------------------------------------------------------------
# Specific programs
# -----------------------------------------------------------------------------

.PHONY: pylint
pylint:
	$(info ${\n})
	$(info --- pylint ---------------------------------------------------------------------)
	@$(activate-venv); pylint $(shell git ls-files '*.py' ':!:docs/source/*')
