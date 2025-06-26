import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the steps for converting 171 into binary:
# Division steps:
# 171 / 2 = 85 remainder 1
# 85  / 2 = 42 remainder 1
# 42  / 2 = 21 remainder 0
# 21  / 2 = 10 remainder 1
# 10  / 2 = 5  remainder 0
# 5   / 2 = 2  remainder 1
# 2   / 2 = 1  remainder 0
# 1   / 2 = 0  remainder 1
dividends = [171, 85, 42, 21, 10, 5, 2, 1]
remainders = [1, 1, 0, 1, 0, 1, 0, 1]  # These are the remainders (in order of computation)

fig, ax = plt.subplots(figsize=(6, 4))
ax.axis("off")
text = ax.text(0.5, 0.5, "", ha="center", va="center", fontsize=14, transform=ax.transAxes)

def init():
    text.set_text("")
    return (text,)

def animate(i):
    # For each division step, show the current state
    if i < len(dividends):
        dividend = dividends[i]
        remainder = remainders[i]
        # Accumulate remainders so far (the final binary number will be the remainders in reverse order)
        binary_current = "".join(str(r) for r in remainders[:i+1])[::-1]
        message = (f"Step {i+1}:\n"
                   f"Dividend: {dividend}\n"
                   f"Division by 2 gives remainder: {remainder}\n"
                   f"Binary so far (reversed): {binary_current}")
    else:
        # After all steps, display the final result
        final_binary = "".join(str(r) for r in remainders[::-1])
        message = f"Conversion complete!\n171 in binary is: {final_binary}"
    text.set_text(message)
    return (text,)

# Create the animation (frames: one for each step plus a few extra to show the final result)
anim = animation.FuncAnimation(fig, animate, init_func=init,
                               frames=len(dividends) + 5, interval=1500, blit=True)

# Save the animation as a GIF file
anim.save("binary_conversion.gif", writer="pillow")
plt.show()


