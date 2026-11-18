import numpy as np
import matplotlib.pyplot as plt


# Modified UR5 dimensions (+5%), in metres
d = [0.09361695, 0, 0, 0.1146075, 0.0993825, 0.086415]
a = [0, -0.44625, -0.4118625, 0, 0, 0]
alpha = [90, 0, 0, 90, -90, 0]

# Joint angles, in degrees
q = [30, 45, 30, 20, 60, 90]


def dh_transform(theta, d_i, a_i, alpha_i):
    """Return a Standard DH homogeneous transformation matrix."""
    theta = np.radians(theta)
    alpha_i = np.radians(alpha_i)

    ct, st = np.cos(theta), np.sin(theta)
    ca, sa = np.cos(alpha_i), np.sin(alpha_i)

    return np.array([
        [ct, -st * ca, st * sa, a_i * ct],
        [st, ct * ca, -ct * sa, a_i * st],
        [0.0, sa, ca, d_i],
        [0.0, 0.0, 0.0, 1.0]
    ])


def calculate_frames():
    """Calculate base-to-frame transforms for frames 0 through 6."""
    transforms = [np.eye(4)]
    T = np.eye(4)

    for i in range(6):
        T = T @ dh_transform(q[i], d[i], a[i], alpha[i])
        transforms.append(T.copy())

    return transforms


def set_equal_axes(ax, points):
    """Set equal scale on the three plot axes."""
    mins = points.min(axis=0)
    maxs = points.max(axis=0)
    center = (mins + maxs) / 2
    radius = max((maxs - mins).max() / 2, 0.1)

    ax.set_xlim(center[0] - radius, center[0] + radius)
    ax.set_ylim(center[1] - radius, center[1] + radius)
    ax.set_zlim(center[2] - radius, center[2] + radius)


def main():
    frames = calculate_frames()
    origins = np.array([T[:3, 3] for T in frames])

    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111, projection="3d")

    # Draw links between consecutive DH frame origins.
    ax.plot(
        origins[:, 0], origins[:, 1], origins[:, 2],
        marker="o", linewidth=3, markersize=6,
        label="Link / frame origins"
    )

    # Draw the coordinate axes for each frame.
    axis_length = 0.08
    for i, T in enumerate(frames):
        origin = T[:3, 3]
        rotation = T[:3, :3]

        for j, axis_label in enumerate(("X", "Y", "Z")):
            direction = rotation[:, j] * axis_length
            ax.quiver(
                origin[0], origin[1], origin[2],
                direction[0], direction[1], direction[2],
                length=1, normalize=False
            )

        ax.text(origin[0], origin[1], origin[2], f"  {i}")

    end_position_mm = origins[-1] * 1000

    ax.set_title("Modified UR5 - Forward Kinematics")
    ax.set_xlabel("X (m)")
    ax.set_ylabel("Y (m)")
    ax.set_zlabel("Z (m)")
    ax.legend()
    set_equal_axes(ax, origins)

    print("End-effector position (mm):")
    print(f"X = {end_position_mm[0]:.3f}")
    print(f"Y = {end_position_mm[1]:.3f}")
    print(f"Z = {end_position_mm[2]:.3f}")

    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()
