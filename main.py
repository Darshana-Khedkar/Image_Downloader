import os
import requests

def get_extension(image_url: str) -> str | None:
    extensions: list[str] = ['.png', '.jpeg', '.jpg', '.gif', '.svg']
    for ext in extensions:
        if ext in image_url:
            return ext
        
def download_image(image_url: str, name: str, folder: str = None):
    if ext:=get_extension(image_url):
        if  folder:
            image_name: str = f"{folder}/{name}{ext}"
            
        else:
            image_name: str = f"{name}{ext}"
            
    else:
        raise Exception('Image extension could not get located...')
    
    # check if name already exists
    
    if os.path.isfile(image_name):
        raise Exception('File name already exists...')
    
    
    
    #Download the image
    
    try:
        image_content: bytes = requests.get(image_url).content
        with open(image_name, 'wb') as handler:
            handler.write(image_content)
            
            print(f'Downloaded: "{image_name}" Successfully!')
            
    except Exception as e:
        print(f"Error: {e}")
        
if __name__ == '__main__':
    input_url: str = input("enter a url: ")
    input_name: str = input("what would you like to name it?:")
    
    print("Downloading...")
    download_image(input_url, name=input_name, folder='images')
    
            
     
    
    
    
    