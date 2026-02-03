# Feature Specification: Bronze Tier Foundation - AI Employee Automation

**Feature Branch**: `001-bronze-tier-foundation`
**Created**: 2026-02-03
**Status**: Completed
**Input**: User description: "Document the completed Bronze tier implementation: Obsidian vault setup, File System Watcher, Claude Code integration, and Agent Skills for basic AI Employee automation"

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Set Up AI Employee Workspace (Priority: P1)

As a user, I need a centralized workspace where my AI Employee can store information, track tasks, and maintain operational state, so that all automation activities are organized and accessible.

**Why this priority**: This is the foundational infrastructure - nothing else can work without a proper workspace. It's the "office" where the AI Employee operates.

**Independent Test**: Can be fully tested by opening the workspace in Obsidian, verifying all folders exist, and confirming Dashboard and Company Handbook are readable and properly formatted.

**Acceptance Scenarios**:

1. **Given** I have installed Obsidian, **When** I open the AI_Employee_Vault folder as a vault, **Then** I see a properly structured workspace with Dashboard.md as the main overview
2. **Given** the vault is open, **When** I navigate through folders, **Then** I see Inbox, Needs_Action, Done, Pending_Approval, Approved, Plans, and Logs folders
3. **Given** I open Dashboard.md, **When** I review the content, **Then** I see current status, active tasks count, recent activity log, and quick links to other sections
4. **Given** I open Company_Handbook.md, **When** I review the content, **Then** I see clear operating principles, approval rules, priority definitions, and communication guidelines

---

### User Story 2 - Automatic File Detection and Processing (Priority: P1)

As a user, I need the AI Employee to automatically detect when I drop files into the Inbox folder and create actionable task items, so that I don't have to manually notify the system about new work.

**Why this priority**: This is the core automation capability - the "nervous system" that allows the AI Employee to perceive new work without manual intervention.

**Independent Test**: Can be fully tested by starting the watcher, dropping a test file in Inbox, and verifying an action file appears in Needs_Action within the check interval.

**Acceptance Scenarios**:

1. **Given** the File System Watcher is running, **When** I drop a document into the Inbox folder, **Then** an action file is created in Needs_Action within 10 seconds
2. **Given** an action file is created, **When** I open it, **Then** I see file metadata (name, type, size), priority level, suggested actions checklist, and processing notes section
3. **Given** multiple files are dropped, **When** the watcher processes them, **Then** each file gets its own uniquely named action file with timestamp
4. **Given** a file with urgent keywords in the name, **When** the watcher processes it, **Then** the action file is marked with high priority

---

### User Story 3 - AI Processing and Task Completion (Priority: P1)

As a user, I need Claude Code to read action items, add processing notes, categorize them, and move completed tasks to the Done folder, so that the AI Employee can actually process work autonomously.

**Why this priority**: This demonstrates the "brain" of the AI Employee - the reasoning capability that turns detected items into completed work.

**Independent Test**: Can be fully tested by having Claude Code read a file from Needs_Action, update it with processing notes, and move it to Done, then verifying the Dashboard reflects the change.

**Acceptance Scenarios**:

1. **Given** an action file exists in Needs_Action, **When** Claude Code processes it, **Then** the file is updated with processing notes, categorization, and completion timestamp
2. **Given** a task is processed, **When** Claude Code completes it, **Then** the file is moved from Needs_Action to Done folder
3. **Given** a task is completed, **When** I check the Dashboard, **Then** I see the completed task count incremented and activity logged in Recent Activity section
4. **Given** Claude Code is processing, **When** it reads the Company Handbook, **Then** it follows the defined rules for prioritization, categorization, and approval requirements

---

### User Story 4 - Reusable Automation Skills (Priority: P2)

As a user, I need the AI Employee's capabilities packaged as reusable Agent Skills, so that I can easily invoke specific automation functions and understand what each skill does.

**Why this priority**: This provides a clean interface to the AI Employee's capabilities and makes the system extensible for future enhancements.

