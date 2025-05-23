import customtkinter as ctk
from measurement import Measurement
from edit_window import EditWindow


class MainWindow(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Измерения давления")
        self.geometry("600x400+500+300")

        self.measurements = []

        self.date_entry = ctk.CTkEntry(self, placeholder_text="Дата")
        self.date_entry.pack(pady=5)

        self.height_entry = ctk.CTkEntry(self, placeholder_text="Высота")
        self.height_entry.pack(pady=5)

        self.pressure_entry = ctk.CTkEntry(self, placeholder_text="Давление")
        self.pressure_entry.pack(pady=5)

        add_button = ctk.CTkButton(self, text="Добавить", command=self.add_measurement)
        add_button.pack(pady=10)

        self.table_frame = ctk.CTkScrollableFrame(self)
        self.table_frame.pack(expand=True, fill="both", pady=10)

        self.refresh_table()

    def add_measurement(self):
        m = Measurement(
            self.date_entry.get(),
            self.height_entry.get(),  # строки, как есть
            self.pressure_entry.get()
        )
        self.measurements.append(m)
        self.refresh_table()

    def refresh_table(self):
        for widget in self.table_frame.winfo_children():
            widget.destroy()

        for i, m in enumerate(self.measurements):
            row_text = f"{m.date} | {m.height} | {m.pressure}"
            if not (m.is_valid_height and m.is_valid_pressure):
                row_text += "  ⚠️"

            label = ctk.CTkLabel(self.table_frame, text=row_text,
                                 text_color="red" if not (m.is_valid_height and m.is_valid_pressure) else "white")
            label.grid(row=i, column=0, padx=5, pady=5, sticky="w")

            edit_btn = ctk.CTkButton(self.table_frame, text="Редактировать", width=100,
                                     command=lambda m=m: self.open_edit_window(m))
            edit_btn.grid(row=i, column=1, padx=5)

            del_btn = ctk.CTkButton(self.table_frame, text="Удалить", width=80,
                                    command=lambda m=m: self.delete_measurement(m))
            del_btn.grid(row=i, column=2, padx=5)

    def open_edit_window(self, measurement):
        EditWindow(self, measurement, self.refresh_table)

    def delete_measurement(self, measurement):
        self.measurements.remove(measurement)
        self.refresh_table()
