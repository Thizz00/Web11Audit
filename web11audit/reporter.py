import logging

logger = logging.getLogger(__name__)


class AccessibilityReporter:
    def __init__(self, results):
        self.results = results

    def report(self):
        if self.results["violations"]:
            logger.info(
                f"Found {len(self.results['violations'])} accessibility issues:"
            )
            for violation in self.results["violations"]:
                logger.info(f"\nIssue: {violation['description']}")
                logger.info(f"Impact: {violation['impact']}")
                for node in violation["nodes"]:
                    logger.info(f"  Element: {node['html']}")
                    logger.info(
                        f"  Summary: {node.get('failureSummary', 'No details available')}"
                    )
        else:
            logger.info("No accessibility issues found on the page.")
