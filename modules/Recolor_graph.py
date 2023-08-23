import Machine_learning
import matplotlib.pyplot as plt


def new_graph():
    
    from Color_changer import colors, color2, background_color
    
    #print(colors[1])
    #print(color2[1])
    
    plt.rcParams['axes.facecolor'] = background_color[1]
    
    plt.figure(figsize=(5, 4))
    plt.title("Machine learning")
    plt.xlabel('Date', fontsize=8)
    plt.ylabel('Closing price', fontsize=8)
    plt.plot(Machine_learning.train['Close']) # The training data
    plt.plot(Machine_learning.valid['Close'], color=colors[1])
    plt.plot(Machine_learning.valid['Predictions'], color=color2[1])
    plt.legend(['Train', 'Validations', 'Predictions'], loc='lower right')
    plt.show()
