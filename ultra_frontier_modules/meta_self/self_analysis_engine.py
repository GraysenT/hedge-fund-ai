from .meta_structure_reflector import summarize_structure
from .reinvention_trigger import trigger_reinvention

def run_self_analysis():
    structure = summarize_structure()
    findings = []

    for file, funcs in structure.items():
        if len(funcs) > 20:
            findings.append(trigger_reinvention(
                reason=f"High function count in {file}",
                proposed_change=f"Consider modularizing {file}"
            ))

    return findings