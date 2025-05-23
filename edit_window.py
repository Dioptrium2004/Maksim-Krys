import customtkinter as ctk


class EditWindow(ctk.CTkToplevel):
    def __init__(self, parent, measurement, on_save_callback):
        super().__init__(parent)
        self.title("Редактировать измерение")
        self.geometry("300x200+500+300")

        self.measurement = measurement
        self.on_save_callback = on_save_callback

        self.date_entry = ctk.CTkEntry(self, placeholder_text="Дата")
        self.date_entry.insert(0, measurement.date)
        self.date_entry.pack(pady=5)

        self.height_entry = ctk.CTkEntry(self, placeholder_text="Высота")
        self.height_entry.insert(0, str(measurement.height_raw))
        self.height_entry.pack(pady=5)

        self.pressure_entry = ctk.CTkEntry(self, placeholder_text="Давление")
        self.pressure_entry.insert(0, str(measurement.pressure_raw))
        self.pressure_entry.pack(pady=5)

        save_button = ctk.CTkButton(self, text="Сохранить", command=self.save)
        save_button.pack(pady=10)

        # Сделать окно модальным и на переднем плане
        self.transient(parent)
        self.grab_set()
        self.focus()
        self.wait_window(self)

    def save(self):
        self.measurement.update(
            self.date_entry.get(),
            self.height_entry.get(),
            self.pressure_entry.get()
        )
        self.on_save_callback()
        self.destroy()
