import json
import subprocess
from pathlib import Path

_CONFIG_PATH = Path(__file__).with_name("tool_config.json")


def _load_config() -> dict[str, str]:
    with _CONFIG_PATH.open("r", encoding="utf-8") as fp:
        return json.load(fp)


def run_tool(name: str, *args: str) -> subprocess.CompletedProcess[str]:
    config = _load_config()
    if name not in config:
        raise ValueError(f"Unknown tool: {name}")
    return subprocess.run([config[name], *args], check=False, text=True, capture_output=True)
