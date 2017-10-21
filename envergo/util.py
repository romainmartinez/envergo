def axis2int(x=True, y=True):
    import matplotlib.pyplot as plt
    if x:
        plt.gca().xaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: int(x)))
    if y:
        plt.gca().yaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: int(x)))