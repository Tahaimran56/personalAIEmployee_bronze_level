# Implementation Plan: Bronze Tier Foundation

**Branch**: `001-bronze-tier-foundation` | **Date**: 2026-02-03 | **Spec**: [spec.md](spec.md)
**Input**: Feature specification from `/specs/001-bronze-tier-foundation/spec.md`

## Summary

Build the foundational infrastructure for a Personal AI Employee using a local-first architecture. The system consists of an Obsidian vault for data storage, Python-based file system watcher for automatic detection of new work, Claude Code for AI-powered processing, and documented Agent Skills for reusable automation capabilities. This Bronze tier establishes the core "nervous system" (perception), "brain" (reasoning), and "memory" (storage) for the AI Employee.

**Primary Technical Approach**: File-based automation using Markdown documents, event-driven architecture with watchers, and human-readable state management in Obsidian vault.

## Technical Context

**Language/Version**: Python 3.13+
**Primary Dependencies**:
- watchdog 6.0.0 (file system monitoring)
- python-dotenv 1.2.1 (environment variables)
- Obsidian (Markdown vault, no version constraint)
- Claude Code 2.1.30 (AI reasoning engine)

**Storage**: Local filesystem (Markdown files in Obsidian vault)
**Testing**: Manual verification via verify_bronze.py script + end-to-end workflow testing
**Target Platform**: Cross-platform (Windows, macOS, Linux)
**Project Type**: Single project (local automation system)
**Performance Goals**:
- File detection within 10 seconds
- Action file creation < 1 second
- Dashboard updates < 2 seconds
**Constraints**:
- Local-only (no cloud services)
- Human-readable formats (Markdown)
- No databases (file-based storage)
**Scale/Scope**:
- Single user
- ~100 files/day processing capacity
- 7 vault folders
- 3 Agent Skills

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

✅ **I. Local-First Architecture**: All data stored in local Obsidian vault, no cloud services
✅ **II. Human-in-the-Loop (HITL) Safety**: Approval workflow structure created (Pending_Approval folder)
✅ **III. Markdown-First Documentation**: All files are .md with YAML frontmatter
✅ **IV. Agent Skills as Interface**: 3 skills documented in .claude/skills/
✅ **V. Tiered Complexity**: Bronze tier scope clearly defined, Silver tier out of scope
✅ **VI. Fail-Safe Error Handling**: Watcher logs errors, no silent failures
✅ **VII. Specification-Driven Development**: Spec created (retrospectively for Bronze)

**Constitution Compliance**: ✅ PASS - All principles followed

## Project Structure

### Documentation (this feature)

```text
specs/001-bronze-tier-foundation/
├── spec.md                    # Feature specification (user stories, requirements)
├── plan.md                    # This file (architecture decisions)
├── tasks.md                   # Implementation tasks (to be created)
└── checklists/
    └── requirements.md        # Specification quality checklist
```

### Source Code (AI_Employee_Vault)

```text
AI_Employee_Vault/
├── .obsidian/                 # Obsidian configuration
│   └── app.json              # Vault settings
├── .claude/skills/            # Agent Skills documentation
│   ├── process-actions.skill.md
│   ├── update-dashboard.skill.md
│   └── start-watcher.skill.md
├── Inbox/                     # Entry point for new files
├── Needs_Action/              # Tasks awaiting processing
├── Done/                      # Completed tasks archive
├── Pending_Approval/          # Actions awaiting human approval
├── Approved/                  # Approved actions ready for execution
├── Plans/                     # Multi-step task plans
├── Logs/                      # Activity audit trail
│   └── FileSystemWatcher.log # Watcher activity log
├── Dashboard.md               # Main command center
├── Company_Handbook.md        # Operating rules and guidelines
├── README.md                  # Setup and usage guide
├── BRONZE_TIER_README.md      # Complete implementation guide
├── BRONZE_TIER_COMPLETE.md    # Achievement report
├── SILVER_TIER_ROADMAP.md     # Next tier planning
├── base_watcher.py            # Abstract base class for watchers
├── filesystem_watcher.py      # File system monitoring implementation
├── verify_bronze.py           # Automated verification script
└── requirements.txt           # Python dependencies
```

**Structure Decision**: Single project structure chosen because Bronze tier is a standalone local automation system with no frontend/backend separation. All components run locally on user's machine.

## Complexity Tracking

No constitution violations. All complexity is justified by Bronze tier requirements.

---

## Phase 0: Research & Discovery

### Existing Codebase Analysis

**Finding**: No existing codebase - greenfield project for hackathon.

