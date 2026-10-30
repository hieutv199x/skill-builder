# NestJS — Coding Conventions

## Naming

| Artifact | Convention (match repo if different) |
|---|---|
| Module | `users.module.ts` → `UsersModule` |
| Controller | `users.controller.ts` → `UsersController` |
| Service | `users.service.ts` → `UsersService` |
| DTO | `create-user.dto.ts` → `CreateUserDto` |
| Entity | `user.entity.ts` → `User` |
| Guard | `jwt-auth.guard.ts` → `JwtAuthGuard` |

## Dependency injection

- Constructor injection only for Nest-managed classes
- Prefer `private readonly` constructor params
- Use interfaces + custom provider tokens only when the repo already does
- Scope (`DEFAULT` / `REQUEST`) must match existing patterns — don’t make request-scoped providers casually

## DTOs & validation

When global or controller `ValidationPipe` is enabled with `class-validator`:

```typescript
import { IsEmail, IsString, MinLength } from 'class-validator';

export class CreateUserDto {
  @IsEmail()
  email!: string;

  @IsString()
  @MinLength(8)
  password!: string;
}
```

- Prefer `whitelist: true` / `forbidNonWhitelisted: true` if already configured globally — don’t fight it
- Separate `Create*` / `Update*` DTOs unless the codebase uses a single DTO by convention
- For Zod-based repos, follow existing Zod schemas — do not introduce class-validator beside Zod

## Controllers

```typescript
@Post()
@HttpCode(HttpStatus.CREATED)
create(@Body() dto: CreateUserDto) {
  return this.usersService.create(dto);
}
```

- Explicit `@HttpCode` when status is not Nest default
- Use `@Param`, `@Query`, `@Body` with typed DTOs
- Apply `@UseGuards` at controller/method consistently with sibling routes

## Services

- Throw NestHTTP or domain exceptions already used (`NotFoundException`, etc.)
- Keep methods intentional: `create`, `findById`, `update`, `remove` — or match local verbs
- Don’t return ORM entities if the API layer maps to response DTOs elsewhere in the module

## Config

- Read env via existing `ConfigService` / validated config module
- Never hardcode secrets or environment URLs in services
