import matplotlib.pyplot as plt
import numpy as np



def transactions_per_second(start_times, durations):

    # Example data
    start_times = np.arange('2023-04-01T12:00:00', '2023-04-01T12:01:00', dtype='datetime64[s]')
    durations = np.random.normal(loc=200, scale=50, size=len(start_times))  # Random durations in milliseconds

    # Count the number of API calls starting in each second
    unique, counts = np.unique(start_times, return_counts=True)

    # Plotting
    plt.figure(figsize=(10, 6))
    plt.bar(unique, counts, width=np.timedelta64(1, 's'), align='center', color='skyblue')
    plt.xlabel('Start Time')
    plt.ylabel('Calls per Second')
    plt.title('API Calls Per Second Over Time')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()


def percentile_plot(start_times, durations):
    # Calculate percentiles
    percentiles = np.percentile(durations, [25, 50, 90])

    # Plotting
    plt.figure(figsize=(10, 6))
    plt.scatter(start_times, durations, alpha=0.7, label='API Call Durations')
    plt.axhline(percentiles[0], color='r', linestyle='--', label='25th Percentile')
    plt.axhline(percentiles[1], color='g', linestyle='--', label='50th Percentile')
    plt.axhline(percentiles[2], color='b', linestyle='--', label='90th Percentile')

    plt.xlabel('Start Time')
    plt.ylabel('Duration (ms)')
    plt.title('API Call Durations Over Time')
    plt.legend()
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()


def main():


    # Example data
    start_times = np.arange('2023-04-01T12:00:00', '2023-04-01T12:01:00', dtype='datetime64[s]')
    durations = np.random.normal(loc=200, scale=50, size=len(start_times))  # Random durations in milliseconds

    transactions_per_second(start_times=start_times, durations=durations)

    percentile_plot(start_times=start_times, durations=durations)




if __name__ == "__main__":
    main()



