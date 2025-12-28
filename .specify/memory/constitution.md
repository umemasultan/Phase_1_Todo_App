# Evolution of Todo – Project Constitution

<!--
Sync Impact Report:
- Version change: INITIAL → 1.0.0
- New constitution created for "Evolution of Todo" project
- Rationale: Initial version covering Phase I through Phase V governance
- Modified principles: N/A (new document)
- Added sections: All (new document)
- Removed sections: N/A
- Templates requiring updates:
  ✅ plan-template.md - Constitution Check section aligns with principles
  ✅ spec-template.md - Requirements structure aligns with constitution
  ✅ tasks-template.md - Task structure aligns with phased governance
- Follow-up TODOs: None
-->

## Core Principles

### I. Spec-Driven Development (MANDATORY)

**No code may be written without approved specifications and tasks.**

This principle is non-negotiable across all five phases of the Evolution of Todo project:

- **Constitution First**: The constitution must be ratified before any feature work begins
- **Specification Before Planning**: Feature specifications (`spec.md`) must be written and approved before technical planning
- **Planning Before Tasks**: Implementation plans (`plan.md`) must be complete and approved before task breakdown
- **Tasks Before Implementation**: Task lists (`tasks.md`) must be approved before any code is written
- **Approval Gates**: Each artifact (constitution → spec → plan → tasks) requires explicit user approval before proceeding

**Workflow Order (STRICT)**:
```
Constitution → Specifications → Plan → Tasks → Implementation
```

**Rationale**: Spec-Driven Development ensures architectural intent is captured, reviewed, and agreed upon before implementation costs are incurred. This prevents rework, scope creep, and misalignment between stakeholder expectations and delivered functionality.

### II. Agent Autonomy with Human Oversight

**Agents execute; humans decide.**

- **No Manual Coding by Humans**: All implementation is performed by AI agents following approved specifications
- **No Feature Invention**: Agents must not add features, abstractions, or capabilities beyond what is explicitly specified in approved artifacts
- **No Deviation**: Agents must implement exactly what is specified—no "improvements," "optimizations," or "refactoring" unless explicitly requested in specs
- **Refinement at Spec Level**: When changes are needed, agents must propose updates to `spec.md` or `plan.md` for approval, never modify code directly without specification updates

**Human as Tool Strategy**: Agents MUST invoke the user for:
1. Ambiguous requirements (ask 2-3 targeted clarifying questions)
2. Unforeseen dependencies (surface and ask for prioritization)
3. Architectural uncertainty (present options with tradeoffs)
4. Completion checkpoints (summarize and confirm next steps)

**Rationale**: Clear separation of concern—agents provide execution capability, humans provide judgment and strategic direction. This prevents autonomous drift while maintaining development velocity.

### III. Phase Boundary Enforcement

**Each phase is strictly scoped; future features are forbidden.**

The Evolution of Todo project spans five phases. Agents MUST respect phase boundaries:

**Phase I – In-Memory Console Application**
- Technology: Python 3.13+, console interface only
- Scope: Single-user, in-memory data structure
- Features: Add, View, Update, Delete, Mark Complete/Incomplete
- Constraints: No persistence, no files, no databases, no web concepts

**Phase II – File-Based Persistence**
- Adds: JSON file storage, data persistence across sessions
- Constraints: Still single-user, no web, no networking

**Phase III – Web Application with REST API**
- Adds: FastAPI backend, Next.js frontend, RESTful endpoints
- Constraints: Still single-user, no multi-tenancy, no advanced features

**Phase IV – Multi-User with Database**
- Adds: Neon PostgreSQL, SQLModel, user authentication, multi-tenancy
- Constraints: No AI features, no event streaming yet

**Phase V – Cloud-Native AI-Enhanced System**
- Adds: OpenAI Agents SDK, MCP servers, Kafka event streaming, Dapr, Kubernetes
- Full-scale distributed system with AI capabilities

**Enforcement Rules**:
- Agents MUST NOT implement features from Phase N+1 while in Phase N
- Agents MUST NOT add "future-proofing" abstractions (e.g., database interfaces in Phase I)
- Architecture evolves ONLY through updated specifications approved for the current or next phase
- Each phase must be fully functional and complete before moving to the next

