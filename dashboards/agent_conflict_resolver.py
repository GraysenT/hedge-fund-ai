Below is a Python script using Tkinter for creating a visual panel to track agent disagreements and resolution patterns. This script sets up a basic GUI where you can log disagreements, view them, and mark resolutions. It also includes simple statistics to observe patterns.

```python
import tkinter as tk
from tkinter import ttk, messagebox
import datetime

class DisagreementTracker:
    def __init__(self, root):
        self.root = root
        self.root.title("Agent Disagreement Tracker")

        # Data structure to store disagreements
        self.disagreements = []

        # Layout configuration
        self.setup_widgets()

    def setup_widgets(self):
        # Frames
        input_frame = ttk.Frame(self.root, padding="10")
        input_frame.grid(row=0, column=0, sticky=(tk.W, tk.E))

        list_frame = ttk.Frame(self.root, padding="10")
        list_frame.grid(row=1, column=0, sticky=(tk.W, tk.E))

        # Input area
        ttk.Label(input_frame, text="Disagreement Description:").grid(row=0, column=0)
        self.description_entry = ttk.Entry(input_frame, width=50)
        self.description_entry.grid(row=0, column=1)

        add_button = ttk.Button(input_frame, text="Add Disagreement", command=self.add_disagreement)
        add_button.grid(row=0, column=2)

        # Disagreement list
        self.disagreement_listbox = tk.Listbox(list_frame, height=10, width=100)
        self.disagreement_listbox.grid(row=1, column=0, columnspan=3)

        resolve_button = ttk.Button(list_frame, text="Mark as Resolved", command=self.resolve_disagreement)
        resolve_button.grid(row=2, column=1)

        # Status bar
        self.status_var = tk.StringVar()
        self.status_var.set("Total Disagreements: 0, Resolved: 0")
        status_label = ttk.Label(self.root, textvariable=self.status_var, relief=tk.SUNKEN, anchor="w")
        status_label.grid(row=2, column=0, sticky=(tk.W, tk.E))

    def add_disagreement(self):
        description = self.description_entry.get()
        if description:
            current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            entry = f"{current_time} - {description} [UNRESOLVED]"
            self.disagreements.append(entry)
            self.disagreement_listbox.insert(tk.END, entry)
            self.description_entry.delete(0, tk.END)
            self.update_status()

    def resolve_disagreement(self):
        selected_indices = self.disagreement_listbox.curselection()
        if not selected_indices:
            messagebox.showerror("Error", "Please select a disagreement to resolve.")
            return

        for i in selected_indices:
            item = self.disagreements[i]
            if "[RESOLVED]" not in item:
                self.disagreements[i] = item.replace("[UNRESOLVED]", "[RESOLVED]")
                self.disagreement_listbox.delete(i)
                self.disagreement_listbox.insert(i, self.disagreements[i])

        self.update_status()

    def update_status(self):
        total = len(self.disagreements)
        resolved = sum(1 for d in self.disagreements if "[RESOLVED]" in d)
        self.status_var.set(f"Total Disagreements: {total}, Resolved: {resolved}")

def main():
    root = tk.Tk()
    app = DisagreementTracker(root)
    root.mainloop()

if __name__ == "__main__":
    main()
```

This script creates a simple GUI with the following features:
- An entry widget to input new disagreements.
- A listbox to display current disagreements.
- Buttons to add a new disagreement and to mark selected disagreements as resolved.
- A status bar at the bottom showing the total number of disagreements and how many have been resolved.

This basic application can be expanded with more features like saving/loading data, more detailed statistics, and better handling of multiple selections for resolution.