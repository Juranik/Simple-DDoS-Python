import requests  # Import the requests library to work with HTTP requests
import time  # Import the time library to work with time

# Function send_requests takes URL, number of requests, and requests per second
def send_requests(url, num_requests, requests_per_second):
    start_time = time.time()  # Record the start time of the function
    for i in range(num_requests):  # Loop to send the specified number of requests
        try:
            response = requests.get(url)  # Send a GET request to the specified URL
            print(f"Request {i+1}: {response.status_code}")  # Print the request number and response status code
        except requests.exceptions.RequestException as e:  # Handle errors that occur during the request
            print(f"Request {i+1}: Error: {str(e)}")  # Print the request number and error message
        time.sleep(1 / requests_per_second)  # Wait to not exceed the requests per second limit
    end_time = time.time()  # Record the end time of the function
    print(f"\nTotal time taken: {end_time - start_time:.2f} seconds")  # Print the total execution time

# Set parameters: URL, number of requests, and requests per second
url = "https://example.com/"  # URL to which we will send requests
num_requests = 1000  # Total number of requests
requests_per_second = 100  # Number of requests to send per second

# Call the function with the specified parameters
send_requests(url, num_requests, requests_per_second)