**Key Insights**:
- Hackathon requirements clearly defined in hackathonread.md
- Bronze tier is minimum viable deliverable (8-12 hours estimated)
- Must use Obsidian for vault, Claude Code for AI, Python for watchers
- Agent Skills are mandatory (not optional)

### Technology Selection

#### Obsidian for Vault
**Decision**: Use Obsidian as the knowledge base and GUI

**Rationale**:
- Markdown-first (human-readable, version-controllable)
- Local storage (privacy, security)
- Cross-platform (Windows, Mac, Linux)
- No lock-in (plain .md files)
- Rich plugin ecosystem (future extensibility)

**Alternatives Considered**:
- Notion: Rejected (cloud-based, proprietary format)
- VS Code: Rejected (not designed for knowledge management)
- Custom web app: Rejected (over-engineering for Bronze tier)

#### Python for Watchers
**Decision**: Use Python 3.13+ with watchdog library

**Rationale**:
- Cross-platform file system monitoring
- Simple to implement and maintain
- Rich ecosystem for future integrations (Gmail API, etc.)
- User likely has Python installed

**Alternatives Considered**:
- Node.js: Rejected (adds another runtime dependency)
- Bash scripts: Rejected (not cross-platform, limited functionality)
- Built into Claude Code: Rejected (Claude Code is interactive, not daemon)

#### Claude Code for AI Processing
**Decision**: Use Claude Code as the reasoning engine

**Rationale**:
- Required by hackathon (Claude Code is the primary tool)
- Powerful file operations (read, write, edit)
- Can follow Company Handbook rules
- Integrates with MCP servers (Silver tier)

**Alternatives Considered**:
- OpenAI API: Rejected (hackathon requires Claude)
- Local LLM: Rejected (resource-intensive, lower quality)

### Architecture Pattern

**Decision**: Event-Driven Architecture with File-Based State

**Pattern**:
```
[File Drop] → [Watcher Detects] → [Action File Created] → [Claude Processes] → [Task Completed] → [Dashboard Updated]
```

**Rationale**:
- Simple to understand and debug
- No complex message queues or databases
- Human-readable state (Markdown files)
- Easy to recover from failures (files persist)

**Alternatives Considered**:
- Database-driven: Rejected (violates Markdown-first principle)
- API-based: Rejected (over-engineering, requires server)
- Cron-based polling: Rejected (less responsive than event-driven)

---

## Phase 1: Design Decisions

### 1. Vault Folder Structure

**Decision**: 7-folder structure with clear separation of concerns

**Folders**:
- **Inbox**: Entry point (watcher monitors this)
- **Needs_Action**: Pending tasks (Claude processes these)
- **Done**: Completed tasks (archive)
- **Pending_Approval**: Awaiting human review (HITL workflow)
- **Approved**: Ready for execution (orchestrator processes these)
- **Plans**: Multi-step strategies (Silver tier+)
- **Logs**: Activity audit trail (90-day retention)

**Rationale**:
- Clear workflow: Inbox → Needs_Action → Done
- HITL safety: Pending_Approval → Approved
- Audit trail: Logs folder
- Future extensibility: Plans folder ready for Silver tier

**Alternative Considered**:
- Simpler 3-folder structure (Inbox, Processing, Done): Rejected (no HITL support, no audit trail)

### 2. Action File Format

**Decision**: Markdown with YAML frontmatter

**Format**:
```markdown
---
type: file_drop
source_file: example.pdf
file_type: PDF Document
file_size: 245760
priority: normal
status: pending
---

## 📄 New File Received
[metadata and details]

## 📋 Suggested Actions
- [ ] Review file contents
- [ ] Categorize file

## 📝 Processing Notes
[Claude adds notes here]
```

**Rationale**:
- YAML frontmatter for machine-readable metadata
- Markdown body for human-readable content
- Checkboxes for task tracking
- Processing notes section for Claude's analysis

**Alternative Considered**:
- JSON files: Rejected (not human-readable in Obsidian)
- Plain text: Rejected (no structured metadata)

### 3. Watcher Architecture

**Decision**: Object-oriented design with base class and inheritance

**Classes**:
- `BaseWatcher`: Abstract base class with common functionality
  - Logging setup
  - Vault path management
  - Main run loop
  - Abstract methods: `check_for_updates()`, `create_action_file()`
- `FileSystemWatcher`: Concrete implementation for file monitoring
  - Monitors Inbox folder
  - Tracks processed files (avoid duplicates)
  - Determines priority from keywords
  - Categorizes file types by extension

**Rationale**:
- Extensibility: Easy to add GmailWatcher, WhatsAppWatcher (Silver tier)
- Code reuse: Common functionality in base class
- Testability: Each watcher can be tested independently
- Maintainability: Clear separation of concerns

