import requests

def get_order_details():
    base_url = "https://petstore.swagger.io/v2"
    
    # Fetch details for 100 orders
    for order_id in range(1, 101):
        order_url = f"{base_url}/store/order/{order_id}"
        
        try:
            order_response = requests.get(order_url)
            
            if order_response.status_code == 200:
                order_data = order_response.json()
                pet_id = order_data.get("petId")
                
                if pet_id:
                    # Fetch pet details if petId exists in the order
                    pet_url = f"{base_url}/pet/{pet_id}"
                    pet_response = requests.get(pet_url)
                    
                    if pet_response.status_code == 200:
                        print(f"Order {order_id} for pet {pet_id}.")
                    else:
                        print(f"Order {order_id} references pet {pet_id}, but pet details could not be fetched.")
                else:
                    print(f"Order {order_id} has no associated pet.")
            else:
                print(f"Failed to fetch details for order {order_id}. HTTP Status Code: {order_response.status_code}")
        except requests.exceptions.RequestException as e:
            print(f"An error occurred while fetching details for order {order_id}: {e}")

if __name__ == "__main__":
    get_order_details()
