import hashlib
from typing import Any, Dict

class MuzanKibutsuji:
    def __init__(self):
        self._data: Dict[str, Any] = {}
        self._checksums: Dict[str, str] = {}

    def set(self, key: str, value: Any) -> None:
        """Set a value if it doesn't exist or hasn't changed."""
        if key not in self._data:
            self._data[key] = value
            self._update_checksum(key)
        elif self._has_changed(key, value):
            raise ValueError(f"Change detected in '{key}'. Permanence violated.")

    def get(self, key: str) -> Any:
        """Retrieve a value if it exists."""
        if key in self._data:
            return self._data[key]
        raise KeyError(f"'{key}' does not exist. Maintain permanence.")

    def _update_checksum(self, key: str) -> None:
        """Update the checksum for a given key."""
        value = str(self._data[key]).encode('utf-8')
        self._checksums[key] = hashlib.sha256(value).hexdigest()

    def _has_changed(self, key: str, new_value: Any) -> bool:
        """Check if a value has changed by comparing checksums."""
        new_checksum = hashlib.sha256(str(new_value).encode('utf-8')).hexdigest()
        return self._checksums[key] != new_checksum

    def eternal_view(self) -> Dict[str, Any]:
        """Provide an unchanging view of all data."""
        return self._data.copy()

    def assimilate(self, other: 'MuzanKibutsuji') -> None:
        """Assimilate another MuzanKibutsuji instance without changing existing data."""
        for key, value in other._data.items():
            try:
                self.set(key, value)
            except ValueError:
                pass  # Ignore changes to maintain permanence

    def purge(self, key: str) -> None:
        """Remove a key-value pair, but only if it exists."""
        if key in self._data:
            del self._data[key]
            del self._checksums[key]
        else:
            raise KeyError(f"Cannot purge non-existent key '{key}'. Maintain order.")

    def __str__(self) -> str:
        return f"MuzanKibutsuji: Eternal data store with {len(self._data)} unchanging elements."
