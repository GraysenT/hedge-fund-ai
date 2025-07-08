class SignalLabeler:
    def label(self, signal):
        label = ""
        conf = signal.get("confidence", 0)
        action = signal.get("action")

        if conf > 0.9:
            label = f"High Confidence {action}"
        elif conf > 0.75:
            label = f"Moderate {action}"
        else:
            label = f"Low Signal"

        signal["label"] = label
        print(f"[LABEL] {signal}")
        return signal