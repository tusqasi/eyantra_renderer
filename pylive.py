import matplotlib.pyplot as plt
import numpy as np

# use ggplot style for more sophisticated visuals
plt.style.use("ggplot")

def live_bar(ir_values, ax, title="", pause_time=0.1):
    # this is the call to matplotlib that allows dynamic plotting
    plt.ion()
    if ax == -1:
        ax = plt.bar(list(range(5)), [1000]*5)
        print("first run")
    else:
        for i,data in enumerate(ir_values):
            ax.patches[i].set_height(data)

    plt.ylabel("ACTIVATION")
    plt.title(title)
    plt.show()
    plt.pause(pause_time)

    return ax

def live_plotter(x_vec, y_mat, lines, title="", pause_time=0.1):
    if -1 in lines:
        # this is the call to matplotlib that allows dynamic plotting
        plt.ion()
        fig = plt.figure(figsize=(13, 6))
        ax = fig.add_subplot(111)
        # create a variable for the line so we can later update it
        lines = [ax.plot(x_vec, y_data)[0] for y_data in y_mat]
        # update plot label/title
        plt.ylabel("IR values")
        plt.xlabel("Time")
        plt.title(title)
        plt.show()

    # after the figure, axis, and line are created, we only need to update the y-data
    for line, y_data in zip(lines, y_mat):
        line.set_ydata(y_data)
    # adjust limits if new data goes beyond bounds
    for line, y_data in zip(lines, y_mat):
        if (
            np.min(y_data) <= line.axes.get_ylim()[0]
            or np.max(y_data) >= line.axes.get_ylim()[1]
        ):
            plt.ylim([np.min(y_data) - np.std(y_data), np.max(y_data) + np.std(y_data)])
    # this pauses the data so the figure/axis can catch up - the amount of pause can be altered above
    plt.pause(pause_time)

    # return line so we can update it again in the next iteration
    return lines


# the function below is for updating both x and y values (great for updating dates on the x-axis)
def live_plotter_xy(x_vec, y1_data, line1, identifier="", pause_time=0.01):
    if line1 == []:
        plt.ion()
        fig = plt.figure(figsize=(13, 6))
        ax = fig.add_subplot(111)
        (line1,) = ax.plot(x_vec, y1_data, "r-o", alpha=0.8)
        plt.ylabel("Y Label")
        plt.title("Title: {}".format(identifier))
        plt.show()

    line1.set_data(x_vec, y1_data)
    plt.xlim(np.min(x_vec), np.max(x_vec))
    if (
        np.min(y1_data) <= line1.axes.get_ylim()[0]
        or np.max(y1_data) >= line1.axes.get_ylim()[1]
    ):
        plt.ylim([np.min(y1_data) - np.std(y1_data), np.max(y1_data) + np.std(y1_data)])

    plt.pause(pause_time)

    return line1
