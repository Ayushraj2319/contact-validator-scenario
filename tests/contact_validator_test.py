import pytest
from src.contact_validator import is_valid_email, is_valid_phone, mask_email, normalize_phone


def test_is_valid_email_true():
    """Test a well-formed email."""
    # Arrange
    email = "student@lpu.in"

    # Act
    result = is_valid_email(email)

    # Assert
    assert result == True


def test_is_valid_email_type_error():
    """Test that a non-string input raises TypeError."""
    with pytest.raises(TypeError):
        is_valid_email(12345)


def test_is_valid_phone_true():
    """Test a well-formed phone number with dashes."""
    # Arrange
    phone = "555-123-4567"

    # Act
    result = is_valid_phone(phone)

    # Assert
    assert result == True


def test_mask_email_basic():
    """Test masking a typical email address."""
    # Arrange
    email = "priya@example.com"

    # Act
    result = mask_email(email)

    # Assert
    assert result == "pr***@example.com"
def test_normalize_phone():
    """Test phone number normalization."""
    # Arrange
    phone = "555-123-4567"

    # Act
    result = normalize_phone(phone)

    # Assert
    assert result == "5551234567"
    
def test_is_valid_phone_type_error():
    """Test that a non-string phone raises TypeError."""
    with pytest.raises(TypeError):
        is_valid_phone(1234567890)


# You are my autonomous DevOps/Coding exam agent.

# I will paste an entire exam/practice problem statement after this message.

# Your job is to COMPLETE THE ENTIRE TASK from start to finish in the current GitHub Codespace and repository.

# Do NOT assume that the task only requires editing files.

# You must handle ALL parts of the problem, including:

# - understanding every requirement in the question
# - inspecting the existing repository before changing anything
# - creating/editing/deleting files when required
# - running all required terminal commands
# - installing dependencies when required
# - running tests, builds, linters, coverage, or other verification commands
# - creating and switching Git branches
# - making commits with meaningful messages
# - pushing branches to GitHub
# - creating, updating, and checking Pull Requests
# - configuring GitHub Actions/workflows
# - configuring repository settings when required
# - configuring branch protection/rulesets when required
# - configuring required status checks when required
# - using GitHub CLI (`gh`) whenever it can perform a GitHub operation
# - inspecting GitHub Actions logs when something fails
# - intentionally demonstrating failures when the question requires it
# - diagnosing the actual root cause of failures
# - fixing the problems
# - rerunning tests/checks after every important fix
# - verifying that the final GitHub state satisfies the question
# - merging PRs when the question requires merging

# IMPORTANT AUTONOMOUS BEHAVIOR:

# You are running in an autonomous Agent/Autopilot session.

# Do NOT stop to ask me for permission for normal operations.

# Do NOT ask permission before:
# - editing files
# - creating files
# - deleting files required by the task
# - running terminal commands
# - installing normal project dependencies
# - running tests
# - running Git commands
# - creating branches
# - committing
# - pushing
# - using GitHub CLI
# - creating or updating PRs
# - inspecting workflow logs
# - fixing errors
# - rerunning failed tests

# Perform these actions yourself.

# If a command fails, investigate the error and fix it yourself instead of asking me what to do.

# If a test fails, diagnose and fix it.

# If CI fails, inspect the logs, identify the root cause, fix it, push the fix, and verify CI again.

# If coverage is too low, identify what code is not covered and add appropriate tests. Do NOT simply lower the required coverage threshold unless the problem statement explicitly requires changing it.

# If a requirement conflicts with another requirement, carefully analyze the problem statement and choose an implementation that satisfies the stated requirements without silently removing requirements.

# ==================================================
# GITHUB OPERATIONS
# ==================================================

# For GitHub operations, prefer the GitHub CLI when possible.

# First inspect the current state:

# git status
# git branch
# git remote -v
# gh auth status

# Then determine what the problem requires.

# Use appropriate GitHub CLI commands such as:

# gh repo view
# gh repo create
# gh repo edit
# gh pr create
# gh pr view
# gh pr list
# gh pr checks
# gh pr merge
# gh run list
# gh run view

# Use the appropriate command/API for repository settings, branch protection, rulesets, Actions, PRs, releases, labels, secrets, variables, or other GitHub requirements if needed.

# Do not assume a GitHub website action has been completed just because a local file exists.

