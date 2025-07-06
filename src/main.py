import subprocess
import threading
import time
import tkinter as tk
from tkinter import ttk


class BTtoAUXApp(tk.Tk):
    """Simple Bluetooth audio GUI for 320x480 px touch display."""
    WIDTH = 320
    HEIGHT = 480

    def __init__(self):
        super().__init__()
        self.title("BTtoAUX")
        self.geometry(f"{self.WIDTH}x{self.HEIGHT}")
        self.configure(bg="#222222")
        # Placeholder state variables
        self.connected_device = tk.StringVar(value="No device")
        self.track_title = tk.StringVar(value="-")
        self.track_artist = tk.StringVar(value="-")
        self.track_progress = tk.DoubleVar(value=0.0)
        self.track_length = tk.StringVar(value="0:00")
        self.pin_request = tk.StringVar(value="")

        self.create_widgets()
        self.setup_bluetooth()
        threading.Thread(target=self.monitor_bluetooth, daemon=True).start()

    def create_widgets(self):
        # Connection status
        status_label = tk.Label(
            self,
            textvariable=self.connected_device,
            fg="white",
            bg="#444",
            font=("Arial", 12),
        )
        status_label.pack(fill="x", pady=5)

        # Track info frame
        info_frame = tk.Frame(self, bg="#222")
        info_frame.pack(fill="x", pady=10)
        tk.Label(
            info_frame,
            textvariable=self.track_title,
            fg="white",
            bg="#222",
            font=("Arial", 14, "bold"),
        ).pack()
        tk.Label(
            info_frame,
            textvariable=self.track_artist,
            fg="gray",
            bg="#222",
            font=("Arial", 12),
        ).pack()

        # Progress bar
        progress = ttk.Progressbar(
            self,
            variable=self.track_progress,
            maximum=100,
        )
        progress.pack(fill="x", padx=20)
        self.time_label = tk.Label(
            self,
            text="0:00 / 0:00",
            fg="white",
            bg="#222",
        )
        self.time_label.pack(pady=5)

        # Control buttons
        controls = tk.Frame(self, bg="#222")
        controls.pack(pady=10)
        self.prev_btn = tk.Button(controls, text="⏮", width=5)
        self.play_btn = tk.Button(controls, text="⏯", width=5)
        self.next_btn = tk.Button(controls, text="⏭", width=5)
        self.prev_btn.grid(row=0, column=0, padx=5)
        self.play_btn.grid(row=0, column=1, padx=5)
        self.next_btn.grid(row=0, column=2, padx=5)

        # Volume slider
        volume_frame = tk.Frame(self, bg="#222")
        volume_frame.pack(fill="x")
        tk.Label(
            volume_frame,
            text="Volume",
            fg="white",
            bg="#222",
        ).pack(side="left", padx=10)
        self.volume = tk.Scale(
            volume_frame,
            from_=0,
            to=100,
            orient="horizontal",
            length=180,
            bg="#222",
            fg="white",
        )
        self.volume.pack(side="left")

        # PIN entry
        self.pin_frame = tk.Frame(self, bg="#222")
        self.pin_label = tk.Label(
            self.pin_frame,
            text="Enter PIN: ",
            fg="white",
            bg="#222",
        )
        self.pin_entry = tk.Entry(self.pin_frame)
        self.pin_button = tk.Button(self.pin_frame, text="Confirm")
        self.pin_label.pack(side="left")
        self.pin_entry.pack(side="left")
        self.pin_button.pack(side="left")

    def setup_bluetooth(self):
        """Enable Bluetooth discoverability on startup."""
        commands = [
            ("bluetoothctl", "power", "on"),
            ("bluetoothctl", "pairable", "on"),
            ("bluetoothctl", "discoverable", "on"),
        ]
        for cmd in commands:
            try:
                subprocess.run(cmd, check=False, stdout=subprocess.DEVNULL,
                               stderr=subprocess.DEVNULL)
            except FileNotFoundError:
                # bluetoothctl not available; ignore errors
                pass

    def monitor_bluetooth(self):
        """Continuously update connection status."""
        while True:
            device = self._get_connected_device()
            self.connected_device.set(device or "No device")
            time.sleep(5)

    def _get_connected_device(self):
        """Return the name of the connected Bluetooth device if any."""
        try:
            output = subprocess.check_output(
                "bluetoothctl info", shell=True, stderr=subprocess.DEVNULL
            ).decode()
            if "Connected: yes" in output:
                for line in output.splitlines():
                    if line.strip().startswith("Name:"):
                        return line.split(":", 1)[1].strip()
                    if line.strip().startswith("Alias:"):
                        return line.split("Alias:", 1)[-1].strip()
        except (subprocess.CalledProcessError, FileNotFoundError):
            pass
        return None

    def show_pin_request(self, pin):
        self.pin_request.set(pin)
        self.pin_frame.pack(pady=10)

    def hide_pin_request(self):
        self.pin_frame.pack_forget()

    def update_time(self, current, total):
        self.time_label.config(text=f"{current} / {total}")


def main():
    app = BTtoAUXApp()
    app.mainloop()


if __name__ == "__main__":
    main()
