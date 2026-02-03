"""
Bronze Tier Verification Script
Verifies all Bronze tier components are properly set up
"""
import sys
from pathlib import Path


def check_folder_structure(vault_path):
    """Verify all required folders exist"""
    required_folders = [
        'Inbox',
        'Needs_Action',
        'Done',
        'Pending_Approval',
        'Approved',
        'Plans',
        'Logs',
        '.obsidian',
        '.claude/skills'
    ]

    print("\n" + "="*60)
    print("FOLDER STRUCTURE CHECK")
    print("="*60)

    all_exist = True
    for folder in required_folders:
        folder_path = vault_path / folder
        exists = folder_path.exists()
        status = "✓" if exists else "✗"
        print(f"{status} {folder}")
        if not exists:
            all_exist = False

    return all_exist


def check_core_files(vault_path):
    """Verify core markdown files exist"""
    required_files = [
        'Dashboard.md',
        'Company_Handbook.md',
        'README.md',
        'BRONZE_TIER_COMPLETE.md'
    ]

    print("\n" + "="*60)
    print("CORE FILES CHECK")
    print("="*60)

    all_exist = True
    for file in required_files:
        file_path = vault_path / file
        exists = file_path.exists()
        status = "✓" if exists else "✗"
        size = file_path.stat().st_size if exists else 0
        print(f"{status} {file} ({size} bytes)")
        if not exists:
            all_exist = False

    return all_exist


def check_watcher_script(vault_path):
    """Verify watcher script exists and is valid"""
    print("\n" + "="*60)
    print("WATCHER SCRIPT CHECK")
    print("="*60)

    watcher_files = [
        'base_watcher.py',
        'filesystem_watcher.py',
        'requirements.txt'
    ]

    all_exist = True
    for file in watcher_files:
        file_path = vault_path / file
        exists = file_path.exists()
        status = "✓" if exists else "✗"
        print(f"{status} {file}")
        if not exists:
            all_exist = False

    return all_exist


def check_agent_skills(vault_path):
    """Verify Agent Skills are created"""
    print("\n" + "="*60)
    print("AGENT SKILLS CHECK")
    print("="*60)

    skills_dir = vault_path / '.claude' / 'skills'
    if not skills_dir.exists():
        print("✗ Skills directory not found")
        return False

    required_skills = [
        'process-actions.skill.md',
        'update-dashboard.skill.md',
        'start-watcher.skill.md'
    ]

    all_exist = True
    for skill in required_skills:
        skill_path = skills_dir / skill
        exists = skill_path.exists()
        status = "✓" if exists else "✗"
        print(f"{status} {skill}")
        if not exists:
            all_exist = False

    return all_exist


def check_test_results(vault_path):
    """Check if test workflow was completed"""
    print("\n" + "="*60)
    print("TEST WORKFLOW CHECK")
    print("="*60)

    # Check if test file was processed
    done_folder = vault_path / 'Done'
    test_files = list(done_folder.glob('FILE_test_document*.md'))

    if test_files:
        print(f"✓ Test workflow completed ({len(test_files)} test file(s) in Done/)")
        return True
    else:
        print("✗ No completed test files found in Done/")
        return False


def main():
    # Fix Windows console encoding
    import io
    if sys.platform == 'win32':
        sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

    # Get vault path
    vault_path = Path(sys.argv[1]) if len(sys.argv) > 1 else Path('.')
    vault_path = vault_path.resolve()

    print("\n" + "="*60)
    print("BRONZE TIER VERIFICATION")
    print("="*60)
    print(f"Vault: {vault_path}")
    print("="*60)

    # Run all checks
    checks = {
        'Folder Structure': check_folder_structure(vault_path),
        'Core Files': check_core_files(vault_path),
        'Watcher Script': check_watcher_script(vault_path),
        'Agent Skills': check_agent_skills(vault_path),
        'Test Workflow': check_test_results(vault_path)
    }

    # Summary
    print("\n" + "="*60)
    print("VERIFICATION SUMMARY")
    print("="*60)

    all_passed = True
    for check_name, passed in checks.items():
        status = "✓ PASS" if passed else "✗ FAIL"
        print(f"{status} - {check_name}")
        if not passed:
            all_passed = False

    print("="*60)

    if all_passed:
        print("\n🎉 BRONZE TIER: COMPLETE ✅")
        print("\nAll components verified successfully!")
        print("Your AI Employee is ready for basic automation.")
        print("\nNext steps:")
        print("1. Open vault in Obsidian")
        print("2. Test the watcher: python filesystem_watcher.py .")
        print("3. Review BRONZE_TIER_COMPLETE.md for details")
        print("4. Consider advancing to Silver tier")
    else:
        print("\n⚠️  BRONZE TIER: INCOMPLETE")
        print("\nSome components are missing. Review the checks above.")

    print("\n" + "="*60 + "\n")

    return 0 if all_passed else 1


if __name__ == '__main__':
    sys.exit(main())
