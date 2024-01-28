import matplotlib.pyplot as plt

def plot_series(x, y, format="-", start=0, end=None, 
                title=None, xlabel=None, ylabel=None, legend=None):
    """
    Visualizes time series data and returns the figure object.
    """
    # Create a figure object
    fig, ax = plt.subplots(figsize=(10, 6))

    # Check if there are more than two series to plot
    if type(y) is tuple:
        # Loop over the y elements
        for y_curr in y:
            # Plot the x and current y values
            ax.plot(x[start:end], y_curr[start:end], format)
    else:
        # Plot the x and y values
        ax.plot(x[start:end], y[start:end], format)

    # Set labels and title
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.set_title(title)

    # Set the legend
    if legend:
        ax.legend(legend)

    # Overlay a grid
    ax.grid(True)

    # Return the figure object
    return fig

