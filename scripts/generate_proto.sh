#!/bin/bash
set -eo pipefail

# This script generates Python packages from protobuf files found in opi-api.

# Modules from opi-api to include
PROTO_INCLUDE=(common security)

# Ref of opi-api to use. This can be a commit, tag, branch
API_REPO_REF="main"

# You can provide an existing opi-api repo to use, otherwise a fresh clone will
# be created
API_REPO_DIR=${API_REPO_DIR:-"/tmp/opi-api"}


git_toplevel="$(git rev-parse --show-toplevel)"

# Clone opi-api if it does not yet exist
if [[ ! -d "$API_REPO_DIR" ]]; then
    git clone https://github.com/opiproject/opi-api.git "$API_REPO_DIR"
fi

pushd "$API_REPO_DIR" || exit 1
git fetch --all
git checkout "$API_REPO_REF"
git pull --ff-only || true  # Pull in case we are reusing the repo path
popd || exit 2

cd "$git_toplevel/pydpu/proto"

include_dirs=()
for lib in "${PROTO_INCLUDE[@]}"; do include_dirs+=(-I "${API_REPO_DIR}/${lib}"); done

readarray -t lib_proto < <(find "${PROTO_INCLUDE[@]/#/${API_REPO_DIR}/}" -iname "*.proto")
poetry run python -m grpc_tools.protoc \
    "${include_dirs[@]}" \
    --python_out=. --mypy_out=. "${lib_proto[@]}"

readarray -t svc_proto < <(grep -REl "service \w+ {" "${PROTO_INCLUDE[@]/#/${API_REPO_DIR}/}")
poetry run python -m grpc_tools.protoc \
    "${include_dirs[@]}" \
    --grpc_python_out=. \
    --python_out=. --mypy_out=. "${svc_proto[@]}"

