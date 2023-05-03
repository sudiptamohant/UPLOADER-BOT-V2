import os

class Config(object):
    
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6102078578:AAHHOgYpKduh_OFRtzh5yLBOKa1KrDVqXg0")
    
    API_ID = int(os.environ.get("API_ID", 5806640))
    
    API_HASH = os.environ.get("127f130ad3745dbcd31aa39aa0eabcb8")
    
    DOWNLOAD_LOCATION = "./DOWNLOADS"
    
    MAX_FILE_SIZE = 50000000

    TG_MAX_FILE_SIZE = 2097152000

    FREE_USER_MAX_FILE_SIZE = 50000000
    
    CHUNK_SIZE = int(128)

    HTTP_PROXY = ""
    
    MAX_MESSAGE_LENGTH = 4096
    
    PROCESS_MAX_TIMEOUT = 3600
    
    OWNER_ID = int(os.environ.get("1375408229", "1375408229"))

    SESSION_NAME = "UploadLinkToFileBot"
    
    DATABASE_URL = os.environ.get("DATABASE_URL", "mongodb+srv://bossboltebro:<password>@cluster0.jrzdzmy.mongodb.net/?retryWrites=true&w=majority")

    MAX_RESULTS = "50"
