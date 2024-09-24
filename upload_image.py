from redis_client import get_redis_client

def upload_image_to_redis(client, image_path, redis_key):
    with open(image_path, 'rb') as image_file:
        image_data = image_file.read()  
        client.set(redis_key, image_data)  

if __name__ == "__main__":
    redis_host = 'localhost' 
    redis_port = 6378  
    client = get_redis_client(redis_host, redis_port)
    
    image_path = '/home/g20cse0026/GCPRedisCache/images/gcp.png'  # Adjust this based on your VM's directory structure
  
    redis_key = 'image_key'
    
    upload_image_to_redis(client, image_path, redis_key)
    print(f"Image uploaded to Redis with key: {redis_key}")