**Alternative Considered**:
- Single monolithic script: Rejected (hard to extend for Silver tier)
- Functional approach: Rejected (less extensible)

### 4. Priority Detection

**Decision**: Keyword-based priority assignment

**Keywords**:
- **High Priority**: urgent, asap, critical, emergency, important, invoice, payment, bill, receipt
- **Normal Priority**: Everything else

**Rationale**:
- Simple to implement and understand
- Covers common business scenarios
- Easy to customize (user can edit keywords)
- No ML required (appropriate for Bronze tier)

**Alternative Considered**:
- ML-based classification: Rejected (over-engineering, requires training data)
- Manual priority: Rejected (defeats automation purpose)

### 5. Dashboard Design

**Decision**: Single Markdown file with sections for status, activity, and metrics

**Sections**:
- Quick Status (active tasks, pending approvals, completed today)
- Today's Priorities (checklist)
- Recent Activity (timestamped log)
- Alerts & Notifications
- Weekly Summary (metrics)
- Quick Links (navigation)

**Rationale**:
- Single source of truth
- Easy to update (Claude can edit one file)
- Human-readable in Obsidian
- Quick overview at a glance

**Alternative Considered**:
- Multiple dashboard files: Rejected (harder to maintain, fragmented view)
- Database-backed dashboard: Rejected (violates Markdown-first)

### 6. Company Handbook Structure

**Decision**: Comprehensive operating manual with clear rules and thresholds

**Sections**:
- Mission Statement
- Core Operating Principles (HITL, communication style, privacy)
- Auto-Approve Thresholds (what can be done automatically)
- Always Require Approval (what needs human review)
- Task Prioritization Rules
- Message Categorization
- Logging Requirements
- Success Metrics
- Error Handling
- Escalation Rules
- Daily Routine

**Rationale**:
- Provides clear guidance for Claude Code
- User can customize to their preferences
- Defines HITL boundaries
- Establishes consistent behavior

**Alternative Considered**:
- Hardcoded rules in Python: Rejected (not user-customizable)
- Minimal handbook: Rejected (insufficient guidance for AI)

### 7. Agent Skills Documentation

**Decision**: One .skill.md file per capability with standardized format

**Format**:
- Description
- Usage instructions
- What This Skill Does (workflow steps)
- Example Workflow
- Parameters
- Output
- Related Skills
- Notes

**Rationale**:
- Discoverability (user can browse .claude/skills/)
- Reusability (clear interface for each skill)
- Maintainability (standardized format)
- Extensibility (easy to add new skills)

**Alternative Considered**:
- Code comments only: Rejected (not discoverable)
- Single skills.md file: Rejected (harder to navigate)

### 8. Verification Strategy

**Decision**: Automated Python script that checks all components

**Checks**:
- Folder structure exists
- Core files present and non-empty
- Watcher scripts exist
- Agent Skills documented
- Test workflow completed (file in Done/)

**Rationale**:
- Automated verification (no manual checklist)
- Clear pass/fail criteria
- Easy to run (python verify_bronze.py)
- Provides detailed feedback

**Alternative Considered**:
- Manual checklist: Rejected (error-prone, time-consuming)
- Unit tests: Rejected (over-engineering for Bronze tier)

---

## Phase 2: Implementation Strategy

### Build Order

**Sequence** (retrospective documentation of what was built):

1. **Vault Structure** (Foundation)
   - Create AI_Employee_Vault directory
   - Create 7 folders (Inbox, Needs_Action, Done, etc.)
   - Create .obsidian/ configuration

2. **Core Documents** (Memory)
   - Dashboard.md with status sections
   - Company_Handbook.md with operating rules
   - README.md with setup instructions

3. **Base Watcher** (Perception Foundation)
   - BaseWatcher abstract class
   - Logging setup
   - Main run loop
   - Abstract methods

4. **File System Watcher** (Perception Implementation)
   - FileSystemWatcher class
   - Inbox monitoring
   - Action file creation
   - Priority detection
   - File type categorization

5. **Claude Code Integration** (Reasoning)
   - Test read capabilities
   - Test write capabilities
   - Test file processing workflow
   - Test Dashboard updates

6. **Agent Skills** (Interface)
   - process-actions.skill.md
   - update-dashboard.skill.md
   - start-watcher.skill.md

7. **Verification** (Quality Assurance)
   - verify_bronze.py script
   - End-to-end workflow test
   - All components verified

### Integration Points

**Watcher → Vault**:
- Watcher writes action files to Needs_Action/
- Watcher logs activity to Logs/FileSystemWatcher.log

**Claude Code → Vault**:
- Reads action files from Needs_Action/
- Writes processing notes to action files
- Moves completed files to Done/
- Updates Dashboard.md with activity

