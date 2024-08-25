import os
import tkinter as tk
from tkinter import filedialog, messagebox
from tensorflow.keras.models import load_model
from tensorflow.keras.utils import plot_model

def load_and_visualize_model():
    # Open a file dialog to select the model folder
    model_dir = filedialog.askdirectory(title="Select Model Folder")
    
    if not model_dir:
        return
    
    try:
        # Load the model
        model = load_model(model_dir)
        
        # Save the visualization to a file
        save_path = os.path.join(model_dir, 'model_visualization.png')
        plot_model(model, to_file=save_path, show_shapes=True, show_layer_names=True)
        
        # Inform the user that the model has been visualized
        messagebox.showinfo("Success", f"Model visualization saved to {save_path}")
    
    except Exception as e:
        # Show an error message if something goes wrong
        messagebox.showerror("Error", f"Failed to visualize model: {str(e)}")

# Set up the main application window
root = tk.Tk()
root.title("Model Visualizer")

# Create a button to trigger the model loading and visualization
load_button = tk.Button(root, text="Select Model Folder and Visualize", command=load_and_visualize_model)
load_button.pack(pady=20)

# Start the GUI event loop
root.mainloop()