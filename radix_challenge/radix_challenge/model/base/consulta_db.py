class QueryDb():
    def get_sensor_data_avg_day(self):
        query = """
                SELECT
                    equipmentId,
                    AVG(value) AS average_value
                FROM
                    admradix.sensor_data
                WHERE
                    timestamp >= SYSDATE - INTERVAL '1' DAY
                GROUP BY
                    equipmentId;
        """
        return query
    
    def get_sensor_data_avg_twodays(self):
        query = """
                SELECT
                    equipmentId,
                    AVG(value) AS average_value
                FROM
                    admradix.sensor_data
                WHERE
                    timestamp >= SYSDATE - INTERVAL '2' DAY
                GROUP BY
                    equipmentId;
        """
        return query
    
    def get_sensor_data_avg_week(self):
        query = """
                SELECT
                    equipmentId,
                    AVG(value) AS average_value
                FROM
                    admradix.sensor_data
                WHERE
                    timestamp >= SYSDATE - INTERVAL '7' DAY
                GROUP BY
                    equipmentId;
        """
        return query
    
    def get_sensor_data_avg_month(self):
        query = """
                SELECT
                    equipmentId,
                    AVG(value) AS average_value
                FROM
                    admradix.sensor_data
                WHERE
                    timestamp >= ADD_MONTHS(SYSDATE, -1)
                GROUP BY
                    equipmentId;
        """
        return query