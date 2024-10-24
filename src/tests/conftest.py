import sys
from pathlib import Path

# Add the parent directory to sys.path to configure imports from one folder above
sys.path.append(str(Path(__file__).resolve().parent.parent))
