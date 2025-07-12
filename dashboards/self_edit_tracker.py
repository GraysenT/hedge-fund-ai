Here's a Python script that implements a live diff viewer using a simple GUI. This script uses the `tkinter` library for the GUI and the `difflib` library to compute differences between text versions. It allows the user to input original text and edited text, then displays the differences in real-time.

```python
import tkinter as tk
from difflib import ndiff

def update_diff():
    original_text = original_text_box.get("1.0", tk.END)
    edited_text = edited_text_box.get("1.0", tk.END)
    diff = ndiff(original_text.splitlines(keepends=True), edited_text.splitlines(keepends=True))
    diff_text = ''.join(diff)
    diff_label.config(state=tk.NORMAL)
    diff_label.delete("1.0", tk.END)
    diff_label.insert("1.0", diff_text)
    diff_label.config(state=tk.DISABLED)

def setup_window():
    window = tk.Tk()
    window.title("Live Diff Viewer")

    global original_text_box
    global edited_text_box
    global diff_label

    tk.Label(window, text="Original Text:").pack()
    original_text_box = tk.Text(window, height=10, width=50)
    original_text_box.pack()

    tk.Label(window, text="Edited Text:").pack()
    edited_text_box = tk.Text(window, height=10, width=50)
    edited_text_box.pack()

    tk.Button(window, text="Show Differences", command=update_diff).pack()

    tk.Label(window, text="Differences:").pack()
    diff_label = tk.Text(window, height=10, width=50, state=tk.DISABLED, bg='light grey')
    diff_label.pack()

    return window

if __name__ == "__main__":
    root = setup_window()
    root.mainloop()
```

### How It Works:
1. **GUI Setup:** The script creates a simple GUI with two text areas for the original and edited texts and a button to trigger the diff update.
2. **Diff Calculation:** When the user clicks the "Show Differences" button, the script fetches the text from both text areas, computes the differences using `ndiff` from the `difflib` library, and displays the result in another text area.
3. **Real-time Update:** The diff update needs to be triggered manually by the button. For real-time updates without clicking, you could add event bindings to the text boxes to call `update_diff` on text change.

This script provides a basic framework for a diff viewer, which can be extended or modified according to specific needs, such as adding more complex text processing features or improving the user interface.