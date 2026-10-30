# NestJS — Testing

Detect first: Jest version, `nestjs/testing`, e2e folder, in-memory DB vs testcontainers vs mocked repos.

## Unit test — service

```typescript
describe('UsersService', () => {
  let service: UsersService;
  let repo: { findOne: jest.Mock; save: jest.Mock };

  beforeEach(async () => {
    repo = { findOne: jest.fn(), save: jest.fn() };
    const module = await Test.createTestingModule({
      providers: [
        UsersService,
        { provide: getRepositoryToken(User), useValue: repo }, // TypeORM example
      ],
    }).compile();
    service = module.get(UsersService);
  });

  it('throws NotFoundException when missing', async () => {
    repo.findOne.mockResolvedValue(null);
    await expect(service.findById('x')).rejects.toBeInstanceOf(NotFoundException);
  });
});
```

Adapt tokens for Prisma (`PrismaService` mock) or custom repos.

## Unit test — controller (when local practice includes it)

- Mock the service provider
- Assert returned values / thrown exceptions; don’t re-test Nest plumbing

## E2E

- Use existing `test/jest-e2e.json` and `INestApplication` bootstrap helper
- Cover: 201/200 happy path, 400 validation, 401/403 auth, 404
- Clean up DB state the way sibling e2e tests do (transactions, truncate, factories)

## Commands (examples — replace with package.json scripts)

```bash
npx jest src/users/users.service.spec.ts
npm run test:e2e -- --testPathPattern=users
```

Never mark verification successful without the real exit code.
