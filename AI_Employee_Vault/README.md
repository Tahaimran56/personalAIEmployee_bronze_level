# AI Employee Vault - Setup Guide

## 📁 Vault Structure

```
AI_Employee_Vault/
├── .obsidian/           # Obsidian configuration
├── Inbox/               # New items to be processed
├── Needs_Action/        # Tasks requiring attention
├── Done/                # Completed tasks (archive)
├── Pending_Approval/    # Actions awaiting human approval
├── Approved/            # Approved actions ready for execution
├── Plans/               # Task plans and strategies
├── Logs/                # Activity logs
├── Dashboard.md         # Main overview and status
└── Company_Handbook.md  # Rules and operating procedures
```

## 🎯 Purpose of Each Folder

### Inbox/
- **Purpose:** Entry point for all new items
- **Source:** Watcher scripts drop files here
- **Lifecycle:** Items are processed and moved to Needs_Action or archived

### Needs_Action/
- **Purpose:** Tasks that require AI processing
- **Naming:** `TYPE_description_timestamp.md` (e.g., `EMAIL_client_request_2026-02-03.md`)
- **Lifecycle:** AI processes and either completes or escalates to Pending_Approval

### Done/
- **Purpose:** Archive of completed tasks
- **Retention:** Keep for 30 days, then archive
- **Format:** Original files moved here with completion timestamp

### Pending_Approval/
- **Purpose:** Actions that require human approval before execution
- **Critical for:** Emails, payments, social posts, deletions
- **Action:** Human reviews and moves to Approved/ or rejects

### Approved/
- **Purpose:** Approved actions ready for execution
- **Lifecycle:** Orchestrator executes and moves to Done/

### Plans/
- **Purpose:** Multi-step task plans created by Claude
- **Format:** `PLAN_description_timestamp.md`
- **Contains:** Objectives, steps, dependencies, approval requirements

### Logs/
- **Purpose:** Audit trail of all actions
- **Format:** `YYYY-MM-DD.json` (one file per day)
- **Retention:** 90 days minimum

## 🚀 Quick Start

### 1. Open in Obsidian
1. Launch Obsidian
2. Click "Open folder as vault"
3. Select `AI_Employee_Vault` directory
4. You should see Dashboard.md and Company_Handbook.md

### 2. Verify Claude Code Access
```bash
cd AI_Employee_Vault
claude --version
```

### 3. Test Read/Write
Claude Code should be able to:
- Read Dashboard.md and Company_Handbook.md
- Write new files to Needs_Action/
- Update Dashboard.md with activity

### 4. Customize Company_Handbook.md
Edit the handbook to match your:
- Working hours
- Communication preferences
- Approval thresholds
- Priority rules

## 📋 Bronze Tier Checklist

- [x] Vault created with proper folder structure
- [x] Dashboard.md created
- [x] Company_Handbook.md created
- [x] Obsidian configuration set up
- [x] Claude Code can read from vault
- [ ] Claude Code can write to vault (test pending)
- [ ] First watcher script created
- [ ] End-to-end workflow tested
- [ ] Functionality converted to Agent Skills

## 🔧 Next Steps

1. **Choose a Watcher Type:**
   - Option A: File System Watcher (simpler, no API setup)
   - Option B: Gmail Watcher (requires Google API credentials)

2. **Create the Watcher Script:**
   - Set up Python environment
   - Install dependencies
   - Configure watcher to monitor and create files in Needs_Action/

3. **Test the Workflow:**
   - Watcher detects new item → creates file in Needs_Action/
   - Claude Code reads file → processes → creates plan
   - Human approves → action executed → moved to Done/

4. **Convert to Agent Skills:**
   - Package watcher logic as a skill
   - Package processing logic as a skill
   - Document skill usage

## 📖 Key Documents

### Dashboard.md
Your command center. Check this daily for:
- Active tasks count
- Pending approvals
- Recent activity
- Alerts and notifications

### Company_Handbook.md
Your AI Employee's operating manual. Defines:
- What can be done automatically
- What requires approval
- Communication style
- Priority rules
- Error handling

## 🔒 Security Notes

- All data stays local (local-first architecture)
- No credentials stored in vault
- Use .env files for API keys (add to .gitignore)
- Sensitive data redacted in logs
- Human approval required for critical actions

## 🆘 Troubleshooting

**Obsidian doesn't recognize the vault:**
- Ensure .obsidian/ folder exists
- Check folder permissions
- Try "Open folder as vault" instead of "Open vault"

**Claude Code can't access files:**
- Verify you're in the correct directory
- Check file permissions
- Use absolute paths if needed

**Watcher not creating files:**
- Check watcher script is running
- Verify folder paths are correct
- Check logs for errors

## 📚 Resources

- Hackathon Guide: `hackathonread.md`
- Obsidian Docs: https://help.obsidian.md
- Claude Code Docs: https://agentfactory.panaversity.org/docs/AI-Tool-Landscape/claude-code-features-and-workflows
- MCP Docs: https://modelcontextprotocol.io

---

**Vault Version:** 1.0
**Created:** 2026-02-03
**Bronze Tier Status:** Setup Complete ✅
