from time import sleep
from tqdm import tqdm  # Import the tqdm library
from Loading import ft_tqdm

# Using ft_tqdm
for elem in ft_tqdm(range(333)):
    sleep(0.005)
print()

# Using the original tqdm
for elem in tqdm(range(333)):
    sleep(0.005)
print()
