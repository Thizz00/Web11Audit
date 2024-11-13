import pytest
from web11audit.auditor import AccessibilityAuditor


def test_audit_accessibility():

    LINK = "https://streamlit.io"

    auditor = AccessibilityAuditor(LINK)
    results = auditor.audit_accessibility()

    assert isinstance(results, dict)

    assert "violations" in results
