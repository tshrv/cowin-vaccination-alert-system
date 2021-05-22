from fastapi.templating import Jinja2Templates
from src import settings

# templates
templates = Jinja2Templates(directory=settings.TEMPLATES_DIR_PATH)
