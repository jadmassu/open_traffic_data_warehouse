
def try_parse_int(value, default=0):
    try:
        return int(value)
    except ValueError:
        return default

def try_parse_float(value, default=0.0):
    try:
        return float(value)
    except ValueError:
        return default


def load_data_from_csv(csv_file):
    vehicle_data = []
    vehicle_path_data = []
    try:
        with open(csv_file, 'r') as file:
            # Skip the header row
            next(file)

            # Read vehicle data from the first line
            for line in file:
                row = line.strip().split(',')
                track_id = try_parse_int(row[0])
                type_vehicle = row[1]
                traveled_distance = try_parse_float(row[2])
                avg_speed = try_parse_float(row[3])
                vehicle_data.append({
                    'track_id': track_id,
                    'type': type_vehicle,
                    'traveled_distance': traveled_distance,
                    'avg_speed': avg_speed
                })

                # Read path data
                path_data = []
                for i in range(4, len(row), 6):  # Starting index for path data, assuming time is available
                    lat = try_parse_float(row[i])
                    lon = try_parse_float(row[i+1])
                    speed = try_parse_float(row[i+2])
                    lon_acc = try_parse_float(row[i+3])
                    lat_acc = try_parse_float(row[i+4])
                    time = try_parse_float(row[i+5])  # Assuming time is available
                    path_data.append({
                        'track_id': track_id,
                        'lat': lat,
                        'lon': lon,
                        'speed': speed,
                        'lon_acc': lon_acc,
                        'lat_acc': lat_acc,
                        'time': time
                    })
                vehicle_path_data.extend(path_data)
        return vehicle_data, vehicle_path_data
            
    except Exception as e:
        print(f"Error loading data from CSV: {e}")
        return [], []


