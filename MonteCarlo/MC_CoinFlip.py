"""Monte Carlo Coin flip """
import random, numpy as np, matplotlib.pyplot as plt 

# Select random 0 or 1
def coin_flip():
    return random.randint(0,1)

# Value store
store = []

# Build Monte Carlo Function on 'n' itterations
def monte_carlo(n):
    results = 0
    for i in range(n):
        flip_result = coin_flip()
        results = results + flip_result

        # Probability 
        prob_value = results / (i + 1)
        store.append(prob_value)

        # Plot results
        plt.axhline(y = 0.5, color = 'grey', linestyle = '-')
        plt.xlabel('Itterations')
        plt.ylabel('Probability')
        plt.plot(store, color = 'blue')

    return results / n

# Run the simulation
ans = monte_carlo(500)
print('Final value:', round(100 * ans, 1),'%')
 
