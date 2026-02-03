# Start Watcher Skill

## Description
Starts the File System Watcher to monitor the Inbox folder for new files and automatically create action items.

## Usage
```
/start-watcher [interval]
```

## What This Skill Does

1. **Initializes Watcher**
   - Sets up monitoring on Inbox folder
   - Configures check interval (default: 10 seconds)
   - Initializes logging system
   - Creates necessary directories if missing

2. **Monitors for New Files**
   - Continuously scans Inbox folder
   - Detects new files (not directories)
   - Ignores hidden/system files
   - Tracks processed files to avoid duplicates

3. **Creates Action Items**
   - Generates action file in Needs_Action/
   - Includes file metadata (size, type, timestamp)
   - Determines priority based on filename keywords
   - Categorizes file type by extension
   - Adds suggested actions checklist

4. **Logs Activity**
   - Records all detected files
   - Logs action file creation
   - Writes to Logs/FileSystemWatcher.log
   - Console output for monitoring

## Example Usage

```bash
# Start with default 10-second interval
/start-watcher

# Start with custom 30-second interval
/start-watcher 30
```

## Example Output

```
============================================================
File System Watcher Started
============================================================
Vault: C:\Users\Dell\Desktop\hackathon0\AI_Employee_Vault
Inbox: C:\Users\Dell\Desktop\hackathon0\AI_Employee_Vault\Inbox
Check interval: 10 seconds

Drop files into the Inbox folder to test!
Press Ctrl+C to stop

============================================================

2026-02-03 12:39:34 - INFO - Found 1 new items to process
2026-02-03 12:39:34 - INFO - Created action file for: test_document.txt
2026-02-03 12:39:34 - INFO - Created action file: FILE_test_document_2026-02-03_12-39-34.md
```

## Parameters
- `interval` (optional): Check interval in seconds (default: 10)

## Files Created
- `Needs_Action/FILE_<filename>_<timestamp>.md` - Action item for each detected file
- `Logs/FileSystemWatcher.log` - Activity log

## Priority Detection
The watcher automatically assigns priority based on filename keywords:

**High Priority:**
- urgent, asap, critical, emergency, important
- invoice, payment, bill, receipt

**Normal Priority:**
- All other files

## Supported File Types
- Text documents (.txt, .md)
- PDF documents (.pdf)
- Word documents (.doc, .docx)
- Excel spreadsheets (.xls, .xlsx)
- CSV data (.csv)
- Images (.jpg, .jpeg, .png, .gif)
- Archives (.zip, .rar)
- JSON/XML data (.json, .xml)

## Related Skills
- `/process-actions` - Process the created action items
- `/update-dashboard` - Update Dashboard with watcher status

## Notes
- Watcher runs continuously until stopped (Ctrl+C)
- Files remain in Inbox until manually moved/deleted
- Action files are created immediately upon detection
- Duplicate files are ignored (based on filename)
- For production use, consider running as a background service

## Troubleshooting

**Watcher not detecting files:**
- Verify Inbox folder exists
- Check file permissions
- Ensure files are not hidden
- Review FileSystemWatcher.log for errors

**Unicode errors on Windows:**
- Script automatically handles UTF-8 encoding
- If issues persist, check console encoding settings
