import numpy as np
from scipy.integrate import solve_ivp
import plotly.graph_objects as go
import icecream as ic


def lorenz(t, state, sigma=10.0, rho=28.0, beta=8.0 / 3.0):
    x, y, z = state
    dx = sigma * (y - x)
    dy = x * (rho - z) - y
    dz = x * y - beta * z
    return [dx, dy, dz]


def solve_lorenz(initial_state, t_span=(0, 50), steps=10000):
    t_eval = np.linspace(*t_span, steps)
    solution = solve_ivp(lorenz, t_span, initial_state, t_eval=t_eval)
    # ic(solution)
    # ic(soulution.y)
    return solution.y


def create_lorenz_figure(x, y, z):
    x_first, y_first, z_first = x[0], y[0], z[0]
    x_last, y_last, z_last = x[-1], y[-1], z[-1]

    first_point_label = f"Початкова точка ({x_first:.6f}, {y_first:.6f}, {z_first:.6f})"
    last_point_label = f"Остання точка ({x_last:.6f}, {y_last:.6f}, {z_last:.6f})"

    fig = go.Figure()
    # ic(fig)

    fig.add_trace(go.Scatter3d(
        x=x, y=y, z=z,
        mode='lines',
        name='Траєкторія',
        line=dict(color='blue', width=2)
    ))

    fig.add_trace(go.Scatter3d(
        x=[x_first], y=[y_first], z=[z_first],
        mode='markers',
        marker=dict(size=6, color='green'),
        name=first_point_label
    ))

    fig.add_trace(go.Scatter3d(
        x=[x_last], y=[y_last], z=[z_last],
        mode='markers',
        marker=dict(size=6, color='red'),
        name=last_point_label
    ))

    fig.update_layout(
        scene=dict(
            xaxis_title='X',
            yaxis_title='Y',
            zaxis_title='Z'
        ),
        title="Атрактор Лоренца"
    )

    return fig


def generate_lorenz_plot(initial_state):
    x, y, z = solve_lorenz(initial_state)
    fig = create_lorenz_figure(x, y, z)
    # fig.show()
    fig.write_html(r"C:\Users\GeerBeen\PycharmProjects\KFC\Practise4\static\lorenz.html")


if __name__ == '__main__':
    generate_lorenz_plot([1.0, 1.0, 1.0])
