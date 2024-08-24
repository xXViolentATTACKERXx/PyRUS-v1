import tkinter as tk
import random
import time
import math
import winsound

# Utility Functions
def random_color():
    """Generate a random color."""
    return f'#{random.randint(0, 0xFFFFFF):06x}'

def random_text(length=20):
    """Generate a random text string."""
    return ''.join(random.choices('HAHAHAHAHAHAHAHAHAHAHAH', k=length))

def random_position(width, height, obj_width, obj_height):
    """Generate a random position for placing an object."""
    x = random.randint(0, max(0, width - obj_width))
    y = random.randint(0, max(0, height - obj_height))
    return x, y

def play_sound(file_path):
    """Play a sound file."""
    winsound.PlaySound(file_path, winsound.SND_ASYNC)

# Drawing Functions
def draw_shapes(canvas, shape_type, count=10, max_size=100):
    """Draw random shapes on the canvas."""
    for _ in range(count):
        x1, y1 = random.randint(0, canvas.winfo_width()), random.randint(0, canvas.winfo_height())
        x2, y2 = random.randint(0, canvas.winfo_width()), random.randint(0, canvas.winfo_height())
        color = random_color()
        width = random.randint(1, 10)
        
        if shape_type == 'rectangle':
            canvas.create_rectangle(x1, y1, x2, y2, outline=color, fill='', width=width)
        elif shape_type == 'line':
            canvas.create_line(x1, y1, x2, y2, fill=color, width=width)
        elif shape_type == 'oval':
            canvas.create_oval(x1, y1, x2, y2, outline=color, fill='', width=width)
        elif shape_type == 'arc':
            canvas.create_arc(x1, y1, x2, y2, start=random.randint(0, 360), extent=random.randint(0, 180),
                              outline=color, fill='', width=width)
        elif shape_type == 'polygon':
            points = [random.randint(0, canvas.winfo_width()) for _ in range(6)]
            canvas.create_polygon(points, outline=color, fill='', width=width)

def draw_background(canvas, count=30):
    """Draw a funky background effect on the canvas."""
    for _ in range(count):
        x1, y1 = random.randint(0, canvas.winfo_width()), random.randint(0, canvas.winfo_height())
        x2, y2 = random.randint(x1, canvas.winfo_width()), random.randint(y1, canvas.winfo_height())
        color = random_color()
        canvas.create_rectangle(x1, y1, x2, y2, fill=color, outline='', stipple='gray50')

def draw_animated_shapes(canvas, start_time, count=15):
    """Draw animated shapes with changing properties."""
    elapsed_time = time.time() - start_time
    for _ in range(count):
        x1, y1 = random.randint(0, canvas.winfo_width()), random.randint(0, canvas.winfo_height())
        x2, y2 = random.randint(x1, canvas.winfo_width()), random.randint(y1, canvas.winfo_height())
        color = random_color()
        width = random.randint(1, 15)
        shape = random.choice(['rectangle', 'line', 'oval'])
        
        if shape == 'rectangle':
            canvas.create_rectangle(x1 + elapsed_time % 100, y1 + elapsed_time % 100,
                                    x2 + elapsed_time % 100, y2 + elapsed_time % 100,
                                    outline=color, fill='', width=width)
        elif shape == 'line':
            canvas.create_line(x1 + elapsed_time % 100, y1 + elapsed_time % 100,
                               x2 + elapsed_time % 100, y2 + elapsed_time % 100,
                               fill=color, width=width)
        elif shape == 'oval':
            canvas.create_oval(x1 + elapsed_time % 100, y1 + elapsed_time % 100,
                               x2 + elapsed_time % 100, y2 + elapsed_time % 100,
                               outline=color, fill='', width=width)

        # Additional animated effects
        for _ in range(random.randint(1, 5)):
            angle = random.uniform(0, 360)
            offset = random.randint(0, 100)
            canvas.create_line(x1, y1, x1 + offset * math.cos(math.radians(angle)), 
                               y1 + offset * math.sin(math.radians(angle)),
                               fill=random_color(), width=random.randint(1, 10))

def simulate_transparency(canvas, count=20):
    """Simulate transparency effect with overlapping colors."""
    for _ in range(count):
        x1, y1 = random.randint(0, canvas.winfo_width()), random.randint(0, canvas.winfo_height())
        x2, y2 = random.randint(x1, canvas.winfo_width()), random.randint(y1, canvas.winfo_height())
        color = random_color()
        canvas.create_rectangle(x1, y1, x2, y2, fill=color, outline='', stipple='gray50')