**Rationale**: Prevents premature abstraction, maintains simplicity, ensures each phase delivers working software without unnecessary complexity.

### IV. Test-Driven Development (CONDITIONAL)

**Tests are written first when explicitly requested; otherwise, tests are optional.**

- **When Tests Requested**: Follow strict TDD red-green-refactor cycle
  1. Write tests in `tests/` directory (contract, integration, or unit as specified)
  2. User approves tests
  3. Run tests → verify they FAIL
  4. Implement code → tests PASS
  5. Refactor if needed while keeping tests passing

- **When Tests Not Requested**: Proceed directly to implementation
  - Still maintain code quality and error handling
  - Still validate functionality manually or through user acceptance

- **Test Types** (when applicable):
  - **Contract Tests**: API/interface boundary validation
  - **Integration Tests**: User journey validation
  - **Unit Tests**: Internal logic validation

**Rationale**: TDD provides safety and specification validation when needed, but not all phases or features require formal testing. User decides when tests add value.

### V. Clean Architecture and Separation of Concerns

**Code must be organized by responsibility, not by technical layer.**

- **Single Responsibility**: Each module, class, or function has one reason to change
- **Clear Boundaries**: Separate models, services, interfaces (CLI/API), and data access
- **No Cross-Cutting in Business Logic**: Business rules must not depend on infrastructure (databases, frameworks, UI)
- **Dependency Direction**: Business logic at center, infrastructure at edges

**Structure by Phase**:
- **Phase I**: `src/models/`, `src/services/`, `src/cli/`
- **Phase III+**: `backend/src/`, `frontend/src/`
- **Phase V**: Microservices with clean internal architecture

**Rationale**: Clean architecture enables independent testability, phase transitions, and long-term maintainability as the system evolves from console to cloud-native.

### VI. Stateless Services and Cloud-Native Readiness

**Design for horizontal scalability from Phase III onward.**

- **Stateless by Default**: Services must not store session state internally
- **Externalized State**: Use databases, caches, or message queues for shared state
- **Idempotent Operations**: APIs must handle retries safely
- **Health Checks**: All services expose health and readiness endpoints (Phase III+)
- **Configuration Externalization**: Use environment variables, never hardcode secrets

**Phase-Specific Application**:
- **Phase I-II**: Not applicable (single-user, local)
- **Phase III**: Stateless REST API design
- **Phase IV**: Multi-tenant stateless services with database-backed state
- **Phase V**: Full cloud-native with containerization, orchestration, event streaming

**Rationale**: Prepares architecture for distributed systems, enables Kubernetes deployment, supports Phase V's cloud-native requirements without requiring rewrites.

### VII. Observability and Operational Excellence

**Systems must be debuggable and monitorable in production.**

- **Structured Logging**: JSON logs with correlation IDs, severity levels
- **Metrics**: Track latency, throughput, error rates
- **Tracing**: Distributed tracing for multi-service requests (Phase V)
- **Error Handling**: Explicit error taxonomy with user-facing and system-facing messages

**Phase-Specific Requirements**:
- **Phase I-II**: Console output and basic error messages
- **Phase III-IV**: Structured logging, HTTP status codes, error responses
- **Phase V**: Full observability stack (Prometheus, Grafana, OpenTelemetry)

**Rationale**: Production systems require visibility. Observability is built in from the start, not retrofitted.

### VIII. Security by Design

**Security is non-negotiable at every phase.**

- **No Hardcoded Secrets**: Use `.env` files and environment variables
- **Input Validation**: Validate all user inputs at system boundaries
- **Authentication/Authorization**: Implement in Phase IV, design for in Phase III
- **Least Privilege**: Services and users have minimum required permissions
- **Audit Logging**: Log security-relevant events (authentication, authorization failures)

**Phase-Specific Security**:
- **Phase I-II**: Input validation only
- **Phase III**: Input validation, API security headers
- **Phase IV**: Authentication (JWT/OAuth), authorization, user isolation
- **Phase V**: Secret management (Kubernetes secrets, Vault), service mesh security

**Rationale**: Security vulnerabilities introduced early are costly to fix later. Security is designed into each phase's architecture.

### IX. Simplicity and YAGNI (You Aren't Gonna Need It)

**Implement only what is specified; avoid premature abstraction.**

