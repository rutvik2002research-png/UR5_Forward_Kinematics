import numpy as np

# Modified UR5 dimensions (+5%), in metres
d = [0.09361695, 0, 0, 0.1146075, 0.0993825, 0.086415]
a = [0, -0.44625, -0.4118625, 0, 0, 0]
alpha = [90, 0, 0, 90, -90, 0]

# Given joint angles, in degrees
q = [30, 45, 30, 20, 60, 90]


# Standard Denavit-Hartenberg (DH) transformation matrix
def DH(theta, d, a, alpha):
    t = np.radians(theta)
    al = np.radians(alpha)

    ct, st = np.cos(t), np.sin(t)
    ca, sa = np.cos(al), np.sin(al)

    return np.array([
        [ct, -st * ca, st * sa, a * ct],
        [st, ct * ca, -ct * sa, a * st],
        [0, sa, ca, d],
        [0, 0, 0, 1]
    ])


# Forward kinematics
T = np.eye(4)

for i in range(6):
    A = DH(q[i], d[i], a[i], alpha[i])

    print(f"\nTransformation Matrix A{i + 1}:")
    print(np.round(A, 4))

    T = T @ A

print("\nFinal Transformation Matrix:")
print(np.round(T, 4))

print("\nEnd Effector Position (mm):")
print(np.round(T[:3, 3] * 1000, 3))
