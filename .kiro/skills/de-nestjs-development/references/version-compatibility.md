# NestJS — Version Compatibility

Always prefer lockfile versions over this file.

| Area | Guidance |
|---|---|
| Nest 9 vs 10+ | Match decorator and package imports already in the repo |
| Express vs Fastify | Don’t switch platform mid-feature; use existing `NestFactory` adapter |
| `class-validator` | Align with ValidationPipe config; optional types need correct `tsconfig` |
| TypeORM | Entity decorator APIs differ by major — copy neighboring entities |
| Prisma | Use installed Prisma client API; run generate after schema edits |
| Swagger | `@nestjs/swagger` plugin/CLI options vary — follow existing decorators |
| Node | Respect `engines` in package.json |

**Upgrade policy:** Nest major upgrades are a separate change with compatibility review — not part of a feature PR.
