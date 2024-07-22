from models import db, ApiUser, Location, Device

def create_tables():
    with db:
        db.create_tables([ApiUser, Location, Device])

if __name__ == '__main__':
    create_tables()