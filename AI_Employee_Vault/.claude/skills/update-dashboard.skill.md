# Update Dashboard Skill

## Description
Updates the AI Employee Dashboard with current status, activity logs, and metrics.

## Usage
```
/update-dashboard
```

## What This Skill Does

1. **Counts Current Status**
   - Active tasks in Needs_Action/
   - Pending approvals in Pending_Approval/
   - Completed tasks in Done/ (today)
   - Total items processed

2. **Updates Status Section**
   - Current date
   - Task counters
   - Setup progress percentage
   - System health status

3. **Logs Recent Activity**
   - Timestamps all activities
   - Categorizes by type (file processed, email sent, etc.)
   - Includes brief descriptions
   - Maintains chronological order

4. **Calculates Weekly Summary**
   - Tasks completed this week
   - Messages processed
   - Actions taken
   - Average response time

## Example Output

```
Dashboard Updated Successfully!

Current Status:
- Active Tasks: 3
- Pending Approvals: 1
- Completed Today: 5
- System Status: Operational

Recent Activity Added:
- 2026-02-03 14:30 - Processed 2 email requests
- 2026-02-03 14:15 - File watcher detected new document
- 2026-02-03 14:00 - Dashboard updated
```

## Parameters
- None (automatically scans all folders)

## Output
- Updated Dashboard.md
- Summary of changes
- Current metrics

## Related Skills
- `/process-actions` - Process pending action items
- `/weekly-summary` - Generate weekly report

## Notes
- Runs automatically after processing actions
- Can be called manually anytime
- Preserves historical activity logs
- Updates timestamp at bottom of Dashboard
