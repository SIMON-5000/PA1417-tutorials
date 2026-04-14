class LoanCalculator:
    """Calculates the total repayment for a loan.

    parameters:
        rate_service -- a service with a get_rate() method that returns a decimal (e.g. 0.05 for 5%)
        fee_service  -- a service with a get_fee() method that returns a fixed processing fee

    methods:
        total_repayment(amount) -- return principal + interest + processing fee
    """

    def __init__(self, rate_service, fee_service):
        """Initialise a LoanCalculator with the given rate and fee services.

        parameters:
            rate_service -- a service with a get_rate() method returning a decimal rate
            fee_service  -- a service with a get_fee() method returning a fixed processing fee

        returns:
            none
        """
        self._rate_service = rate_service
        self._fee_service = fee_service

    def total_repayment(self, amount: float) -> float:
        """Return the total repayment amount including interest and processing fee.

        parameters:
            amount -- the principal loan amount

        returns:
            the total repayment as a float (principal + interest + fee)
        """
        rate = self._rate_service.get_rate()
        fee = self._fee_service.get_fee()
        return amount + (amount * rate) + fee
