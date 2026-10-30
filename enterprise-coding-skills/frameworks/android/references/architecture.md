# Android — Architecture

Prefer existing module split (`:app`, `:feature:*`, `:core:*`). UI → ViewModel → use-case/repository → data sources. Keep Android framework types out of pure domain modules when that boundary exists.
