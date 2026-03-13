import os
import sys

# Add app directory to Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'app'))

# Import Flask app
from app import app

# Export for Vercel (this is the entry point)
app = app