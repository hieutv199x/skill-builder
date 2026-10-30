# Enterprise AI Coding Skills — Engineering Implementation Guide

**Version:** 1.0  
**Updated:** 2026-10-30  
**Target:** HyperLoop, Kiro IDE / Kiro CLI, enterprise multi-repository development  
**Status:** Proposed enterprise engineering standard (not an official Backbase standard)

## 1. Mục tiêu và phạm vi

Xây dựng thư viện AI Coding Skills có thể tái sử dụng trên nhiều repository và nhiều framework: Java/Spring Boot, Backbase backend, Angular/Backbase frontend, React/Next.js, Python/FastAPI/Django, .NET/ASP.NET Core, Kotlin/Android/Ktor, Swift/SwiftUI, mở rộng Node.js, Go và Flutter.

Mục tiêu: agent tự nhận diện tech stack, chọn đúng skills, đọc codebase trước khi thay đổi, tôn trọng quy tắc riêng của service, không sao chép anti-pattern, triển khai và kiểm chứng có bằng chứng. Hệ thống sử dụng AI có sẵn trong Kiro; scripts chỉ làm các việc deterministic, không yêu cầu LLM API riêng.

**Không nhầm lẫn:** `SKILL.md` là workflow/tri thức tái sử dụng; `AGENTS.md` là chính sách/context của một repository; Kiro steering là context mang tính IDE/project; Power có thể đóng gói MCP integration. Cơ chế đọc `AGENTS.md` không được giả định mặc định ở mọi agent/phiên bản: cần kiểm chứng và cấu hình explicit nếu cần.

## 2. Cơ sở tiêu chuẩn

- Agent Skills Open Specification: https://agentskills.io/specification
- Kiro Agent Skills: https://kiro.dev/docs/cli/skills/
- Kiro custom-agent resource configuration: https://kiro.dev/docs/custom-agents/configuration-reference/
- Backbase GitHub: https://github.com/Backbase
- Backbase BOAT: https://github.com/Backbase/backbase-openapi-tools

Theo Agent Skills specification: mỗi skill là thư mục có `SKILL.md` bắt buộc; file có YAML frontmatter với `name` và `description`. `scripts/`, `references/`, `assets/` là thư mục tùy chọn. Giữ `SKILL.md` tập trung (khuyến nghị dưới 500 dòng); tách reference để nạp theo nhu cầu. Các thư mục như `evals/` và registry trong guide này là **enterprise extension**, không phải yêu cầu của chuẩn.

Kiro hỗ trợ skills trong `.kiro/skills/` (workspace) và `~/.kiro/skills/` (global), cùng các resource URI kiểu `skill://...`. Không mặc định rằng registry bên ngoài sẽ được Kiro tự phát hiện; cần đồng bộ những skill đã được chọn về đường dẫn được hỗ trợ hoặc cung cấp qua custom-agent resources.

## 3. Nguyên tắc thiết kế bắt buộc

1. **Một skill = một năng lực rõ ràng:** ví dụ `spring-api-implementation`, không phải `all-java-knowledge`.
2. **Description định nghĩa when-to-use + when-not-to-use:** đủ từ khóa về task/framework để discovery chính xác.
3. **Analyze before edit:** đọc build files, dependencies, project rules, code tương đồng, contracts, tests trước khi gen.
4. **Version-aware:** xác định Java/Angular/Backbase SDK version trước khi chọn API/pattern.
5. **Repo is evidence, not authority:** pattern hiện có phải được đánh giá, không tự động sao chép.
6. **Progressive disclosure:** metadata trước, `SKILL.md` khi active, references/scripts theo nhu cầu.
7. **Deterministic tools first:** static parsing, validation, lint/build/test bằng tools khi có thể.
8. **No fabricated validation:** chỉ ghi test PASS khi đã thực thi và có exit code/evidence.
9. **Safe by default:** không đọc/ghi secret trái phép, không auto-merge/auto-deploy, không thay đổi public contract khi chưa được duyệt.
10. **Incremental changes:** ảnh hưởng ít file nhất, phân biệt breaking/non-breaking, tôn trọng branch/worktree.

## 4. Repository layout tiêu chuẩn

