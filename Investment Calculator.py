
# InvestmentCalculator class that allows you to put your initial investment, time, additional amount and rate and calculates and the total
# investment portfolio and time required to be millioniare.


class InvestmentCalculator:
    
    def __init__(self, initial_investment=0.0, time_period=0, additional_amount=0.0, rate_of_return=0.0):
        # Constructor to initialize the InvestmentCalculator object.
        self.initial_investment = initial_investment
        self.time_period = time_period
        self.additional_amount = additional_amount
        self.rate_of_return = rate_of_return

    def set_initial_investment(self, initial_investment):
        # Set the initial investment amount.
        self.initial_investment = initial_investment

    def set_time_period(self, time_period):
        # Set the time period of the investment.
        self.time_period = time_period

    def set_additional_amount(self, additional_amount):
        # Set the additional amount added annually.
        self.additional_amount = additional_amount

    def set_rate_of_return(self, rate_of_return):
        # Set the annual rate of return on the investment.
        self.rate_of_return = rate_of_return

    def get_initial_investment(self):
        # Get the initial investment amount.
        return self.initial_investment

    def get_time_period(self):
        # Get the time period of the investment.
        return self.time_period

    def get_additional_amount(self):
        # Get the additional amount added annually.
        return self.additional_amount

    def get_rate_of_return(self):
        # Get the annual rate of return on the investment.
        return self.rate_of_return

    def calculate_investment_value(self):
        # Calculate the final value of the investment portfolio.
        investment_value = self.initial_investment
        for _ in range(self.time_period):
            if self.rate_of_return >= 0:
                investment_value += (self.rate_of_return / 100) * investment_value
            else:
                investment_value -= abs((self.rate_of_return / 100) * investment_value)
            investment_value += self.additional_amount
        return investment_value - self.additional_amount

    def investment_return_with_changed_amount(self, rate_of_yearly_change):
        # Calculate the final investment value with a changed additional amount.
        investment_value = self.calculate_investment_value()
        for _ in range(self.time_period):
            if self.rate_of_return >= 0:
                investment_value += (self.rate_of_return / 100) * investment_value
            else:
                investment_value -= abs((self.rate_of_return / 100) * investment_value)
            self.additional_amount += (rate_of_yearly_change / 100) * self.additional_amount
        return investment_value - self.additional_amount

    def is_millionaire(self):
        # Calculate the time required to become a millionaire.
        time = 0
        investment_value = self.initial_investment
        while investment_value <= 1000000:
            investment_value += self.additional_amount
            if self.rate_of_return >= 0:
                investment_value += (self.rate_of_return / 100) * investment_value
            else:
                investment_value -= abs((self.rate_of_return / 100) * investment_value)
            time += 1
        return time

    def __str__(self):
        # Convert the object to a string representation.
        return f"Your initial value was {self.initial_investment}. Your total investment time was {self.time_period} years. Your rate of return was {self.rate_of_return}%. Your total portfolio is {self.calculate_investment_value()}"

    def __eq__(self, other):
        # Check if two InvestmentCalculator objects have the same investment value.
        return self.calculate_investment_value() == other.calculate_investment_value()


def main():
    calculator1 = InvestmentCalculator()
    calculator2 = InvestmentCalculator()

    for i in range(1, 3):
        print(f"Enter values for Calculator {i}:")
        initial_investment = float(input("Initial investment: "))
        time_period = int(input("Time period (in years): "))
        additional_amount = float(input("Additional amount (yearly): "))
        rate_of_return = float(input("Rate of return (in percentage): "))
        print("-----------------------------------")

        if i == 1:
            calculator1.set_initial_investment(initial_investment)
            calculator1.set_time_period(time_period)
            calculator1.set_additional_amount(additional_amount)
            calculator1.set_rate_of_return(rate_of_return)
        else:
            calculator2.set_initial_investment(initial_investment)
            calculator2.set_time_period(time_period)
            calculator2.set_additional_amount(additional_amount)
            calculator2.set_rate_of_return(rate_of_return)

    print("\nCALCULATOR I RESULT:")
    investment_value1 = calculator1.calculate_investment_value()
    print(f"Your total investment portfolio after {calculator1.get_time_period()} years will be {investment_value1:.2f}.")
    print(f"It will take {calculator1.is_millionaire()} years to become a millionaire.")
    print(calculator1)

    print("\nEver wondered what your investment portfolio would have been if you increased the additional amount by a certain percentage yearly.")
    rate_of_increase1 = float(input("Enter the percentage value: "))
    print(f"Your investment return would have been {calculator1.investment_return_with_changed_amount(rate_of_increase1):.2f} if you had increased the additional amount yearly.")

    print("\nCALCULATOR II RESULT:")
    investment_value2 = calculator2.calculate_investment_value()
    print(f"Your total investment portfolio after {calculator2.get_time_period()} years will be {investment_value2:.2f}.")
    print(f"It will take {calculator2.is_millionaire()} years to become a millionaire.")
    print(calculator2)

    rate_of_increase2 = float(input("Enter the percentage value: "))
    print(f"Your investment return would have been {calculator2.investment_return_with_changed_amount(rate_of_increase2):.2f} if you had increased the additional amount yearly.")

    print("Are the two calculators equal: ", calculator1 == calculator2)
    
    if investment_value1 > investment_value2:
        greaterValue = "The first person is a wise investor."
    else:
        greaterValue = "The second person is a wise investor."
           
        print ("----------------------------------")
        print( greaterValue)
    


if __name__ == "__main__":
    main()
