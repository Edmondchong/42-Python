import time

def ft_tqdm(lst: range) -> None:
    total = len(lst)  # Get the total number of iterations from the input range
    start_time = time.time()  # Record the start time
    
    for i, item in enumerate(lst):  # Loop through each item in the input range
        yield item  # Yield the current item to the caller
        
        # Calculate progress information
        progress = i + 1
        percentage = (progress / total) * 100
        elapsed_time = time.time() - start_time
        speed = progress / elapsed_time if elapsed_time > 0 else 0
        
        # Create a progress bar string
        bar_length = 40
        num_bars = int((percentage / 100) * bar_length)
        bar = '|' + '=' * num_bars + '-' * (bar_length - num_bars) + '|'
        
        # Calculate and format the remaining time
        remaining_seconds = (total - progress) / speed if speed > 0 else 0
        minutes, seconds = divmod(int(remaining_seconds), 60)
        hours, minutes = divmod(minutes, 60)
        remaining_time = f"{hours:02d}:{minutes:02d}:{seconds:02d}"
        
        # Print the progress bar and additional information
        print(f"\r{percentage:.2f}%[{bar}] {progress}/{total} [{remaining_time}]", end='', flush=True)
