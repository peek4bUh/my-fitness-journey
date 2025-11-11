from typing import Any, Dict


class BaseOutput:
    """Automatically serializes public attributes to a dict.

    - Public attributes: instance attributes that do NOT start with '_'.
    - Handles nested BaseOutput, dicts, lists/tuples/sets, and primitives.
    """

    def to_dict(self) -> Dict[str, Any]:
        return {name: self._serialize_value(value)
                for name, value in vars(self).items()
                if not name.startswith("_")}

    def _serialize_value(self, value: Any) -> Any:
        if isinstance(value, BaseOutput):
            return value.to_dict()
        if isinstance(value, dict):
            return {k: self._serialize_value(v) for k, v in value.items()}
        if isinstance(value, (list, tuple, set)):
            return [self._serialize_value(v) for v in value]
        return value
