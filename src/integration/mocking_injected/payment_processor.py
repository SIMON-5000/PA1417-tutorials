from src.integration.mocking_injected.fraud_detector import FraudDetector


class PaymentProcessor:
    """Processes a payment after evaluating fraud risk.

    Delegates risk evaluation to an injected FraudDetector. The decision
    logic is:
        blocked customer  -> return "blocked"
        flagged customer  -> return "flagged"
        clear customer    -> return "approved: <amount> SEK"

    Methods:
        process(customer_id, amount) — return the processing outcome string
    """

    def __init__(self, detector: FraudDetector) -> None:
        """Initialise a PaymentProcessor with the given fraud detector.

        parameters:
            detector -- a FraudDetector used to evaluate customer risk

        returns:
            none
        """
        self._detector = detector

    def process(self, customer_id: str, amount: float) -> str:
        """Evaluate fraud risk and return the payment outcome.

        parameters:
            customer_id -- the identifier of the customer making the payment
            amount      -- the payment amount in SEK

        returns:
            "blocked"                -- if the customer is blocked
            "flagged"                -- if the customer is flagged for review
            "approved: <amount> SEK" -- if the payment is approved
        """
        if self._detector.is_blocked(customer_id):
            return "blocked"
        if self._detector.is_flagged(customer_id):
            return "flagged"
        return f"approved: {amount} SEK"
