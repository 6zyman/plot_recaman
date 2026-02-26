import turtle
from PIL import Image

def recaman(n):
    """Generate Recamán sequence of size n"""
    sequence = [0]
    seen = {0}
    
    for i in range(1, n):
        prev = sequence[-1]
        back = prev - i
        
        if back > 0 and back not in seen:
            sequence.append(back)
            seen.add(back)
        else:
            forward = prev + i
            sequence.append(forward)
            seen.add(forward)
    
    return sequence

def plot_recaman(n):
    """Plot Recamán sequence using turtle"""
    sequence = recaman(n)
    
    print(sequence)  # Print the sequence
    
    screen = turtle.Screen()
    t = turtle.Turtle()
    t.speed(0)
    t.penup()
    t.pensize(3)
    t.goto(-750, 0)
    screen.bgcolor("black")
   
    t.setheading(90)
      # Point upwards
    
    # Draw the sequence
    for i in range(len(sequence)-1):
        t.pendown()
        if sequence[i+1]- sequence[i] > 0:     
            t.setheading(270)
            t.pencolor("Red")
        else:
            t.setheading(90)
            t.pencolor("green")
        t.circle((i+1)*3,180)  # Draw a semicircle
        t.penup()
    
    turtle.done()


# Generate and plot
plot_recaman(112)