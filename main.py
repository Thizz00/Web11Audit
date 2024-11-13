import argparse
import logging
from web11audit.auditor import AccessibilityAuditor
from web11audit.reporter import AccessibilityReporter

logging.basicConfig(level=logging.INFO)


def main():
    parser = argparse.ArgumentParser(description="Check accessibility of a webpage.")
    parser.add_argument("url", help="URL of the webpage to check")
    args = parser.parse_args()

    auditor = AccessibilityAuditor(args.url)
    results = auditor.audit_accessibility()

    reporter = AccessibilityReporter(results)
    reporter.report()


if __name__ == "__main__":
    main()
