process:
    @echo "Processing raw data..."
    uv run scripts/process.py

build-sdist:
    @echo "Building sdist..."
    uvx --from build pyproject-build --sdist --installer uv

build-wheel:
    @echo "Building wheel..."
    uvx --from build pyproject-build --wheel --installer uv

build: process build-sdist build-wheel

docs:
    uv run --group docs -- quartodoc build --config docs/_quarto.yml
    just docs-index-to-readme
    quarto preview docs

# run tests
test:
    uv run pytest tests/ -v

# compare data columns with README and R package
compare-tables:
    Rscript scripts/extract-r-columns.R
    uv run python scripts/compare-tables.py

docs-index-to-readme:
    cp docs/index.qmd README.qmd
    quarto render README.qmd -t gfm
    rm README.qmd

publish-new-version:
    #!/usr/bin/env zsh
    if ! git diff-index --quiet HEAD --; then
        echo "Error: You have uncommitted changes."
        exit 1
    fi
    if [ "$(git rev-parse HEAD)" != "$(git rev-parse @{u})" ]; then
        echo "Local branch is not in sync with remote."
        exit 1
    fi
    current_version=$(grep '^version = ' pyproject.toml | sed 's/version = "\(.*\)"/\1/')
    echo "Version from pyproject.toml: $current_version"
    echo "Creating git tag v$current_version..."
    git tag "v$current_version"
    git push origin "v$current_version"
    echo "Successfully created and pushed tag v$current_version"