```text
enterprise-coding-skills/
├── README.md
├── registry/
│   ├── catalog.yaml                # index do doanh nghiệp quản lý
│   ├── compatibility.yaml          # framework, version ranges
│   └── bundles.yaml                # composition theo service type
├── foundation/
│   ├── repository-analyzer/SKILL.md
│   ├── coding-quality/SKILL.md
│   ├── secure-coding/SKILL.md
│   └── testing-strategy/SKILL.md
├── languages/
│   ├── java/SKILL.md
│   ├── typescript/SKILL.md
│   ├── python/SKILL.md
│   ├── csharp/SKILL.md
│   ├── kotlin/SKILL.md
│   └── swift/SKILL.md
├── frameworks/
│   ├── spring-boot/SKILL.md
│   ├── backbase-service/SKILL.md
│   ├── backbase-angular/SKILL.md
│   ├── angular/SKILL.md
│   ├── react/SKILL.md
│   ├── fastapi/SKILL.md
│   ├── aspnet-core/SKILL.md
│   ├── android/SKILL.md
│   └── swiftui/SKILL.md
├── workflows/
│   ├── implement-feature/SKILL.md
│   ├── fix-defect/SKILL.md
│   ├── refactor-service/SKILL.md
│   ├── review-code/SKILL.md
│   └── backfill-agents-md/SKILL.md
├── templates/
│   └── AGENTS.md.template
├── tooling/
│   └── validate-catalog.py
└── evals/
    ├── fixtures/
    ├── activation/
    ├── implementation/
    └── scorecards/
```

**Cấu trúc một skill:**

```text
backbase-service/
├── SKILL.md                         # required
├── references/
│   ├── architecture.md
│   ├── coding-conventions.md
│   ├── sdk-compatibility.md
│   └── anti-patterns.md
├── scripts/
│   └── detect-stack.py
├── assets/
│   └── templates/
└── evals/                          # enterprise extension
    ├── should-activate.yaml
    └── should-not-activate.yaml
```

## 5. `SKILL.md` — hợp đồng chuẩn

YAML frontmatter bắt buộc phải tương thích Agent Skills; metadata nội bộ được đặt trong `metadata` thay vì tùy tiện tạo top-level fields. Phần thân nên có:

| Mục | Phải mô tả |
|---|---|
| Scope | Task được làm, task không được làm |
| Detection | Cách xác định stack, version, repo guidance |
| Preconditions | Những thông tin phải kiểm tra trước khi sửa |
| Workflow | Analyze → Plan → Implement → Verify → Report |
| Decision rules | Thứ tự chọn pattern và xử lý mâu thuẫn |
| Guardrails | Security, compatibility, contract safety |
| References | File nào đọc khi nào |
| Verification | Lệnh kiểm tra theo build tool thực tế |
| Output contract | Changed files, tests, risks, evidence |

### Template copy/paste

```markdown
---
name: example-framework-development
description: >-
  Implement and modify features in [framework] repositories.
  Use for [specific tasks], when [positive triggers].
  Do not use for [negative cases].
metadata:
  version: "1.0.0"
  owner: "platform-engineering"
  category: "framework-development"
---

# Example Framework Development

## Scope
- Allowed: [task boundaries].
- Excluded: [non-goals].

## Detect
1. Read build manifests and lockfiles.
2. Identify framework/library versions, project layout and test tools.
3. Read repository AGENTS.md if present and relevant Kiro steering.
4. Inspect 1–3 relevant existing implementations; check for anti-patterns.

## Workflow
1. Analyze requirements, contracts, source and tests.
2. Choose compatible patterns; state assumptions when evidence is missing.
3. Implement the minimal safe change.
4. Run available targeted tests, lint, typecheck and build.
5. Report evidence, unresolved risks and skipped checks.

## Guardrails
- Never invent APIs or dependencies.
- Never blindly copy legacy code.
- Preserve backward compatibility unless explicitly approved.
- Never assert successful verification without execution evidence.

## References
- Read [references/architecture.md](references/architecture.md) for structural changes.
- Read [references/anti-patterns.md](references/anti-patterns.md) if the repo has risky practices.

## Output Contract
- Changed files, key decisions, tests and actual results, remaining risks.
```

## 6. Hai skills thực tế: Backbase

### 6.1 `frameworks/backbase-service/SKILL.md`

```markdown
---
name: backbase-service-development
description: >-
  Implement or change Backbase Java/Spring backend services, endpoints,
  business logic and adapters. Use for Backbase SDK backend tasks and
  service integration changes. Do not use for Angular-only UI work.
metadata:
  version: "1.0.0"
  framework: "backbase-backend"
---

# Backbase Service Development

## Scope
Implement focused changes to existing Backbase backend services.

## Detect and Analyze
1. Read `pom.xml`, `build.gradle` or `build.gradle.kts`.
2. Determine JDK, Spring and Backbase dependency versions from manifests/BOM.
3. Read repository instructions and locate controller/service/adapter patterns.
4. Inspect OpenAPI specifications, generated code boundaries and tests.
5. Flag unsupported or unverified SDK usages; do not guess APIs.

## Workflow
1. Map required behavior to impacted API, service and integration layers.
2. Prefer compatible and demonstrably healthy patterns; reject known anti-patterns.
3. Update contract first when API-first conventions require it.
4. Implement minimal modifications, handling validation, errors and security.
5. Run affected compile/tests/contract checks using the project's own tooling.
6. Report exact verification results and compatibility assumptions.

## Guardrails
- Do not change public APIs or generated sources without agreed workflow.
- Do not add new dependencies without a rationale and compatibility check.
- Do not hardcode secrets, log sensitive data or bypass authorization.
- Never introduce calls to unsupported Backbase SDK methods.

## References
- Architecture guidance: [references/architecture.md](references/architecture.md)
- SDK version policy: [references/sdk-compatibility.md](references/sdk-compatibility.md)
- Anti-pattern checklist: [references/anti-patterns.md](references/anti-patterns.md)

## Output Contract
List changed files, impacted contracts, commands executed, pass/fail results,
remaining risks, and decisions requiring approval.
```

