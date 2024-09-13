from drama import oscar
from dateutil.parser import parse as dtp

max_allowable_lifetime = 1
launch_date = dtp("2027-09-01 00:00")
spacecraft_mass_in_kg = 16
drag_area_in_m2 = 0.034015
coefficient_of_drag = 2.2

R_earth = 6378

drama_config = {
    'epoch': launch_date,
    'sma': 6378 + 100,
    'ecc': 0.00001,
    'inc': 97.6,
    'raan': 0.0,
    'aop': 0.0,
    'ma': 0.0,
    'cross_section': drag_area_in_m2,
    'mass': spacecraft_mass_in_kg,
    'drag_coefficient': coefficient_of_drag,
    'reflectivity_coefficient': 1.9
}

current_computed_lifetime = 0.0
step_size_in_km = 1.0
starting_search_altitude = 100

drama_config["sma"] = R_earth + starting_search_altitude

altitudes = []
lifetimes = []

# TODO: Speed this up so that it is faster
while(current_computed_lifetime < max_allowable_lifetime):
    drama_config['sma'] += step_size_in_km
    results = oscar.run(drama_config, parallel=False)
    current_computed_lifetime = results["results"][0]["lifetime"]
    altitudes.append(drama_config['sma'] - R_earth)
    lifetimes.append(current_computed_lifetime)

print(altitudes[-1])
print(lifetimes[-1])