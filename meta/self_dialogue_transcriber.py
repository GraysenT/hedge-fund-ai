def transcribe_thought_dialogue(agent_conversations):
    """
    Converts internal agent debates into human-readable format for audit and insight.
    """
    transcripts = []
    for conv in agent_conversations:
        transcripts.append(f"{conv['agent1']} vs {conv['agent2']}: {conv['topic']} → {conv['result']}")
    return transcripts