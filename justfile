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
