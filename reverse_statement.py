def reverse_statement(statement: str) -> str:
    """Reverse any given statement or string."""
    return statement[::-1]


if __name__ == "__main__":
    user_input = input("Enter a statement to reverse: ")
    result = reverse_statement(user_input)
    print(f"Original : {user_input}")
    print(f"Reversed : {result}")
