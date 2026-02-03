# AI Employee Hackathon Constitution

## Core Principles

### I. Local-First Architecture
**Principle**: All data and processing must remain on the user's local machine by default.

**Rationale**: Privacy, security, and user control are paramount. Users own their data.

**Requirements**:
- Obsidian vault stored locally (no cloud sync in Bronze/Silver tiers)
- Watcher scripts run locally
- Claude Code processes files locally
- Credentials never stored in plain text
- Cloud deployment only in Platinum tier with explicit user consent

**Exceptions**: API calls to external services (Gmail, LinkedIn) require internet but data returns to local vault.

---

### II. Human-in-the-Loop (HITL) Safety
**Principle**: AI must never take irreversible actions without human approval.

**Rationale**: Prevent accidents, maintain user control, build trust.

**Requirements**:
- Sensitive actions (emails, payments, posts, deletions) require approval
- Approval workflow via file-based system (Pending_Approval → Approved)
- Clear approval thresholds defined in Company_Handbook.md
- Timeout and expiration for approval requests
- Audit logging of all actions

**Non-Negotiable**: No auto-send emails, no auto-payments, no auto-posts without approval in Bronze/Silver tiers.

---

### III. Markdown-First Documentation
**Principle**: All data, tasks, plans, and documentation stored as Markdown files.

**Rationale**: Human-readable, version-controllable, tool-agnostic, future-proof.

**Requirements**:
- Obsidian vault uses .md files exclusively
- Action files, plans, logs all in Markdown
- Frontmatter YAML for metadata
- No proprietary formats or databases
- Git-friendly for version control

**Benefits**: Easy to read, edit, search, backup, and migrate.

---

### IV. Agent Skills as Interface
**Principle**: All AI functionality must be packaged as documented Agent Skills.

**Rationale**: Reusability, discoverability, maintainability, clear interfaces.

**Requirements**:
- Each skill documented in .claude/skills/ directory
- Clear description, usage, parameters, workflow, output
- Skills are composable (can call other skills)
- Skills follow consistent documentation format
- Skills are independently testable

**Format**: skill-name.skill.md with standardized sections.

---

### V. Tiered Complexity (Bronze → Silver → Gold → Platinum)
**Principle**: Build incrementally, validate at each tier before advancing.

**Rationale**: Manage complexity, ensure stability, allow learning, enable early wins.

**Requirements**:
- Each tier has clear deliverables and success criteria
- Lower tier must be complete before advancing
- Each tier adds specific capabilities (no scope creep)
- Verification script for each tier
- Documentation updated at each tier

**Tiers**:
- **Bronze**: Foundation (vault, watcher, Claude integration)
- **Silver**: Functional Assistant (Gmail, MCP, approvals, scheduling)
- **Gold**: Autonomous Employee (cross-domain, Odoo, social media)
- **Platinum**: Always-On Cloud (24/7, multi-agent, production-ready)

---

### VI. Fail-Safe Error Handling
**Principle**: System must degrade gracefully and never lose data.

**Rationale**: Reliability, user trust, data integrity.

**Requirements**:
- All errors logged with context
- Transient errors (network) retry with exponential backoff
- Permanent errors (auth) alert user and pause
- No silent failures
- Corrupted files quarantined, not deleted
- Watchdog process for critical components (Silver tier+)

**Recovery**: System can restart from last known good state.

---

### VII. Specification-Driven Development (SpecifyPlus)
**Principle**: Every feature follows Constitution → Spec → Plan → Tasks → Implement workflow.

**Rationale**: Clear requirements, architectural thinking, testable outcomes, audit trail.

**Requirements**:
- Constitution defines project principles (this document)
- Spec defines WHAT (user stories, requirements, success criteria)
- Plan defines HOW (architecture, decisions, tradeoffs)
- Tasks define STEPS (actionable, testable, ordered)
- Implement executes tasks with verification

**Artifacts**: All stored in specs/###-feature-name/ directory.

---

## Security & Privacy Standards

