import yaml
from google_images_download import google_images_download

config = yaml.load(open('config.yaml'), Loader=yaml.FullLoader)
response = google_images_download.googleimagesdownload()

def downloadimages(): 
    
    arguments = {"keywords": config["Search"], # This is your search term.
                 "output_directory": config["Out_Dir"],# This is your directory to save all downloads to.
                 "no_directory": True,
                 "format": "jpg",
                 "chromedriver": config["Chrome_Driver"],# This is only needed if you are downloading large batches of images. (100+)
                 "limit":config["Number_To_Download"],# This is how many images you want to download
                 "size": "medium"}
    try: 
        response.download(arguments) 
      
    # Handling File NotFound Error     
    except FileNotFoundError as Error:  
        print(Error)


if __name__ == "__main__":
    downloadimages()