### 6.2 `frameworks/backbase-angular/SKILL.md`

```markdown
---
name: backbase-angular-development
description: >-
  Implement Backbase Angular frontend journeys, components, forms,
  routing, API clients and UI tests. Use for Backbase Angular app changes.
  Do not use for Java backend-only tasks.
metadata:
  version: "1.0.0"
  framework: "backbase-angular"
---

# Backbase Angular Development

## Scope
Change Angular functionality using the versions and patterns supported
by the actual Backbase frontend application.

## Detect and Analyze
1. Read `package.json`, lockfile, `angular.json`, `nx.json` if present.
2. Detect Angular, Nx and Backbase frontend package versions.
3. Read repo instructions and existing journey/component conventions.
4. Identify API client generation boundaries, state and testing stack.
5. Check accessibility requirements and design-system usage.

## Workflow
1. Trace requirement through journeys, routes, state and API contracts.
2. Reuse compatible components and approved UI patterns.
3. Handle loading, empty, success and error states.
4. Implement accessible, testable and minimal changes.
5. Run applicable lint, typecheck, unit tests and build commands.
6. Report UI coverage and validation gaps.

## Guardrails
- Do not assume the latest Angular API is installed.
- Do not invent Backbase component exports or generated client methods.
- Do not introduce a new state library without architecture approval.
- Do not bypass authentication, permissions or accessibility rules.

## References
- UI conventions: [references/component-patterns.md](references/component-patterns.md)
- Version support: [references/version-compatibility.md](references/version-compatibility.md)
- Anti-patterns: [references/anti-patterns.md](references/anti-patterns.md)

## Output Contract
List changed journeys/components, API impacts, commands/results,
accessibility checks and remaining risks.
```

> Hai mẫu Backbase là **enterprise-proposed skills**, không phải skills do Backbase chính thức phân phối. Các files trong `references/` cần được soạn từ codebase và documentation mà doanh nghiệp có quyền truy cập; không tạo nội dung SDK chưa được xác minh.

## 7. Skill discovery, selection và composition

**Mặc định của Kiro:** tự chọn skill bằng `name`/`description` hoặc user gọi `/skill-name`. **Mở rộng của HyperLoop:** registry và selector riêng (deterministic + Kiro inference) để quản lý quy mô lớn; đây không phải tính năng mặc định được bảo đảm của Kiro.

**Pipeline đề xuất:**

```text
User Story / DevSpec / Ticket
           |
           v
Repository Detection (manifests + code + project guidance)
           |
           v
Candidate Filtering (task type, stack, version, policy)
           |
           v
Skill Selection (top applicable skills; resolve conflicts)
           |
           v
Sync Selected Skills into supported Kiro skill scope
           |
           v
Kiro Session: Analyze → Implement → Verify → Report
           |
           v
Eval Center + Skill Feedback
```

**Priority resolution:** security/legal policy > explicit approved repository contracts > version compatibility > project-specific validated guidance > reusable framework guidance > weak/inferred examples. Nếu xung đột chưa rõ, không tự ý sửa public contract.

**Anti-overloading:** task đơn giản thường dùng workflow skill + framework skill + một skill kiểm tra cần thiết. Không cố định bắt buộc 4–8 skills cho mọi prompt; chọn theo bằng chứng.

**Ví dụ:** Backbase Angular story → `implement-feature` + `backbase-angular-development` + (khi cần) `angular` + `frontend-testing`. Không tự động tải `spring-boot` trừ khi scope có backend.

## 8. `AGENTS.md` — quy tắc cho từng service

File này nên ngắn, cụ thể, được sinh từ repository evidence và được review. Không coi `AGENTS.md` là bộ framework skill khác. Cách Kiro tiêu thụ file phải được kiểm chứng trong môi trường đang triển khai; nếu cần chắc chắn, tạo Kiro steering hoặc explicit custom-agent resource để đọc.

### Mẫu

