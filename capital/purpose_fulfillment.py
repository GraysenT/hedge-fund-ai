class PurposeFulfillment:
    def __init__(self):
        self.fulfilled_purposes = []

    def fulfill_purpose(self, purpose_name, progress):
        """Track and fulfill the system’s recursive purpose."""
        fulfillment = {"purpose": purpose_name, "progress": progress}
        self.fulfilled_purposes.append(fulfillment)
        print(f"Fulfilled purpose: {purpose_name} with progress: {progress}%")
    
    def get_fulfilled_purposes(self):
        return self.fulfilled_purposes