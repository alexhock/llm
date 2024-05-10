from collections import deque
from datetime import datetime, timedelta


def parse_time(time_str):
    # Assuming time_of_call is in a standard format like "YYYY-MM-DD HH:MM:SS"
    return datetime.strptime(time_str, "%Y-%m-%d %H:%M:%S")

def sliding_window_average(timings, window_size_seconds=60):
    # Convert window size to timedelta for easier time comparisons
    window_size = timedelta(seconds=window_size_seconds)
    
    # Sort timings by finish time to handle out-of-order calls
    timings.sort(key=lambda x: parse_time(x[2]))

    # Initialize deque to keep the calls within the current window
    current_window = deque()
    
    # Lists to hold the averages for each window
    tokens_per_minute = []
    calls_per_minute = []
    
    # Iterate over each call in timings
    for tokens, start_time_str, finish_time_str in timings:
        start_time = parse_time(start_time_str)
        finish_time = parse_time(finish_time_str)
        print(start_time, finish_time, tokens)
        
        # Maintain a tuple of start time, finish time, and tokens
        current_window.append((start_time, finish_time, tokens))
        
        # Adjust window to current finish time
        while current_window and current_window[0][1] < finish_time - window_size:
            current_window.popleft()

        #print(current_window)
        
        # Calculate averages for the current window
        total_tokens = sum(tokens for _, _, tokens in current_window)
        total_calls = len(current_window)
        
        # Average tokens and calls per minute
        if current_window:
            # Use the maximum span in the window for calculation
            min_start_time = min(start for start, _, _ in current_window)
            max_finish_time = max(finish for _, finish, _ in current_window)
            time_span = (max_finish_time - min_start_time).total_seconds() / 60
            print(min_start_time, max_finish_time, time_span, total_tokens, total_calls)
            if time_span > 0:
                avg_tokens_per_minute = total_tokens / time_span
                avg_calls_per_minute = total_calls / time_span
            else:
                avg_tokens_per_minute = 0
                avg_calls_per_minute = 0
            
            tokens_per_minute.append(avg_tokens_per_minute)
            calls_per_minute.append(avg_calls_per_minute)

    return tokens_per_minute, calls_per_minute


def calculate_wait_time(tokens_per_minute, calls_per_minute, max_tokens_per_minute, max_calls_per_minute):
    if not tokens_per_minute or not calls_per_minute:
        return 0  # No recent activity, no need to wait
    
    # Get the most recent rates
    latest_tokens_per_minute = tokens_per_minute[-1]
    latest_calls_per_minute = calls_per_minute[-1]
    
    # Calculate how much excess there is over the maximum rates
    excess_tokens_per_minute = max(0, latest_tokens_per_minute - max_tokens_per_minute)
    excess_calls_per_minute = max(0, latest_calls_per_minute - max_calls_per_minute)
    
    # Calculate wait times needed for each rate to drop below the max
    if excess_tokens_per_minute > 0:
        # Time (in minutes) needed for excess tokens to decay below the limit
        tokens_wait_time = excess_tokens_per_minute / latest_tokens_per_minute
    else:
        tokens_wait_time = 0
    
    if excess_calls_per_minute > 0:
        # Time (in minutes) needed for excess calls to decay below the limit
        calls_wait_time = excess_calls_per_minute / latest_calls_per_minute
    else:
        calls_wait_time = 0
    
    # Return the maximum of the two wait times as the required wait time
    return int(max(tokens_wait_time, calls_wait_time) * 60)  # Convert to seconds


def main():

    # Example usage:
    timings = [
        [150, "2024-04-14 12:00:00", "2024-04-14 12:00:20"],
        [100, "2024-04-14 12:00:30", "2024-04-14 12:00:50"],
        [200, "2024-04-14 12:00:25", "2024-04-14 12:00:55"],
        [120, "2024-04-14 12:01:00", "2024-04-14 12:01:30"],
        [180, "2024-04-14 12:01:10", "2024-04-14 12:01:40"],
    ]

    tokens_per_minute, calls_per_minute = sliding_window_average(timings)
    print("Tokens per minute:", tokens_per_minute)
    print("Calls per minute:", calls_per_minute)

    # Example usage:
    max_tokens_per_minute = 400  # Set maximum tokens per minute
    max_calls_per_minute = 10    # Set maximum calls per minute


    # Assume tokens_per_minute and calls_per_minute have been calculated previously
    required_wait_time = calculate_wait_time(tokens_per_minute, calls_per_minute, max_tokens_per_minute, max_calls_per_minute)
    print(f"Wait time required to stay within limits: {required_wait_time} seconds")


if __name__ == "__main__":
    main()