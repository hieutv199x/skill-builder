# Test Levels

1. **Unit** — fast, isolated, deterministic
2. **Integration** — real or sanctioned test doubles for DB/bus
3. **Contract** — OpenAPI/consumer-driven when present
4. **E2E** — sparse; critical paths only

Prefer adding tests next to existing suites.
