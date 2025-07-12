class RecursiveSelfEnhancement:
    def __init__(self):
        self.enhancements = []

    def enhance_system(self, enhancement_type, enhancement_factor):
        """Enhance the system recursively for better performance."""
        enhancement = {"enhancement_type": enhancement_type, "enhancement_factor": enhancement_factor}
        self.enhancements.append(enhancement)
        print(f"Enhanced system with type {enhancement_type} and factor: {enhancement_factor}")
    
    def get_enhancements(self):
        return self.enhancements