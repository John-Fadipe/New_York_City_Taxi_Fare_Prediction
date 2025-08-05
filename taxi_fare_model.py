class TaxiFareModel:
    def __init__(self, model):
        self.model = model

    def haversine_np(self, long1, lat1, long2, lat2):
        import numpy as np
        long1, lat1, long2, lat2 = map(np.radians, [long1, lat1, long2, lat2])
        dlon = long2 - long1
        dlat = lat2 - lat1
        a = np.sin(dlat/2.0)**2 + np.cos(lat1) * np.cos(lat2) * np.sin(dlon/2.0)**2
        c = 2 * np.arcsin(np.sqrt(a))
        return 6367 * c

    def compute_landmark_distances(self, dropoff_long, dropoff_lat):
        landmarks = {
            "jfk": (-73.7781, 40.6413),
            "lga": (-73.8740, 40.7769),
            "ewr": (-74.1745, 40.6895),
            "met": (-73.9632, 40.7794),
            "wtc": (-74.0134, 40.7115),
        }
        distances = {}
        for name, (lon, lat) in landmarks.items():
            dist = self.haversine_np(dropoff_long, dropoff_lat, lon, lat)
            distances[f"{name}_drop_distance"] = dist
        return distances

    def extract_datetime_features(self, dt):
        return {
            "pickup_datetime_year": dt.year,
            "pickup_datetime_month": dt.month,
            "pickup_datetime_day": dt.day,
            "pickup_datetime_weekday": dt.weekday(),
            "pickup_datetime_hour": dt.hour,
        }

    def get_coordinates(self, address):
        from geopy.geocoders import Nominatim
        from geopy.exc import GeocoderTimedOut
        geolocator = Nominatim(user_agent = "nyc_taxi_app")
        try:
            location = geolocator.geocode(address)
            if location:
                return location.longitude, location.latitude
            else:
                raise ValueError(f"Could not geocode address: {address}")
        except GeocoderTimedOut:
            raise RuntimeError("Geocoding timed out")

    def preprocess_input(self, pickup_address, dropoff_address, passenger_count, pickup_datetime = None):
        from datetime import datetime
        import pandas as pd

        if pickup_datetime is None:
            pickup_datetime = datetime.now()

        pickup_long, pickup_lat = self.get_coordinates(pickup_address)
        dropoff_long, dropoff_lat = self.get_coordinates(dropoff_address)

        trip_distance = self.haversine_np(pickup_long, pickup_lat, dropoff_long, dropoff_lat)
        landmark_distances = self.compute_landmark_distances(dropoff_long, dropoff_lat)
        datetime_features = self.extract_datetime_features(pickup_datetime)

        features = {
            "pickup_longitude": pickup_long,
            "pickup_latitude": pickup_lat,
            "dropoff_longitude": dropoff_long,
            "dropoff_latitude": dropoff_lat,
            "passenger_count": passenger_count,
            "trip_distance": trip_distance,
            **datetime_features,
            **landmark_distances
        }

        model_input_columns = [
            'pickup_longitude', 'pickup_latitude',
            'dropoff_longitude', 'dropoff_latitude',
            'passenger_count',
            'pickup_datetime_year', 'pickup_datetime_month', 'pickup_datetime_day',
            'pickup_datetime_weekday', 'pickup_datetime_hour',
            'trip_distance',
            'jfk_drop_distance', 'lga_drop_distance', 'ewr_drop_distance',
            'met_drop_distance', 'wtc_drop_distance'
        ]

        return pd.DataFrame([features])[model_input_columns]

    def predict(self, pickup_address, dropoff_address, passenger_count, pickup_datetime = None):
        X = self.preprocess_input(pickup_address, dropoff_address, passenger_count, pickup_datetime)
        return self.model.predict(X)[0]