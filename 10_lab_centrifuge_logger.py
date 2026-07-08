"""
Lab Centrifuge Logger
Practices: functions with default parameter values
"""

def log_centrifuge(user_name, sample_id, duration=15):
    print(f"{user_name} is spinning sample {sample_id} for {duration} minutes.")


log_centrifuge("Harshwardhan", "Sample123", 30)
log_centrifuge("Harshwardhan", "Sample123")