**Independent Test**: Can be fully tested by reviewing the .claude/skills directory, reading each skill documentation, and verifying the skills describe clear inputs, outputs, and workflows.

**Acceptance Scenarios**:

1. **Given** the skills directory exists, **When** I list the skills, **Then** I see process-actions, update-dashboard, and start-watcher skills documented
2. **Given** I open a skill file, **When** I review the documentation, **Then** I see clear description, usage instructions, workflow steps, parameters, and related skills
3. **Given** a skill is documented, **When** I follow its usage instructions, **Then** I can successfully invoke the described functionality
4. **Given** multiple skills exist, **When** I review them, **Then** I understand how they work together to form a complete automation workflow

---

### Edge Cases

- What happens when the Inbox folder contains hidden files or system files? (System should ignore them)
- What happens when duplicate files with the same name are dropped? (Watcher tracks processed files and ignores duplicates)
- What happens when Claude Code tries to process a corrupted or unreadable file? (Should log error and create error notification in Needs_Action)
- What happens when the Done folder accumulates too many files? (Manual archival for Bronze tier; automated retention for Silver tier)
- What happens when the watcher crashes or stops running? (Manual restart for Bronze tier; watchdog process for Silver tier)
- What happens when multiple action files need processing simultaneously? (Process sequentially in Bronze tier; parallel processing in Silver tier)

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: System MUST provide a local Markdown-based workspace (Obsidian vault) with persistent storage for all AI Employee data
- **FR-002**: System MUST include a Dashboard that displays current status, active task count, pending approvals, completed tasks, and recent activity log
- **FR-003**: System MUST include a Company Handbook that defines operating principles, approval thresholds, priority rules, and communication guidelines
- **FR-004**: System MUST provide folder structure including Inbox (entry point), Needs_Action (pending tasks), Done (completed), Pending_Approval (awaiting human review), Approved (ready for execution), Plans (multi-step strategies), and Logs (activity audit trail)
- **FR-005**: System MUST include a File System Watcher that continuously monitors the Inbox folder for new files
- **FR-006**: Watcher MUST detect new files within a configurable check interval (default 10 seconds)
- **FR-007**: Watcher MUST create action files in Needs_Action folder with metadata including file name, type, size, timestamp, priority, and suggested actions
- **FR-008**: Watcher MUST determine file priority based on filename keywords (urgent, asap, critical, invoice, payment = high priority)
- **FR-009**: Watcher MUST categorize file types by extension (documents, spreadsheets, images, archives, data files)
- **FR-010**: Watcher MUST log all activity to a dedicated log file with timestamps and event details
- **FR-011**: System MUST enable Claude Code to read files from any vault folder
- **FR-012**: System MUST enable Claude Code to write and edit files in the vault
- **FR-013**: Claude Code MUST be able to process action files by adding processing notes, categorization, and completion status
- **FR-014**: Claude Code MUST be able to move completed tasks from Needs_Action to Done folder
- **FR-015**: Claude Code MUST be able to update Dashboard with current metrics and activity logs
- **FR-016**: System MUST provide Agent Skills documentation for core capabilities (process-actions, update-dashboard, start-watcher)
- **FR-017**: Each Agent Skill MUST include description, usage instructions, workflow steps, parameters, output format, and related skills
- **FR-018**: System MUST support end-to-end workflow: file drop → detection → action creation → processing → completion → dashboard update
- **FR-019**: System MUST maintain audit trail of all actions in Logs folder
- **FR-020**: System MUST be compatible with Windows, Mac, and Linux operating systems

### Key Entities