def add_geometric_glitches(canvas, count=15):
    """Add geometric glitches with random shapes and distortions."""
    for _ in range(count):
        x1, y1 = random.randint(0, canvas.winfo_width()), random.randint(0, canvas.winfo_height())
        x2, y2 = random.randint(x1, canvas.winfo_width()), random.randint(y1, canvas.winfo_height())
        color = random_color()
        shape = random.choice(['rectangle', 'line', 'oval', 'arc'])
        distortion = random.randint(-30, 30)
        
        if shape == 'rectangle':
            canvas.create_rectangle(x1 + distortion, y1 + distortion, x2 + distortion, y2 + distortion,
                                    outline=color, fill='', width=random.randint(1, 15))
        elif shape == 'line':
            canvas.create_line(x1 + distortion, y1 + distortion, x2 + distortion, y2 + distortion,
                               fill=color, width=random.randint(1, 15))
        elif shape == 'oval':
            canvas.create_oval(x1 + distortion, y1 + distortion, x2 + distortion, y2 + distortion,
                               outline=color, fill='', width=random.randint(1, 15))
        elif shape == 'arc':
            canvas.create_arc(x1 + distortion, y1 + distortion, x2 + distortion, y2 + distortion,
                              start=random.randint(0, 360), extent=random.randint(0, 180),
                              outline=color, fill='', width=random.randint(1, 15))

def add_flickering_effect(canvas, count=20):
    """Add flickering effects to the canvas."""
    for _ in range(count):
        x1, y1 = random.randint(0, canvas.winfo_width()), random.randint(0, canvas.winfo_height())
        x2, y2 = random.randint(x1, canvas.winfo_width()), random.randint(y1, canvas.winfo_height())
        color = random_color()
        canvas.create_rectangle(x1, y1, x2, y2, fill=color, outline='', stipple='gray75')

def create_noise_labels(window, color, count=30):
    """Create random noise labels on the window."""
    for _ in range(count):
        noise_font_size = random.randint(10, 70)
        noise_label = tk.Label(window, text=random_text(), font=("Helvetica", noise_font_size),
                              fg=random_color(), bg=color)
        noise_width = noise_label.winfo_reqwidth()
        noise_height = noise_label.winfo_reqheight()
        noise_x, noise_y = random_position(window.winfo_width(), window.winfo_height(), noise_width, noise_height)
        noise_label.place(x=noise_x, y=noise_y)
        noise_label.after(random.randint(100, 1000), noise_label.destroy)

def draw_moving_shapes(canvas, start_time, count=10):
    """Draw moving shapes that animate over time."""
    elapsed_time = time.time() - start_time
    for _ in range(count):
        shape_type = random.choice(['rectangle', 'line', 'oval'])
        x1, y1 = random.randint(0, canvas.winfo_width()), random.randint(0, canvas.winfo_height())
        x2, y2 = random.randint(x1, canvas.winfo_width()), random.randint(y1, canvas.winfo_height())
        color = random_color()
        width = random.randint(1, 15)
        movement = int(elapsed_time * 10) % 100
        
        if shape_type == 'rectangle':
            canvas.create_rectangle(x1 + movement, y1 + movement, x2 + movement, y2 + movement,
                                    outline=color, fill='', width=width)
        elif shape_type == 'line':
            canvas.create_line(x1 + movement, y1 + movement, x2 + movement, y2 + movement,
                               fill=color, width=width)
        elif shape_type == 'oval':
            canvas.create_oval(x1 + movement, y1 + movement, x2 + movement, y2 + movement,
                               outline=color, fill='', width=width)

def update_window(start_time):
    """Update the window with various glitch effects and sounds."""
    while True:
        color = random_color()
        canvas.config(bg=color)
        
        text = random_text()
        label.config(text=text, fg=random_color())
        label_width = label.winfo_reqwidth()
        label_height = label.winfo_reqheight()
        x, y = random_position(window.winfo_width(), window.winfo_height(), label_width, label_height)
        label.place(x=x, y=y)
        
        font_size = random.randint(20, 100)
        label.config(font=("Helvetica", font_size))
        
        canvas.delete('all')
        
        draw_background(canvas)
        draw_shapes(canvas, shape_type='rectangle', count=15)
        draw_shapes(canvas, shape_type='line', count=15)
        draw_shapes(canvas, shape_type='oval', count=10)
        draw_shapes(canvas, shape_type='arc', count=10)
        draw_shapes(canvas, shape_type='polygon', count=5)
        draw_animated_shapes(canvas, start_time)
        simulate_transparency(canvas)
        add_geometric_glitches(canvas)
        add_flickering_effect(canvas)
        create_noise_labels(window, color)
        draw_moving_shapes(canvas, start_time)
        
        # Play a random sound effect
        play_sound('glitch_sound.wav')
        
        window.update()
        time.sleep(random.uniform(0.05, 0.2))

# Setup the window
def setup_window():
    """Initialize the main window for the glitch effect."""
    window = tk.Tk()
    window.title("Simulated Transparency Glitch Effect")
    window.attributes('-fullscreen', True)
    #window.bind('<Escape>', lambda e: window.destroy())  # Allow exit with Escape key
    
    label = tk.Label(window, font=("Helvetica", 50))
    label.pack(expand=True)
    
    canvas = tk.Canvas(window, bg='black')
    canvas.pack(fill=tk.BOTH, expand=True)
    
    return window, label, canvas

# Initialize main window and start glitch effect
window, label, canvas = setup_window()
start_time = time.time()
window.after(100, lambda: update_window(start_time))

window.mainloop()
