# Bronze Tier Demo Video Script (5-10 minutes)

**Target Duration**: 7-8 minutes
**Purpose**: Showcase Bronze tier functionality and architecture

---

## Introduction (30 seconds)

**[Screen: GitHub Repository]**

"Hi, I'm presenting my Bronze Tier submission for the Personal AI Employee Hackathon. This project builds a foundational AI Employee using Claude Code, Obsidian, and a local-first architecture. Let me show you what it can do."

---

## Part 1: Architecture Overview (1 minute)

**[Screen: README.md - Architecture Diagram]**

"The Bronze tier implements three core components:

1. **Obsidian Vault** - The 'memory' where all data lives as Markdown files
2. **File System Watcher** - The 'nervous system' that detects new work automatically
3. **Claude Code** - The 'brain' that processes tasks and makes decisions

Everything follows a local-first architecture - your data never leaves your machine."

**[Screen: Project Structure in VS Code]**

"Here's the folder structure. We have:
- Inbox for new files
- Needs_Action for pending tasks
- Done for completed work
- And folders for approvals, plans, and logs"

---

## Part 2: SpecifyPlus Documentation (1.5 minutes)

**[Screen: specs/001-bronze-tier-foundation/]**

"This project follows the SpecifyPlus methodology - a systematic approach to software development.

**[Open constitution.md]**
First, we have a Constitution with 7 core principles including Local-First Architecture, Human-in-the-Loop Safety, and Markdown-First Documentation.

**[Open spec.md]**
The Specification defines WHAT to build - 4 user stories, 20 functional requirements, and 12 measurable success criteria.

**[Open plan.md]**
The Implementation Plan defines HOW to build it - 594 lines of architecture decisions and design rationale.

**[Open tasks.md]**
And the Tasks document defines the STEPS - 49 tasks with clear acceptance criteria.

This systematic approach ensures quality and maintainability."

---

## Part 3: Live Demo - File System Watcher (2 minutes)

**[Screen: Terminal + File Explorer side by side]**

"Let me show you the core automation. I'll start the File System Watcher."

**[Terminal]**
```bash
cd AI_Employee_Vault
python filesystem_watcher.py .
```

**[Show watcher output]**
"The watcher is now monitoring the Inbox folder every 10 seconds."

**[File Explorer]**
"Now I'll drop a test file into the Inbox."

**[Create file: urgent_client_proposal.pdf]**
"Notice the filename has 'urgent' - the watcher will detect this as high priority."

**[Wait 5-10 seconds, show watcher log]**
"Within 10 seconds, the watcher detected the file and created an action item."

**[Open Needs_Action folder]**
"Here's the action file it created. Let me open it."

**[Open action file in Obsidian]**
"The action file includes:
- File metadata (name, type, size)
- Priority level (HIGH because of 'urgent' keyword)
- Suggested actions checklist
- Processing notes section for Claude Code"

---

## Part 4: Claude Code Integration (2 minutes)

**[Screen: Obsidian with action file open]**

"Now let me show Claude Code processing this task."

**[Screen: Claude Code terminal]**
"I'll ask Claude Code to process the action file."

**[Type/Show]**
"Read the action file in Needs_Action, add processing notes about the client proposal, categorize it as Business/High Priority, and move it to Done when complete."

**[Show Claude Code reading file]**
"Claude Code reads the file..."

**[Show Claude Code adding notes]**
"...adds processing notes with categorization..."

**[Show file being moved to Done]**
"...and moves the completed task to the Done folder."

**[Open Dashboard.md]**
"The Dashboard is automatically updated with the activity log and completed task count."

---

## Part 5: Agent Skills (1 minute)

**[Screen: .claude/skills/ folder]**

"All functionality is packaged as Agent Skills for reusability.

**[Open process-actions.skill.md]**
This skill processes all pending action items.

**[Open update-dashboard.skill.md]**
This skill updates the Dashboard with current metrics.

**[Open start-watcher.skill.md]**
And this skill starts the File System Watcher.

Each skill has clear documentation with usage instructions, workflow steps, and examples."

---

## Part 6: Verification (1 minute)

**[Screen: Terminal]**

"Bronze tier includes automated verification."

**[Run verification script]**
```bash
python verify_bronze.py .
```

**[Show output]**
"The script checks:
- ✓ Folder structure (9 folders)
- ✓ Core files (Dashboard, Handbook)
- ✓ Watcher scripts
- ✓ Agent Skills (3 documented)
- ✓ Test workflow (end-to-end tested)

All 5 checks passed!"

---

## Part 7: Company Handbook (30 seconds)

**[Screen: Company_Handbook.md in Obsidian]**

"The Company Handbook defines operating rules for the AI Employee:
- What can be done automatically
- What requires human approval
- Priority levels and categorization
- Communication style and error handling

This ensures the AI follows your preferences and maintains safety."

---

## Conclusion (30 seconds)

**[Screen: README.md]**

"To summarize, Bronze tier delivers:
- ✅ Automatic file detection and processing
- ✅ Claude Code integration for AI reasoning
- ✅ Complete SpecifyPlus documentation (1,526 lines)
- ✅ 3 Agent Skills for reusable automation
- ✅ Local-first, privacy-focused architecture
- ✅ All 5 Bronze tier requirements met

The foundation is ready for Silver tier enhancements like Gmail integration, MCP servers, and automated approvals.

Thank you for watching!"

**[Screen: GitHub repository URL]**
https://github.com/Tahaimran56/personalAIEmployee_bronze_level

---

## Recording Tips

1. **Screen Setup**: Use screen recording software (OBS, Loom, or QuickTime)
2. **Resolution**: 1920x1080 or 1280x720
3. **Audio**: Clear microphone, minimize background noise
4. **Pace**: Speak clearly, not too fast
5. **Preparation**:
   - Have all files ready
   - Test the watcher before recording
   - Prepare the test file in advance
   - Have Obsidian and terminals open
6. **Editing**:
   - Cut any mistakes or long pauses
   - Add text overlays for key points if needed
   - Keep final video 5-10 minutes

## What to Show

**Must Show**:
- ✅ File System Watcher detecting files
- ✅ Action file creation with metadata
- ✅ Claude Code processing
- ✅ Dashboard updates
- ✅ Verification script passing

**Nice to Have**:
- SpecifyPlus documentation
- Agent Skills
- Company Handbook
- Project structure

## Upload

- **YouTube** (unlisted or public)
- **Loom** (shareable link)
- **Google Drive** (public link)

Include video link in submission form.
