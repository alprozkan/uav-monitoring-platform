from app import app, db
from models import Drone

def seed_data():
    with app.app_context():
        db.create_all()

        # Create initial drone data
        drones = [
            Drone(name='Drone 1', model='Model A'),
            Drone(name='Drone 2', model='Model B'),
            Drone(name='Drone 3', model='Model C')
        ]

        db.session.bulk_save_objects(drones)
        db.session.commit()

if __name__ == '__main__':
    seed_data()
    print("Database seeded successfully.")
