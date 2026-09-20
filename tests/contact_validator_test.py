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


#         You are my autonomous DevOps/CI assistant.

# I will give you a complete practice exercise/problem statement below.

# Your job is to complete the entire task in my current GitHub Codespace and repository, not just explain how to do it.

# IMPORTANT:
# 1. First read the entire problem statement carefully.
# 2. Inspect the current repository structure and existing files before making changes.
# 3. Convert every requirement into a checklist and make sure every requirement is completed.
# 4. Do the work yourself in the Codespace wherever you have permission.
# 5. Create, edit, and configure all required files.
# 6. Use the exact filenames, folder structure, commands, workflow names, branches, and requirements specified by the problem.
# 7. Do not unnecessarily change or "clean up" existing code that the problem tells me to leave unchanged.
# 8. Run the required tests locally.
# 9. Run coverage locally when required and record the actual result.
# 10. Create and configure the required GitHub Actions workflows.
# 11. Make sure workflow triggers, jobs, dependencies, and failure conditions exactly match the requirements.
# 12. Create a feature branch when the exercise requires one.
# 13. Make the intentional bug/failure required by the exercise and push it.
# 14. If a Pull Request is required, create the PR with the required title and description.
# 15. Wait for/check GitHub Actions results and inspect failures.
# 16. Diagnose failures from the actual logs rather than guessing.
# 17. Fix problems one at a time and rerun the tests.
# 18. Verify that all required checks pass.
# 19. Configure GitHub repository settings such as branch protection if you have permission.
# 20. Verify that the protection actually works rather than assuming it works.
# 21. Do not lower requirements such as coverage thresholds just to make a check pass.
# 22. Do not skip a requirement because it is inconvenient.
# 23. Before finishing, perform a complete final audit against the original problem statement.
# 24. Tell me exactly what you completed, what you could not complete because of GitHub permissions/UI limitations, and what I must manually click if anything remains.

# AUTONOMOUS MODE:
# - Do not give me a tutorial before doing the work.
# - Do not ask me to copy commands that you can execute yourself.
# - Do not ask me to create files manually if you can create/edit them yourself.
# - Do not stop after creating files; test everything.
# - If something fails, investigate and fix it.
# - If a GitHub UI action cannot be performed by the agent, clearly identify that specific action and give me the exact clicks required.
# - Never claim something is completed unless you have actually verified it.

# IMPORTANT FOR GIT:
# - Do not force-push.
# - Do not delete the main branch.
# - Do not overwrite unrelated work.
# - Before committing, inspect the changes.
# - Use clear commit messages.
# - Push changes to the appropriate branch.
# - Do not merge a PR until all requirements and checks are satisfied, unless the problem explicitly requires you to demonstrate a blocked merge first.

# At the end, give me:
# A. A requirement-by-requirement checklist.
# B. Tests and coverage results.
# C. GitHub Actions results.
# D. Branch/PR status.
# E. Anything I still need to do manually.

# Here is the problem statement:

# [PASTE THE ENTIRE PROBLEM STATEMENT HERE]