- **Vault**: The Obsidian workspace containing all AI Employee data, organized into folders with specific purposes
- **Dashboard**: Central overview document showing current status, metrics, activity log, and quick navigation links
- **Company Handbook**: Operating manual defining rules, thresholds, priorities, and guidelines for AI Employee behavior
- **Action File**: Markdown document in Needs_Action folder representing a task to be processed, containing metadata, suggested actions, and processing notes
- **Watcher**: Background process that monitors Inbox folder and creates action files when new items are detected
- **Agent Skill**: Documented capability of the AI Employee, describing a specific automation function with usage instructions

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: User can open the AI_Employee_Vault in Obsidian and see a fully structured workspace with all required folders and documents
- **SC-002**: File System Watcher detects new files dropped in Inbox within 10 seconds and creates corresponding action files
- **SC-003**: Action files contain complete metadata (file name, type, size, priority, timestamp) and suggested actions checklist
- **SC-004**: Claude Code can successfully read any file in the vault and extract its content
- **SC-005**: Claude Code can create new files and edit existing files in the vault
- **SC-006**: Claude Code can process an action file by adding notes, categorization, and moving it to Done folder
- **SC-007**: Dashboard accurately reflects current system state (active tasks, completed tasks, recent activity)
- **SC-008**: All three Agent Skills (process-actions, update-dashboard, start-watcher) are documented with clear usage instructions
- **SC-009**: End-to-end workflow completes successfully: file drop → detection → action creation → processing → completion → dashboard update
- **SC-010**: System operates reliably for continuous periods (watcher runs without crashes for extended sessions)
- **SC-011**: All activity is logged with timestamps and can be reviewed for audit purposes
- **SC-012**: User can verify Bronze tier completion by running verification script that checks all components

## Assumptions *(mandatory)*

- User has Obsidian installed and knows how to open a folder as a vault
- User has Python 3.13+ installed for running watcher scripts
- User has Claude Code installed and configured
- User has basic command-line familiarity for starting watcher scripts
- Files dropped in Inbox are standard file types (documents, images, data files) not executables or malware
- User will manually start the watcher script (automated startup is Silver tier requirement)
- User will manually process action files with Claude Code (fully autonomous processing is Gold tier requirement)
- Vault remains on local filesystem (cloud sync is Platinum tier requirement)
- Single user operates the system (multi-user is not in scope)
- English language is used for all documents and file names

## Out of Scope *(mandatory)*

- Automated email monitoring (Gmail Watcher is Silver tier)
- Automated social media posting (LinkedIn integration is Silver tier)
- MCP servers for external actions (Silver tier requirement)
- Automated approval workflow execution (Silver tier requirement)
- Scheduled task execution via cron/Task Scheduler (Silver tier requirement)
- Multi-step planning with Plan.md files (Silver tier requirement)
- WhatsApp monitoring (Silver tier optional)
- Cloud deployment (Platinum tier requirement)
- Odoo accounting integration (Gold tier requirement)
- Multi-agent coordination (Platinum tier requirement)
- Real-time notifications or alerts
- Mobile app or web interface
- Database integration
- API endpoints
- User authentication or multi-user support

## Dependencies *(if applicable)*

### External Dependencies

- **Obsidian**: Markdown editor and knowledge base application (free, cross-platform)
- **Python 3.13+**: Runtime for watcher scripts
- **watchdog library**: Python package for file system monitoring (pip installable)
- **python-dotenv library**: Python package for environment variable management (pip installable)
- **Claude Code**: AI-powered development tool for file processing and automation
- **Git**: Version control for tracking changes (optional but recommended)

### Internal Dependencies

- base_watcher.py must be created before filesystem_watcher.py (inheritance dependency)
- Vault folder structure must exist before watcher can create action files
- Dashboard.md and Company_Handbook.md must exist before Claude Code can reference them
- Agent Skills documentation depends on implemented functionality

## Open Questions *(if any)*

None - Bronze tier requirements are well-defined and implementation is complete.

## Notes

This specification documents the **completed** Bronze tier implementation. All requirements have been met and verified through testing. The system is operational and ready for use.

**Verification Status**: ✅ All components verified via verify_bronze.py script

**Next Steps**: User can proceed to Silver tier implementation, which adds Gmail integration, MCP servers, approval workflows, planning capabilities, LinkedIn posting, and scheduled execution.
