import uuid
from datetime import datetime


def generate_uuid():
    return str(uuid.uuid4())


def format_created_date():
    created_date = datetime.today()
    return f"{created_date.month} {created_date.day}, {created_date.year}"