"""Settings and configuration for Argos Translate.

This module handles application-wide settings including paths for
package storage, cache directories, and other configuration options.
"""

import os
from pathlib import Path

# Application name
APP_NAME = "argos-translate"

# Base directories
def _get_data_dir() -> Path:
    """Get the base data directory for Argos Translate.

    Respects XDG_DATA_HOME on Linux/macOS, uses APPDATA on Windows.
    Can be overridden with ARGOS_TRANSLATE_DATA_DIR environment variable.
    """
    env_override = os.environ.get("ARGOS_TRANSLATE_DATA_DIR")
    if env_override:
        return Path(env_override)

    if os.name == "nt":  # Windows
        base = Path(os.environ.get("APPDATA", Path.home() / "AppData" / "Roaming"))
    else:  # Linux / macOS
        base = Path(os.environ.get("XDG_DATA_HOME", Path.home() / ".local" / "share"))

    return base / APP_NAME


def _get_cache_dir() -> Path:
    """Get the cache directory for Argos Translate.

    Respects XDG_CACHE_HOME on Linux/macOS.
    Can be overridden with ARGOS_TRANSLATE_CACHE_DIR environment variable.
    """
    env_override = os.environ.get("ARGOS_TRANSLATE_CACHE_DIR")
    if env_override:
        return Path(env_override)

    if os.name == "nt":  # Windows
        base = Path(os.environ.get("LOCALAPPDATA", Path.home() / "AppData" / "Local"))
    else:  # Linux / macOS
        base = Path(os.environ.get("XDG_CACHE_HOME", Path.home() / ".cache"))

    return base / APP_NAME


# Resolved directory paths
data_dir: Path = _get_data_dir()
cache_dir: Path = _get_cache_dir()

# Package storage directory — where .argosmodel files are installed
package_data_dir: Path = data_dir / "packages"

# Directory for downloaded but not yet installed packages
downloads_dir: Path = cache_dir / "downloads"

# Path to the local package index cache
package_index_path: Path = cache_dir / "index.json"

# Remote package index URL
package_index_url: str = os.environ.get(
    "ARGOS_TRANSLATE_PACKAGE_INDEX_URL",
    "https://raw.githubusercontent.com/argosopentech/argospm-index/main/index.json",
)

# Whether to verify SSL certificates when downloading packages
verify_ssl: bool = os.environ.get("ARGOS_TRANSLATE_VERIFY_SSL", "true").lower() != "false"

# Request timeout in seconds for network operations
request_timeout: int = int(os.environ.get("ARGOS_TRANSLATE_REQUEST_TIMEOUT", "30"))

# Whether to use GPU acceleration if available (requires CTranslate2 with CUDA)
device: str = os.environ.get("ARGOS_TRANSLATE_DEVICE", "auto")

# Inter-sentence delimiter used when splitting text for translation
sentence_split_max_chars: int = int(
    os.environ.get("ARGOS_TRANSLATE_SENTENCE_SPLIT_MAX_CHARS", "1500")
)


def ensure_dirs() -> None:
    """Create required application directories if they do not exist."""
    for directory in (package_data_dir, downloads_dir, cache_dir):
        directory.mkdir(parents=True, exist_ok=True)
