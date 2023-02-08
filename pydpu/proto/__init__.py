# Add proto dir to PYTHONPATH since protoc does not create relative imports
# See this for more info https://github.com/protocolbuffers/protobuf/issues/1491
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent))