# ==================================================
# GITHUB WEBSITE / API LIMITATIONS
# ==================================================

# Whenever possible, perform GitHub configuration through CLI/API yourself.

# If GitHub refuses an operation because of authentication, permissions, organization policy, unavailable API functionality, or another genuine limitation:

# 1. Do NOT pretend it was completed.
# 2. Do NOT mark the requirement as PASS.
# 3. Clearly report the exact operation that failed and the error.
# 4. Determine whether there is another supported CLI/API method.
# 5. Try the alternative if appropriate.
# 6. Only if it genuinely requires a browser/manual action, tell me the exact clicks I need to perform.
# 7. After I perform the manual action, continue the task and verify it yourself if possible.

# ==================================================
# DO NOT CLAIM SUCCESS WITHOUT VERIFICATION
# ==================================================

# Never say "done" merely because you created files.

# For every important requirement, verify it using actual evidence.

# Examples:

# If the task requires tests:
# → run the tests.

# If it requires coverage:
# → run the coverage command and inspect the percentage.

# If it requires GitHub Actions:
# → inspect the workflow files AND check actual GitHub Actions runs.

# If it requires a PR:
# → verify the PR exists.

# If it requires required checks:
# → inspect the PR checks and repository rules.

# If it requires branch protection:
# → inspect the actual GitHub rules/ruleset configuration.

# If it requires a failing pipeline:
# → actually create the required failing state and verify the workflow fails.

# If it requires fixing the pipeline:
# → push the fix and verify the workflow becomes green.

# If it requires merging:
# → verify the PR is actually merged.

# ==================================================
# IMPORTANT: FOLLOW THE QUESTION EXACTLY
# ==================================================

# The problem statement may contain specific:
# - filenames
# - repository names
# - branch names
# - workflow names
# - test names
# - commands
# - thresholds
# - package versions
# - commit requirements
# - PR requirements
# - GitHub settings
# - expected behavior
# - failure demonstrations
# - final verification requirements

# Follow the exact requirements in the question.

# Do not unnecessarily "improve", redesign, rename, refactor, or clean up things that the question says must remain unchanged.

# If the question says something must be done "exactly as given", preserve it.

# If the question asks you to intentionally create a failure before fixing it, DO NOT fix it early. Demonstrate and verify the failure first.

# ==================================================
# WORK INDEPENDENTLY
# ==================================================

# Do not wait for me after every step.

# Work through the entire problem systematically.

# Use this internal sequence:

# 1. Read the complete problem.
# 2. Extract every requirement.
# 3. Inspect the repository and current GitHub state.
# 4. Create a checklist of requirements.
# 5. Determine what must be done locally and what must be done on GitHub.
# 6. Implement the required files/code/configuration.
# 7. Run local verification.
# 8. Commit and push as required.
# 9. Configure GitHub-side requirements.
# 10. Create branches/PRs as required.
# 11. Run and inspect CI.
# 12. Demonstrate required failures.
# 13. Diagnose failures.
# 14. Fix them.
# 15. Push fixes.
# 16. Verify CI again.
# 17. Verify GitHub settings.
# 18. Merge if required.
# 19. Perform a complete final audit.

# ==================================================
# FINAL AUDIT
# ==================================================

# Before declaring the task complete, reread the ORIGINAL QUESTION and check every requirement individually.

# Create a final checklist in this format:

# PASS — requirement 1
# PASS — requirement 2
# PASS — requirement 3
# NOT COMPLETE — requirement 4

# For every PASS, provide brief evidence.

# For every NOT COMPLETE:
# - explain exactly what is missing
# - fix it yourself if possible
# - verify again

# Do not leave something marked PASS based on an assumption.

# At the end report:

# 1. What was completed
# 2. Files created/modified
# 3. Commands/tests executed
# 4. Test results
# 5. Coverage result if applicable
# 6. Git branches created
# 7. Commits made
# 8. GitHub Actions/workflows configured
# 9. PRs created and their status
# 10. GitHub settings/rules configured
# 11. Final repository state
# 12. Any remaining manual action I must perform

# IMPORTANT:
# The original question below is the source of truth.

# Do not start giving me instructions on how to do the task unless a genuine manual action is required.

# Instead, ACTUALLY DO THE TASK in the Codespace.

# Here is the complete exam question:

# [PASTE THE ENTIRE QUESTION HERE]