**User → Vault**:
- Drops files in Inbox/
- Reviews Dashboard.md in Obsidian
- Reads Company_Handbook.md for rules
- Approves actions by moving files to Approved/

### Error Handling Strategy

**Watcher Errors**:
- Log error with full context
- Continue monitoring (don't crash)
- Skip problematic files (don't block queue)

**Claude Code Errors**:
- Log error in action file
- Create ERROR_ prefixed file in Needs_Action/
- Alert user via Dashboard

**File System Errors**:
- Retry transient errors (3 attempts)
- Alert user for permanent errors
- Never delete files (quarantine instead)

### Testing Approach

**Manual Testing**:
1. Drop test file in Inbox
2. Verify action file created in Needs_Action
3. Process with Claude Code
4. Verify file moved to Done
5. Verify Dashboard updated

**Automated Verification**:
- Run verify_bronze.py
- Check all components present
- Verify test workflow completed

---

## Phase 3: Deployment & Operations

### Installation Steps

1. Install prerequisites (Python 3.13+, Obsidian, Claude Code)
2. Clone/download AI_Employee_Vault
3. Install Python dependencies: `pip install -r requirements.txt`
4. Open vault in Obsidian
5. Customize Company_Handbook.md
6. Start watcher: `python filesystem_watcher.py .`

### Operational Considerations

**Watcher Management**:
- Manual start/stop (Bronze tier)
- Check interval: 10 seconds (configurable)
- Logs to Logs/FileSystemWatcher.log

**Maintenance**:
- Archive Done/ folder weekly (manual)
- Review Logs/ monthly
- Update Company_Handbook.md as needed

**Backup Strategy**:
- Vault is just files (easy to backup)
- Use Git for version control
- Copy vault folder for backup

### Monitoring

**Health Checks**:
- Watcher running? (check process)
- Files being processed? (check Needs_Action/)
- Dashboard updated? (check timestamp)

**Metrics**:
- Files processed per day
- Average processing time
- Error rate

---

## Risks & Mitigations

### Risk 1: Watcher Crashes
**Impact**: New files not detected
**Mitigation**:
- Robust error handling in watcher
- Watchdog process (Silver tier)
- Manual restart instructions in README

### Risk 2: Obsidian Vault Corruption
**Impact**: Data loss
**Mitigation**:
- Files are plain text (easy to recover)
- Git version control
- Regular backups

### Risk 3: Claude Code Misinterprets Rules
**Impact**: Incorrect processing
**Mitigation**:
- Clear Company Handbook rules
- HITL approval for sensitive actions
- Audit logging

### Risk 4: File System Permissions
**Impact**: Watcher can't read/write
**Mitigation**:
- Check permissions in verify_bronze.py
- Clear error messages
- Troubleshooting guide in README

---

## Success Criteria Mapping

| Success Criterion | Implementation | Verification |
|-------------------|----------------|--------------|
| SC-001: Vault structure | 7 folders + core docs | verify_bronze.py |
| SC-002: File detection < 10s | Watcher check interval | Manual test |
| SC-003: Complete metadata | Action file format | Manual review |
| SC-004: Claude can read | File operations tested | Manual test |
| SC-005: Claude can write | File operations tested | Manual test |
| SC-006: Task completion | End-to-end workflow | Manual test |
| SC-007: Dashboard accuracy | Update logic | Manual review |
| SC-008: Skills documented | 3 .skill.md files | verify_bronze.py |
| SC-009: End-to-end workflow | Full test completed | verify_bronze.py |
| SC-010: Reliable operation | Error handling | Extended testing |
| SC-011: Activity logged | Logs/ folder | Manual review |
| SC-012: Verification script | verify_bronze.py | Script execution |

---

## Future Considerations (Silver Tier)

**Not Implemented in Bronze** (documented for planning):
- Gmail Watcher (requires Google API setup)
- MCP email server (requires Node.js MCP)
- Automated approval execution (requires orchestrator)
- Scheduling (requires cron/Task Scheduler)
- LinkedIn integration (requires API or browser automation)
- Multi-step planning (requires Plan.md workflow)

**Architecture Ready For**:
- Additional watchers (base class extensible)
- MCP server integration (folder structure supports)
- Approval workflow (Pending_Approval/Approved folders exist)
- Planning system (Plans/ folder exists)

---

## Conclusion

Bronze tier implementation successfully establishes the foundational infrastructure for a Personal AI Employee. The architecture is simple, maintainable, and extensible. All constitution principles are followed. The system is ready for Silver tier enhancements.

**Status**: ✅ Implementation Complete & Verified
**Next Phase**: Silver Tier Planning (Gmail, MCP, Approvals, Scheduling)
