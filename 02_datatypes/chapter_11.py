import arrow

brewing_time = arrow.utcnow()
rome_time = brewing_time.to("Europe/Rome")

print(f"UTC time: {brewing_time}")
print(f"Rome time: {rome_time}")

from collections import namedtuple

chaiProfile = namedtuple("chaiProfile", ["flavor", "aroma"])

profile = chaiProfile(flavor="spicy", aroma="ginger")

print(f"Chai profile: {profile}")
print(f"Flavor: {profile.flavor}")
print(f"Aroma: {profile.aroma}")
