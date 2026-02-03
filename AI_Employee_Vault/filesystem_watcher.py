"""
File System Watcher
Monitors the Inbox folder for new files and creates action items
"""
from pathlib import Path
from datetime import datetime
import shutil
from base_watcher import BaseWatcher


class FileSystemWatcher(BaseWatcher):
    """Watches Inbox folder for new files and creates action items"""

    def __init__(self, vault_path: str, check_interval: int = 30):
        super().__init__(vault_path, check_interval)
        self.inbox = self.vault_path / 'Inbox'
        self.inbox.mkdir(parents=True, exist_ok=True)
        self.processed_files = set()

        self.logger.info(f'Monitoring inbox at: {self.inbox}')

    def check_for_updates(self) -> list:
        """Check Inbox folder for new files"""
        new_files = []

        # Get all files in Inbox (not directories)
        for file_path in self.inbox.iterdir():
            if file_path.is_file() and file_path.name not in self.processed_files:
                # Skip hidden files and system files
                if not file_path.name.startswith('.'):
                    new_files.append(file_path)
                    self.processed_files.add(file_path.name)

        return new_files

    def create_action_file(self, file_path: Path) -> Path:
        """Create action file in Needs_Action folder"""
        timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
        file_size = file_path.stat().st_size
        file_ext = file_path.suffix

        # Determine file type and priority
        file_type = self._determine_file_type(file_ext)
        priority = self._determine_priority(file_path)

        # Create action file content
        content = f"""---
type: file_drop
source_file: {file_path.name}
file_type: {file_type}
file_size: {file_size} bytes
received: {datetime.now().isoformat()}
priority: {priority}
status: pending
---

## 📄 New File Received

**File Name:** {file_path.name}
**File Type:** {file_type}
**Size:** {self._format_size(file_size)}
**Location:** Inbox/{file_path.name}

## 📋 Suggested Actions

- [ ] Review file contents
- [ ] Categorize file (Personal/Business/Administrative)
- [ ] Determine next steps
- [ ] Move to appropriate folder or archive

## 🔍 File Details

**Extension:** {file_ext if file_ext else 'None'}
**Created:** {timestamp}

## 📝 Processing Notes

*Add notes here about how this file should be handled*

---

**Original file location:** `Inbox/{file_path.name}`
**Action file created:** {datetime.now().isoformat()}
"""

        # Create action file
        action_filename = f'FILE_{file_path.stem}_{timestamp}.md'
        action_filepath = self.needs_action / action_filename
        action_filepath.write_text(content, encoding='utf-8')

        self.logger.info(f'Created action file for: {file_path.name}')

        # Optionally copy the original file to a processing folder
        # (keeping it in Inbox for now, can be moved after processing)

        return action_filepath

    def _determine_file_type(self, extension: str) -> str:
        """Determine file type from extension"""
        extension = extension.lower()

        type_mapping = {
            '.txt': 'Text Document',
            '.md': 'Markdown Document',
            '.pdf': 'PDF Document',
            '.doc': 'Word Document',
            '.docx': 'Word Document',
            '.xls': 'Excel Spreadsheet',
            '.xlsx': 'Excel Spreadsheet',
            '.csv': 'CSV Data',
            '.jpg': 'Image',
            '.jpeg': 'Image',
            '.png': 'Image',
            '.gif': 'Image',
            '.zip': 'Archive',
            '.rar': 'Archive',
            '.json': 'JSON Data',
            '.xml': 'XML Data',
        }

        return type_mapping.get(extension, 'Unknown')

    def _determine_priority(self, file_path: Path) -> str:
        """Determine priority based on file name keywords"""
        filename_lower = file_path.name.lower()

        # Check for urgent keywords
        urgent_keywords = ['urgent', 'asap', 'critical', 'emergency', 'important']
        if any(keyword in filename_lower for keyword in urgent_keywords):
            return 'high'

        # Check for invoice/payment keywords
        financial_keywords = ['invoice', 'payment', 'bill', 'receipt']
        if any(keyword in filename_lower for keyword in financial_keywords):
            return 'high'

        return 'normal'

    def _format_size(self, size_bytes: int) -> str:
        """Format file size in human-readable format"""
        for unit in ['B', 'KB', 'MB', 'GB']:
            if size_bytes < 1024.0:
                return f"{size_bytes:.1f} {unit}"
            size_bytes /= 1024.0
        return f"{size_bytes:.1f} TB"


if __name__ == '__main__':
    import sys
    import io

    # Set UTF-8 encoding for Windows console
    if sys.platform == 'win32':
        sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

    # Get vault path from command line or use default
    vault_path = sys.argv[1] if len(sys.argv) > 1 else '.'

    # Create and run watcher
    watcher = FileSystemWatcher(vault_path, check_interval=10)

    print(f"\n{'='*60}")
    print("File System Watcher Started")
    print(f"{'='*60}")
    print(f"Vault: {watcher.vault_path.absolute()}")
    print(f"Inbox: {watcher.inbox.absolute()}")
    print(f"Check interval: {watcher.check_interval} seconds")
    print(f"\nDrop files into the Inbox folder to test!")
    print(f"Press Ctrl+C to stop\n")
    print(f"{'='*60}\n")

    try:
        watcher.run()
    except KeyboardInterrupt:
        print("\n\nWatcher stopped successfully")