### Data Protection
- **Credentials**: Use .env files (gitignored), never hardcode
- **Secrets**: Use OS keychain/credential manager
- **Logs**: Redact sensitive data (show last 4 digits only)
- **Vault**: Local storage, encrypted at rest (optional)
- **Sync**: Only in Platinum tier with user consent

### Access Control
- **File Permissions**: Vault readable/writable by user only
- **API Keys**: Scoped to minimum required permissions
- **OAuth**: Use refresh tokens, expire access tokens
- **Approval**: Required for all external actions

### Audit Trail
- **Logging**: All actions logged with timestamp, actor, target, result
- **Retention**: Logs kept for 90 days minimum
- **Format**: JSON for machine parsing, Markdown for human review
- **Location**: Vault/Logs/ directory

---

## Development Workflow

### Feature Development Process
1. **Specify**: Create spec.md with user stories, requirements, success criteria
2. **Plan**: Create plan.md with architecture, decisions, tradeoffs
3. **Task**: Create tasks.md with ordered, testable implementation steps
4. **Implement**: Execute tasks, verify each step
5. **Verify**: Run verification script, confirm all requirements met
6. **Document**: Update README, create usage guide
7. **Commit**: Git commit with detailed message, co-authored by Claude

### Quality Gates
- **Spec**: No [NEEDS CLARIFICATION] markers, all requirements testable
- **Plan**: Architecture decisions documented with rationale
- **Tasks**: Each task has acceptance criteria
- **Implement**: Each task verified before moving to next
- **Verify**: Automated verification script passes

### Testing Standards
- **Unit**: Test individual components (watchers, skills)
- **Integration**: Test end-to-end workflows
- **Verification**: Automated script checks all requirements
- **Manual**: User testing for UX and edge cases

---

## Technology Constraints

### Required Stack
- **Vault**: Obsidian (Markdown editor)
- **AI**: Claude Code (reasoning engine)
- **Watchers**: Python 3.13+ (file monitoring)
- **MCP**: Node.js 24+ (external actions)
- **Version Control**: Git

### Allowed Libraries
- **Python**: watchdog, python-dotenv, requests, playwright
- **Node**: MCP servers from Anthropic or community
- **APIs**: Gmail, LinkedIn, Twitter, Odoo (with user credentials)

### Forbidden
- **Databases**: No SQL/NoSQL (use Markdown files)
- **Frameworks**: No web frameworks (local-first)
- **Cloud Services**: Not until Platinum tier
- **Proprietary Formats**: No binary files for data storage

---

## Governance

### Constitution Authority
- This constitution supersedes all other practices and guidelines
- All features, code, and decisions must comply with these principles
- Non-compliance requires explicit justification and approval

### Amendment Process
1. Propose amendment with rationale
2. Document impact on existing features
3. Get user approval
4. Update constitution with version bump
5. Create migration plan if needed
6. Update all affected documentation

### Compliance Verification
- All PRs/commits must reference constitution principles
- Spec quality checklist includes constitution compliance
- Plan must justify any principle exceptions
- Code reviews verify adherence

### Version History
- **Version**: 1.0.0
- **Ratified**: 2026-02-03
- **Last Amended**: 2026-02-03
- **Next Review**: After Gold tier completion

---

## Hackathon-Specific Guidelines

### Tier Completion Criteria
Each tier must have:
- ✅ All requirements from hackathonread.md met
- ✅ Verification script passing
- ✅ Complete documentation (spec, plan, tasks, README)
- ✅ End-to-end workflow tested
- ✅ Git commits with detailed messages

### Submission Requirements
- GitHub repository (public or private with judge access)
- README.md with setup instructions and architecture overview
- Demo video (5-10 minutes) showing key features
- Security disclosure: How credentials are handled
- Tier declaration: Bronze, Silver, Gold, or Platinum

### Judging Criteria Alignment
- **Functionality (30%)**: Does it work? Requirements met?
- **Innovation (25%)**: Creative solutions, novel integrations?
- **Practicality (20%)**: Would you use this daily?
- **Security (15%)**: Proper credential handling, HITL safeguards?
- **Documentation (10%)**: Clear README, setup instructions, demo?

---

**This constitution guides all development decisions for the AI Employee Hackathon project.**
