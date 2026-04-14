from src.integration.mocking_injected.risk_database import RiskDatabase


class FraudDetector:
    """Evaluates fraud risk for a customer using a risk score.

    Risk thresholds:
        score > 90  -> blocked  (highest risk; transaction must be refused)
        score > 70  -> flagged  (elevated risk; transaction requires review)
        score <= 70 -> clear    (normal risk; transaction may proceed)

    Both thresholds are checked independently, giving the PaymentProcessor
    two distinct methods to call on the real FraudDetector.

    Methods:
        is_blocked(customer_id) — True if the customer's score is above 90
        is_flagged(customer_id) — True if the customer's score is above 70
    """

    def __init__(self, risk_database: RiskDatabase) -> None:
        """Initialise a FraudDetector with the given risk database.

        parameters:
            risk_database -- a RiskDatabase used to retrieve customer risk scores

        returns:
            none
        """
        self._db = risk_database

    def is_blocked(self, customer_id: str) -> bool:
        """Return True if the customer's risk score exceeds 90.

        parameters:
            customer_id -- the unique identifier of the customer

        returns:
            True  -- if the customer's risk score is greater than 90
            False -- if the customer's risk score is 90 or below
        """
        return self._db.get_score(customer_id) > 90

    def is_flagged(self, customer_id: str) -> bool:
        """Return True if the customer's risk score exceeds 70.

        parameters:
            customer_id -- the unique identifier of the customer

        returns:
            True  -- if the customer's risk score is greater than 70
            False -- if the customer's risk score is 70 or below
        """
        return self._db.get_score(customer_id) > 70
