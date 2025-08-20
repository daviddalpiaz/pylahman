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
    quartodoc build --config docs/_quarto.yml
    # quarto render docs
    quarto preview docs

# run standard tests
test:
    @echo "Running standard tests (docstring validation against data)..."
    uv run pytest tests/ -v

# run extended tests
test-all:
    @echo "Running all tests including README validation..."
    uv run pytest tests/ -m "" -v
