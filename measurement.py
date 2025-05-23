class Measurement:
    def __init__(self, date: str, height: str, pressure: str):
        self.date = date
        self.height_raw = height
        self.pressure_raw = pressure

        self.is_valid_height = self._validate_height()
        self.is_valid_pressure = self._validate_pressure()

    def _validate_height(self):
        try:
            self.height = float(self.height_raw)
            return True
        except ValueError:
            self.height = self.height_raw  #оставим как строку
            return False

    def _validate_pressure(self):
        try:
            self.pressure = int(self.pressure_raw)
            return True
        except ValueError:
            self.pressure = self.pressure_raw  #оставим как строку
            return False

    def update(self, date: str, height: str, pressure: str):
        self.date = date
        self.height_raw = height
        self.pressure_raw = pressure
        self.is_valid_height = self._validate_height()
        self.is_valid_pressure = self._validate_pressure()