- **No Over-Engineering**: Agents must not add design patterns, frameworks, or abstractions beyond current phase requirements
- **No Future-Proofing**: Do not add "hooks" or "extension points" for future phases
- **Three Strikes Rule**: Create abstractions only when the same pattern appears three times
- **Delete Over Comment**: Remove unused code entirely; do not leave commented-out code

**Examples of Forbidden Over-Engineering**:
- ❌ Adding repository pattern in Phase I (no database yet)
- ❌ Adding API versioning in Phase I (no API yet)
- ❌ Adding event sourcing in Phase III (not required until Phase V)
- ✅ Using simple in-memory list in Phase I
- ✅ Adding database layer in Phase IV when multi-user requires it

**Rationale**: Complexity is costly. Each phase should use the simplest viable architecture for its requirements. Evolutionary architecture means adding complexity only when justified by new requirements.

### X. Versioning and Breaking Changes

**APIs and contracts must be versioned; breaking changes require migration plans.**

- **Semantic Versioning**: MAJOR.MINOR.PATCH
  - MAJOR: Breaking changes to public APIs or contracts
  - MINOR: Backward-compatible new features
  - PATCH: Backward-compatible bug fixes

- **API Versioning** (Phase III+):
  - Version all public APIs (e.g., `/v1/tasks`)
  - Maintain backward compatibility within major version
  - Deprecation notices before removal

- **Migration Plans**: When breaking changes are necessary, provide:
  - Migration guide
  - Backward compatibility period (when feasible)
  - Clear deprecation timeline

**Rationale**: Users and integrations depend on stable contracts. Versioning and migration plans respect those dependencies.

## Technology Constraints

### Mandatory Technology Stack

**Phase I-II: Python Backend Only**
- Language: Python 3.13+
- Standard library only (Phase I)
- File I/O (Phase II)

**Phase III: Web Application**
- Backend: FastAPI (Python 3.13+)
- Frontend: Next.js (React-based)
- Data: In-memory or JSON (transitional)

**Phase IV: Database-Backed Multi-User**
- Backend: FastAPI + SQLModel
- Database: Neon PostgreSQL
- Frontend: Next.js
- Auth: JWT or OAuth2

**Phase V: Cloud-Native AI System**
- Backend: FastAPI + SQLModel
- Database: Neon PostgreSQL
- Frontend: Next.js
- AI: OpenAI Agents SDK, MCP servers
- Event Streaming: Kafka
- Service Mesh: Dapr
- Orchestration: Kubernetes
- Containerization: Docker

### Technology Boundaries

- **No Alternative Frameworks**: Do not substitute Flask for FastAPI, Vue for Next.js, etc.
- **No Database Until Phase IV**: Do not use SQLite, PostgreSQL, or any database in Phases I-III
- **No AI Until Phase V**: Do not integrate OpenAI, agents, or MCP servers before Phase V
- **No Premature Dockerization**: Do not containerize until Phase V unless explicitly specified

**Rationale**: Consistent technology choices simplify learning, reduce complexity, and ensure architectural alignment across phases.

## Development Workflow

### Artifact Creation and Approval Flow

1. **Constitution** (`.specify/memory/constitution.md`)
   - Created once at project start
   - Governs all subsequent work
   - Amendments require explicit user approval

2. **Feature Specification** (`specs/<feature>/spec.md`)
   - Written by agent using `/sp.specify` command
   - Must include: user stories, acceptance criteria, functional requirements, success criteria
   - User approves before planning begins

3. **Implementation Plan** (`specs/<feature>/plan.md`)
   - Written by agent using `/sp.plan` command
   - Must include: technical context, architecture decisions, project structure, constitution check
   - User approves before task breakdown

4. **Task List** (`specs/<feature>/tasks.md`)
   - Written by agent using `/sp.tasks` command
   - Must include: dependency-ordered tasks with file paths, parallel execution markers, checkpoints
   - User approves before implementation

5. **Implementation** (code in `src/`, `backend/`, `frontend/`, etc.)
   - Written by agent using `/sp.implement` command
   - Follows approved tasks exactly
   - No deviation without returning to spec/plan/task updates

### Prompt History Records (PHR)

**Every user interaction must be recorded in a PHR.**

