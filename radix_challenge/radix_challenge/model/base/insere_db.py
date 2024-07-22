class InsertDb():
    def insert_sensor_data(self):
        query = """
                INSERT INTO ADMRADIX.SENSOR_DATA 
                    (sensorId, equipmentId, timestamp, value) 
                VALUES 
                    (ADMRADIX.SENSOR_ID_SEQ.NEXTVAL, :equipmentId, :timestamp, :value)
        """
        return query