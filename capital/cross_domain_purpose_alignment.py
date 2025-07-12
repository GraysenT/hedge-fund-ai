class CrossDomainPurposeAlignment:
    def __init__(self):
        self.alignments = []

    def align_across_domains(self, domain_name, purpose):
        """Align recursive purpose across multiple domains."""
        alignment = {"domain": domain_name, "purpose": purpose}
        self.alignments.append(alignment)
        print(f"Aligned purpose: {purpose} across domain: {domain_name}")
    
    def get_alignments(self):
        return self.alignments