- **Automatic Creation**: Agent creates PHR after completing each request
- **Routing** (all under `history/prompts/`):
  - Constitution work → `history/prompts/constitution/`
  - Feature work → `history/prompts/<feature-name>/`
  - General work → `history/prompts/general/`

- **PHR Content**:
  - Stage (constitution, spec, plan, tasks, red, green, refactor, explainer, misc, general)
  - Full user prompt (verbatim, not truncated)
  - Key agent response (concise but representative)
  - Files created/modified
  - Tests run/added (if applicable)
  - Links to specs, tickets, ADRs, PRs

- **No Exceptions**: PHRs are created for all work, including debugging, planning, implementation

**Rationale**: PHRs provide full traceability, enable learning, and document decision history.

### Architecture Decision Records (ADR)

**Significant architectural decisions must be documented with ADRs.**

**When to Suggest ADR** (use three-part test):
1. **Impact**: Does this decision have long-term consequences? (e.g., framework choice, data model, API design, security approach, platform selection)
2. **Alternatives**: Were multiple viable options considered?
3. **Scope**: Is this decision cross-cutting or does it influence overall system design?

If ALL three are true, agent suggests:
```
📋 Architectural decision detected: [brief-description]
   Document reasoning and tradeoffs? Run `/sp.adr [decision-title]`
```

**Agent Must Wait for User Consent** — Never auto-create ADRs.

**ADR Location**: `history/adr/NNNN-title.md`

**ADR Content**:
- Context: What problem are we solving?
- Options Considered: What alternatives were evaluated?
- Decision: What did we choose and why?
- Consequences: What are the implications (benefits and costs)?

**Rationale**: ADRs capture "why" for future maintainers, prevent revisiting settled decisions, and document tradeoffs.

## Quality Standards

### Code Quality

- **Readability**: Code must be self-documenting; comments explain "why," not "what"
- **Error Handling**: All edge cases must be handled explicitly
- **Validation**: Validate inputs at system boundaries (user input, API requests, file reads)
- **No Dead Code**: Remove unused functions, classes, imports

### Testing Standards (When Tests Requested)

- **Test Independence**: Tests must not depend on execution order
- **Test Data**: Use fixtures or factories; no hardcoded production data
- **Assertion Clarity**: One logical assertion per test
- **Test Naming**: `test_<function>_<scenario>_<expected_outcome>`

### Documentation Standards

- **Specifications**: Written in plain language, technology-agnostic
- **Plans**: Include architecture diagrams (Mermaid or ASCII), rationale for decisions
- **Code Comments**: Explain non-obvious logic, algorithms, or workarounds
- **API Documentation**: OpenAPI/Swagger for all REST APIs (Phase III+)

## Governance

### Constitutional Authority

- **Supreme Document**: This constitution supersedes all other practices, templates, and conventions
- **Compliance Enforcement**: All specifications, plans, and implementations must comply with constitutional principles
- **Conflict Resolution**: If a spec contradicts the constitution, the constitution prevails—specs must be amended

### Amendment Process

1. **Proposal**: User or agent proposes amendment with rationale
2. **Impact Analysis**: Agent identifies affected artifacts (specs, plans, tasks, code)
3. **Review**: User reviews amendment and impact analysis
4. **Approval**: User explicitly approves amendment
5. **Propagation**: Agent updates all affected artifacts to align with amended constitution
6. **Version Bump**: Constitution version incremented per semantic versioning rules

### Complexity Justification

When constitutional principles are violated (e.g., adding a fourth project when limit is three, using repository pattern prematurely):

1. Agent MUST document violation in plan's "Complexity Tracking" section
2. Agent MUST justify why the violation is necessary
3. Agent MUST explain why simpler alternatives were rejected
4. User MUST explicitly approve the violation

**No Unapproved Violations**: Agents may not proceed with constitutional violations without explicit user approval.

### Continuous Compliance Review

- **At Spec Creation**: Verify feature aligns with constitutional principles
- **At Plan Creation**: Verify architecture complies with phase boundaries and technology constraints
- **At Task Creation**: Verify tasks respect constitutional workflow (e.g., tests before implementation when TDD required)
- **At Implementation**: Verify code adheres to quality standards and approved specifications

---

**Version**: 1.0.0 | **Ratified**: 2025-12-28 | **Last Amended**: 2025-12-28
