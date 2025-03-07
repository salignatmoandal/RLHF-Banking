from db_utils import fetch_customer

if __name__ == "__main__":
    try:
        customers = fetch_customer()
        print("\nListe des clients :")
        print("------------------")
        print(customers)
    except Exception as e:
        print(f"Erreur : {e}")