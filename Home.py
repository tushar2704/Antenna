##© 2024 Tushar Aggarwal. All rights reserved.(https://tushar-aggarwal.com)
##Antenna[Towards-GenAI] (https://github.com/Towards-GenAI)
##################################################################################################
#Importing dependencies
import os
import google.generativeai as genai
from dotenv import load_dotenv
import google.generativeai as genai
import logging

##################################################################################################
# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

##################################################################################################
#Environmental variables
load_dotenv()
# genai.configure(api_key=GOOGLE_API_KEY)
# os.getenv("GOOGLE_API_KEY")
# genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))


google_api_key = os.getenv("GOOGLE_API_KEY")

##################################################################################################
#Check if api key loaded successfully with logging info
if google_api_key:
    logger.info("Google API Key loaded successfully.")
else:
    logger.error("Failed to load Google API Key.")

##################################################################################################


































































