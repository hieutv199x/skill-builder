# Java Conventions

- Match Java language level (records, sealed, pattern switch only if supported)
- Prefer clear packages aligned with modules
- Optional as return type for absence — not fields everywhere
- Checked vs unchecked exceptions: follow module practice
- Keep public surface small; package-private by default when possible
- Equals/hashCode/toString: prefer records or existing utilities
