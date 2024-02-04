import uuid
import concurrent.futures

def generate_device(_):  # Add a dummy argument to handle the extra argument from map
    number1 = str(uuid.uuid4().int & (1<<63)-1)
    number2 = str(uuid.uuid4().int & (1<<63)-1)
    uuid_value = str(uuid.uuid4())
    random_string = ''.join([chr(ord('a') + (i % 26)) for i in range(32)])
    return f"{number1}:{number2}:{uuid_value}:{random_string}"

def generate_and_save_devices(num_devices, file_name):
    with open(file_name, 'w') as file:
        with concurrent.futures.ThreadPoolExecutor(max_workers=100) as executor:
            # Use a list to collect the results from the threads
            devices = list(executor.map(generate_device, range(num_devices)))
            
            for device in devices:
                file.write(device + '\n')

num_devices_to_generate = 100000  # Changed to 100,000
output_file_name = 'devices.txt'

generate_and_save_devices(num_devices_to_generate, output_file_name)

print(f"Done")
