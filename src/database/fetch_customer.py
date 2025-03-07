from db_utils import fetch_customer

"""
Script to retrieve and display customer information.
"""
if __name__ == "__main__":
    try:
        customers = fetch_customer()
        print("\nList of customers:")
        print("------------------")
        print(customers)
    except Exception as e:
        print(f"Error: {e}")