import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, PillowWriter
from config import START, GOAL
import os

def animate(maze, snapshots, path,elapsed_time, algorithm_name):
    fig, ax = plt.subplots()

    def update(frame):
        ax.clear()
        ax.set_xticks([])
        ax.set_yticks([])
        ax.imshow(maze, cmap='gray_r')

        for i in range(min(frame, len(snapshots))):
            y, x = snapshots[i]
            ax.plot(x, y, 'o', color='lightgray', markersize=4)

        if frame >= len(snapshots):
            for (y, x) in path:
                ax.plot(x, y, 'o', color='blue', markersize=4)

        sy, sx = START
        gy, gx = GOAL
        ax.plot(sx, sy, 's', color='blue', markersize=8)
        ax.plot(gx, gy, 's', color='green', markersize=8)
    
    total_frames = len(snapshots) + len(path)
    ani = FuncAnimation(fig, update, frames=total_frames, interval=50)

    # Create directory if it doesn't exist
    save_dir = os.path.join("results/search based algorithms", algorithm_name)
    os.makedirs(save_dir, exist_ok=True)

    # Save video as .mp4 and .gif
    mp4_path = os.path.join(save_dir, f"{algorithm_name}.mp4")
    gif_path = os.path.join(save_dir, f"{algorithm_name}.gif")

    print(f"Saving MP4 to {mp4_path}")
    ani.save(mp4_path, writer='ffmpeg', fps=20)

    gif_fps = max(1, int(total_frames / 3))  # Ensure at least 1 fps
    print(f"Saving GIF to {gif_path} with fps={gif_fps} ")
    ani.save(gif_path, writer=PillowWriter(fps=gif_fps))
    # Save static image of final result
    fig_final, ax_final = plt.subplots()
    ax_final.set_xticks([])
    ax_final.set_yticks([])
    ax_final.imshow(maze, cmap='gray_r')

    for (y, x) in snapshots:
        ax_final.plot(x, y, 'o', color='lightgray', markersize=4)

    for (y, x) in path:
        ax_final.plot(x, y, 'o', color='blue', markersize=4)

    sy, sx = START
    gy, gx = GOAL
    ax_final.plot(sx, sy, 's', color='blue', markersize=8)
    ax_final.plot(gx, gy, 's', color='green', markersize=8)

    # Add title with algorithm name and time
    if elapsed_time is not None:
        ax_final.set_title(f"{algorithm_name.upper()} - Time: {elapsed_time:.4f} s")
    else:
        ax_final.set_title(algorithm_name.upper())

    image_path = os.path.join(save_dir, f"{algorithm_name}_final.png")
    print(f"Saving final static image to {image_path}")
    fig_final.savefig(image_path, bbox_inches='tight', dpi=150)
    plt.close(fig_final)
    plt.show()

    plt.close(fig)



