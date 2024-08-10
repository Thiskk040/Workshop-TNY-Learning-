if __name__ == "__main__":
    gym = ClimbingGym()
    gym.run()
class ClimbingGym:
    def __init__(self):
        self.history = []

    def calculate_price(self, name, age, height, hours, people, trainer_needed):
        price_per_person = 0

        if height >= 101 and height <= 120:
            price_per_person = 460
        elif height > 120 and height <= 140:
            price_per_person = 460
        elif height > 140:
            price_per_person = 460
        if age >= 60:
            price_per_person = 0  # Senior is free

        trainer_cost = 450 * hours if trainer_needed else 0
        total_price = (price_per_person * hours * people) + trainer_cost
        total_price += max(0, hours - 2) * 50 * people  # Extra charge for more than 2 hours

        self.history.append({
            "name": name,
            "age": age,
            "height": height,
            "hours": hours,
            "people": people,
            "trainer_needed": trainer_needed,
            "total_price": total_price
        })

        return total_price

    def print_history(self):
        if not self.history:
            print("No history available.")
        else:
            for idx, entry in enumerate(self.history, 1):
                print(f"Entry {idx}: {entry}")

    def run(self):
        while True:
            command = input("Enter 'login' to calculate the price, 'history' to view history, or 'exit' to exit: ").lower()

            if command == 'login':
                name = input("Enter name: ")
                age = int(input("Enter age: "))
                height = int(input("Enter height (in cm): "))
                hours = int(input("Enter number of hours: "))
                people = int(input("Enter number of people: "))
                trainer_needed = input("Do you need a trainer? (yes/no): ").lower() == 'yes'

                total_price = self.calculate_price(name, age, height, hours, people, trainer_needed)
                print(f"Total Price: {total_price} THB")

            elif command == 'history':
                self.print_history()

            elif command == 'exit':
                print("Exiting the program.")
                break

            else:
                print("Invalid command. Please try again.")


if __name__ == "__main__":
    gym = ClimbingGym()
    gym.run()
