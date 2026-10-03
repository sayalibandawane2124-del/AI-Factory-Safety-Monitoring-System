def assess_risk(detected_class):
    rules = {
        "no_helmet": {
            "severity": "HIGH",
            "recommendation": "Wear the required safety helmet immediately."
        },
        "no_gloves": {
            "severity": "HIGH",
            "recommendation": "Wear appropriate safety gloves before continuing work."
        },
        "no_goggle": {
            "severity": "HIGH",
            "recommendation": "Wear protective safety goggles immediately."
        },
        "no_boots": {
            "severity": "HIGH",
            "recommendation": "Wear approved safety footwear."
        },
        "helmet": {
            "severity": "SAFE",
            "recommendation": "Required helmet detected. Continue monitoring."
        },
        "vest": {
            "severity": "SAFE",
            "recommendation": "Safety vest detected."
        }
    }

    return rules.get(
        detected_class,
        {
            "severity": "REVIEW",
            "recommendation": "Manual safety verification recommended."
        }
    )


# Test
if __name__ == "__main__":
    test_detection = "no_helmet"

    result = assess_risk(test_detection)

    print("Detected Issue :", test_detection)
    print("Severity       :", result["severity"])
    print("Recommendation :", result["recommendation"])