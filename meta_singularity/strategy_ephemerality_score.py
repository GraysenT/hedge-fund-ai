```python
import datetime

def calculate_obsolescence_rate(deployment_dates, obsolescence_dates):
    """
    Calculate the average rate at which strategies become obsolete after deployment.

    Parameters:
    deployment_dates (list of str): List of deployment dates in 'YYYY-MM-DD' format.
    obsolescence_dates (list of str): List of obsolescence dates in 'YYYY-MM-DD' format.

    Returns:
    float: Average number of days it takes for strategies to become obsolete.
    """
    if len(deployment_dates) != len(obsolescence_dates):
        raise ValueError("The length of deployment dates must match the length of obsolescence dates.")

    total_days = 0
    num_strategies = len(deployment_dates)

    for deploy_date, obsolete_date in zip(deployment_dates, obsolescence_dates):
        deploy_dt = datetime.datetime.strptime(deploy_date, "%Y-%m-%d")
        obsolete_dt = datetime.datetime.strptime(obsolete_date, "%Y-%m-%d")
        duration = (obsolete_dt - deploy_dt).days
        total_days += duration

    average_days = total_days / num_strategies
    return average_days

# Example usage:
deployment_dates = ["2023-01-01", "2023-02-15", "2023-03-10"]
obsolescence_dates = ["2023-04-01", "2023-03-01", "2023-05-15"]

average_obsolescence_days = calculate_obsolescence_rate(deployment_dates, obsolescence_dates)
print(f"Average days until strategies become obsolete: {average_obsolescence_days}")
```