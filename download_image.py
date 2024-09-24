# download_image.py
import time
from redis_client import get_redis_client

def download_image_from_redis(client, redis_key, output_path):
    image_data = client.get(redis_key)  # Fetch image data from Redis
    output_file_path = f"{output_path}/gcp_downloaded.png"  # Full path including the filename
    with open(output_file_path, 'wb') as image_file:
        image_file.write(image_data)

if __name__ == "__main__":
    redis_host = 'localhost'  # Redis host IP
    redis_port = 6378  # Redis port
    client = get_redis_client(redis_host, redis_port)

    redis_key = 'image_key'  # Key under which image was stored
    output_path = '/home/g20cse0026/GCPRedisCache/destination/gcp_downloaded.png'  # Ensure this directory exists
  # Destination folder

    start_time = time.time()
    download_image_from_redis(client, redis_key, output_path)
    end_time = time.time()

    print(f"Image downloaded from Redis and saved to {output_path}/gcp_downloaded.png")
    print(f"Download time: {end_time - start_time:.2f} seconds")
