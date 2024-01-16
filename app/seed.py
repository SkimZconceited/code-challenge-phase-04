from app import app, db
from models import Hero, Power, HeroPower
import random

all_heroes = [
    { "name": "Kamala Khan", "super_name": "Ms. Marvel" },
    { "name": "Doreen Green", "super_name": "Squirrel Girl" },
    { "name": "Gwen Stacy", "super_name": "Spider-Gwen" },
    { "name": "Janet Van Dyne", "super_name": "The Wasp" },
    { "name": "Wanda Maximoff", "super_name": "Scarlet Witch" },
    { "name": "Carol Danvers", "super_name": "Captain Marvel" },
    { "name": "Jean Grey", "super_name": "Dark Phoenix" },
    { "name": "Ororo Munroe", "super_name": "Storm" },
    { "name": "Kitty Pryde", "super_name": "Shadowcat" },
    { "name": "Elektra Natchios", "super_name": "Elektra" }]

all_powers = [
    { "name": "super strength", "description": "gives the wielder super-human strengths" },
    { "name": "flight", "description": "gives the wielder the ability to fly through the skies at supersonic speed" },
    { "name": "super human senses", "description": "allows the wielder to use her senses at a super-human level" },
    { "name": "elasticity", "description": "can stretch the human body to extreme lengths" }
]

def seed_heroes():
    with app.app_context():
        
        for hero in all_heroes:
            new_hero = Hero(name = hero['name'], super_name = hero['super_name'])
            db.session.add(new_hero)
        db.session.commit()
        
        # hero = Hero(name = 'Bruce Wayne', super_name = 'Batman')
        # db.session.add(hero)
        # db.session.commit()
        # pass

            # hero_to_delete = Hero.query.filter_by(name=hero['name'], super_name=hero['super_name']).first()
            # if hero_to_delete:
            #     # Delete the fetched hero
            #     db.session.delete(hero_to_delete)
            #     db.session.commit()
        

def seed_powers():
    with app.app_context():
        for power in all_powers:
            new_power = Power(name = power['name'], description = power['description'])
            db.session.add(new_power)
        db.session.commit()


def seed_heropower():
    strengths = ["Strong", "Weak", "Average"]

    # Assuming you have already populated the Hero and Power tables
    with app.app_context():
        all_hero_ids = Hero.query.all()
        all_power_ids = [power.id for power in Power.query.all()]
        
        print(all_hero_ids)
        for hero in all_hero_ids:
            for _ in range(random.randint(1, 3)):  # Random number of powers between 1 and 3
                # Get a random power
                power_id = random.choice(all_power_ids)
                strength = random.choice(strengths)

                # Create a new HeroPower association
                new_hero_power = HeroPower(hero_id=hero.id, power_id=power_id, strength=strength)
                db.session.add(new_hero_power)

        db.session.commit()
            
# seed_heroes()
# seed_powers()
seed_heropower()