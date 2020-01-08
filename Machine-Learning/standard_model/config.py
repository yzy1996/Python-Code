import argparse

def ParseParams():
    parser = argparse.ArgumentParser(description="Neural Combinatorial Optimization with RL")

    parser.add_argument('--task', default='vrp10', help="Select the task to solve; i.e. tsp10")