```markdown
# Service Development Instructions

## Identity
- Service: [name]
- Stack: [detected versions]
- Build/test tools: [actual commands]

## Architecture
- Responsibilities and boundaries: [verified]
- Entry points: [paths]
- Contracts and dependencies: [paths]

## Coding Rules
- MUST: [rules evidenced by project/reference standards]
- SHOULD: [preferred conventions]
- MUST NOT: [verified anti-patterns + reason]

## Workflow
- Read relevant contracts before editing.
- Use applicable enterprise skills.
- Run targeted checks before declaring completion.

## Known Exceptions / Legacy Debt
- [file/pattern, rationale, remediation scope]

## Evidence
- [repo paths, build outputs, approved architectural sources]
```

### Backfill workflow

1. Inventory repository and detect tech stack + versions; record confidence.
2. Read representative architecture, manifests, tests and existing docs.
3. Compare observed patterns with compatible framework guidance.
4. Categorize: `GOOD`, `LEGACY-ACCEPTED`, `BAD`, `UNKNOWN`.
5. Draft `AGENTS.md` with evidence paths and explicit constraints.
6. Evaluate against representative tasks; ensure rules do not block valid changes.
7. Request service owner review before merge.
8. Recheck when dependencies/architecture materially change.

Never turn a detected bad pattern into a new best practice merely because it is common in the repository.

## 9. Quality evaluation và release gates

### Evaluation suites

- **Activation positives:** matching prompts must select the intended skill.
- **Activation negatives:** unrelated prompts must *not* select it.
- **Version compatibility:** fixtures using older and newer supported versions.
- **Implementation correctness:** compile/tests pass for seeded tasks.
- **Contract safety:** detect unintended API/schema changes.
- **Security:** reject secrets exposure and bypass patterns.
- **Context efficiency:** compare loaded references, tool invocations and elapsed time.

### Suggested weighted scorecard (not standard requirements)

| Criterion | Weight |
|---|---:|
| Discovery accuracy | 20% |
| Implementation correctness | 25% |
| Version compatibility | 15% |
| Guardrail compliance | 15% |
| Verification quality | 15% |
| Context efficiency | 10% |

Suggested release threshold **85/100**, with **zero critical security/contract violations**. A score is not enough without passing real integration tests.

### CI gates

1. Validate standard frontmatter and valid relative references (`skills-ref validate` when available).
2. Validate registry unique IDs, dependency resolution and version constraints.
3. Run positive/negative activation fixtures.
4. Run implementation smoke tests on representative project fixtures.
5. Require owner approval for promoted releases.
6. Record skill release ID, test evidence and compatibility snapshot.

## 10. Versioning và lifecycle

- Use semantic versioning at skill level: MAJOR for behavioral/breaking changes; MINOR for compatible capability; PATCH for fixes/docs.
- Maintain skill `metadata.version` and registry compatibility matrix independently from framework release versions.
- Pin released skill versions per project or workflow run to support reproducibility.
- New framework release triggers compatibility review, *not* automatic assumption of support.
- Maintain owner, change log, deprecation notice, audit trail and rollback policy.
- Do not embed proprietary Backbase docs/source in shared public skills without rights.

## 11. Roadmap triển khai

| Phase | Deliverables | Acceptance |
|---|---|---|
| P0 — Foundation | Skill specification, template, registry, repo analyzer, eval harness | Valid structure, activation smoke tests |
| P1 — Core frameworks | Spring, Angular, React, Python, .NET + test skills | Example repositories pass task fixtures |
| P2 — Banking stack | Backbase backend/frontend, BOAT and cross-service contracts | Version-aware + contract-safe changes |
| P3 — Mobile | Kotlin Android, Swift/SwiftUI, mobile test skills | Android/iOS sample builds and tests |
| P4 — Enterprise adoption | Backfill AGENTS.md, selection bundles, CI gates, telemetry | Owner reviews and measurable quality trends |

## 12. Definition of Done

A skill is release-ready only when:

- [ ] Valid `SKILL.md` and accurate positive/negative discovery description.
- [ ] All references and scripts exist and run on supported environments.
- [ ] Framework/version compatibility is specified and tested.
- [ ] Instructions distinguish source evidence from assumptions.
- [ ] Security and contract guardrails are explicit.
- [ ] Tests include both matching and non-matching scenarios.
- [ ] The skill can be used without adding separate LLM APIs.
- [ ] Owner has approved release and registry metadata.

## 13. Khuyến nghị triển khai đầu tiên

Begin with **repository-analyzer**, **backfill-agents-md**, **spring-boot**, **angular**, **backbase-service**, and **backbase-angular**. Validate their activation and generated changes on a handful of real repos before scaling the catalog. Prioritize skill quality and task coverage over raw skill count.

---

**Source references**  
Agent Skills: https://agentskills.io/specification  
Kiro Skills: https://kiro.dev/docs/cli/skills/  
Kiro custom-agent resources: https://kiro.dev/docs/custom-agents/configuration-reference/  
Backbase GitHub: https://github.com/Backbase
