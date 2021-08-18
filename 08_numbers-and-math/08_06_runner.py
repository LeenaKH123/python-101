# If a runner runs 10 miles in 30 minutes and 30 seconds,
# What is their average speed in kilometers per hour?
# (Tip: 1 mile = 1.6 km)
minutes = 30
seconds = 30
distance_in_miles = 10
to_seconds = 30 * 60
total_time = to_seconds + seconds
# velocity_miles_seconds = distance_in_miles / total_time
distance_in_km = distance_in_miles * 1.6
time_hours = total_time / 3600
velocity_km_hr = distance_in_km / time_hours
print(velocity_km_hr)
