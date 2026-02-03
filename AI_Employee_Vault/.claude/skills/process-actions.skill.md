# Process Action Items Skill

## Description
Processes files from the Needs_Action folder, reviews their content, categorizes them, and moves completed items to the Done folder.

## Usage
```
/process-actions
```

## What This Skill Does

1. **Scans Needs_Action Folder**
   - Lists all pending action files
   - Identifies priority levels
   - Sorts by urgency

2. **Processes Each Item**
   - Reads the action file content
   - Reviews the original file if referenced
   - Adds processing notes
   - Updates status and checkboxes
   - Categorizes (Personal/Business/Administrative)

3. **Completes Tasks**
   - Marks all suggested actions as complete
   - Adds timestamp and processor info
   - Moves to Done folder
   - Updates Dashboard with activity

4. **Updates Dashboard**
   - Increments completed tasks counter
   - Logs activity in Recent Activity section
   - Updates last processed timestamp

## Example Workflow

```
User: /process-actions

AI Employee:
1. Found 2 items in Needs_Action/
2. Processing FILE_test_document_2026-02-03.md
   - Category: Administrative
   - Priority: Normal
   - Action: Reviewed and archived
3. Processing EMAIL_client_request_2026-02-03.md
   - Category: Business
   - Priority: High
   - Action: Draft response created (pending approval)
4. Updated Dashboard
5. Moved 1 completed item to Done/
```

## Parameters
- None (processes all items in Needs_Action/)

## Output
- Summary of processed items
- Updated Dashboard
- Completed items moved to Done/

## Related Skills
- `/update-dashboard` - Updates the Dashboard manually
- `/start-watcher` - Starts the File System Watcher

## Notes
- Items requiring approval are moved to Pending_Approval/ instead of Done/
- High priority items are processed first
- All actions are logged in Logs/ folder
