import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.title('Interactive Model: Uniformly Charged Sphere (Gauss Law)')
st.write("Adjust the values of the Sphere Radius (a) and Observation Point (r) to see the Gaussian surface and the graph change accordingly.")

# Input sliders
a = st.slider('Sphere Radius (a)', min_value=0.1, max_value=5.0, value=2.0, step=0.1)
r_point = st.slider('Gaussian Surface Radius (r)', min_value=0.1, max_value=10.0, value=1.0, step=0.1)
rho_0 = 1.0  

# Function to calculate Electric Flux Density (D)
def calculate_D(r, a, rho_0):
    if r <= a:
        return (r * rho_0) / 3
    else:
        return (a**3 * rho_0) / (3 * r**2)

# --- Section 1: Visual Representation of the Sphere and Gaussian Surface ---
st.subheader("Visual Representation")
fig_circles, ax_circles = plt.subplots(figsize=(6, 6))

# Draw the charged sphere (Solid light blue circle)
circle_a = plt.Circle((0, 0), a, color='skyblue', alpha=0.7, label='Charged Sphere')
ax_circles.add_patch(circle_a)

# Draw the Gaussian surface (Dashed black circle)
circle_r = plt.Circle((0, 0), r_point, color='black', fill=False, linestyle='--', linewidth=2, label='Gaussian Surface')
ax_circles.add_patch(circle_r)

# Fix the axes limits so the circles visually grow and shrink inside a static frame
ax_circles.set_xlim(-10, 10)
ax_circles.set_ylim(-10, 10)
ax_circles.set_aspect('equal')
ax_circles.grid(True, linestyle=':', alpha=0.6)
ax_circles.legend(loc='upper right')

# Display the circles plot
st.pyplot(fig_circles)

# --- Section 2: Electric Flux Density Graph ---
st.subheader("Electric Flux Density (D) vs Distance (r)")
fig_graph, ax_graph = plt.subplots(figsize=(8, 4))
r_vals = np.linspace(0.1, 10, 500)
D_vals = [calculate_D(rv, a, rho_0) for rv in r_vals]

# Plot the main curve
ax_graph.plot(r_vals, D_vals, lw=2, color='blue', label='Electric Flux Density (D)')

# Plot the moving point
current_D = calculate_D(r_point, a, rho_0)
ax_graph.plot(r_point, current_D, 'ro', markersize=8, label=f'r = {r_point}, D = {current_D:.2f}')

# Graph settings
ax_graph.set_xlim(0, 10)
ax_graph.set_ylim(0, max(D_vals) + 0.2)
ax_graph.set_xlabel('Distance (r)')
ax_graph.set_ylabel('D')
ax_graph.grid(True)
ax_graph.legend()

# Display the graph plot
st.pyplot(fig_graph)
