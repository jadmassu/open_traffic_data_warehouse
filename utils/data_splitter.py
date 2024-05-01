def load_data_from_csv(csv_file):
    vehicle_data = []
    vehicle_path_data = []
    try:
        with open(csv_file, 'r') as file:
            # Skip the header row
            next(file)
            for line in file:
            # Split the line by tab
                row = line.strip().split('\t')
                track_id = int(row[0])
                type_vehicle = row[1]
                traveled_distance = float(row[2])
                avg_speed = float(row[3])
                vehicle_data.append({
                        'track_id': track_id,
                        'type': type_vehicle,
                        'traveled_d': traveled_distance,
                        'avg_speed': avg_speed
                    })

                for i in range(4, len(row), 6):
                        lat = float(row[i])
                        lon = float(row[i+1])
                        speed = float(row[i+2])
                        lon_acc = float(row[i+3])
                        lat_acc = float(row[i+4])
                        time = float(row[i+5])

                        vehicle_path_data.append({
                            'track_id': track_id,
                            'lat': lat,
                            'lon': lon,
                            'speed': speed,
                            'lon_acc': lon_acc,
                            'lat_acc': lat_acc,
                            'time': time
                        })
        return vehicle_data, vehicle_path_data
            
    except Exception as e:
            print(f"Error loading data from CSV: {e}")
            return [], []
