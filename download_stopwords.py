import ssl
import certifi
import nltk
from nltk.data import find

# Function to set up SSL context
def configure_ssl():
    try:
        context = ssl.create_default_context(cafile=certifi.where())
        ssl._create_default_https_context = lambda: context
    except AttributeError:
        pass

configure_ssl()

# Download stopwords
try:
    nltk.download('stopwords')
except Exception as e:
    print(f"Error: {e}")
