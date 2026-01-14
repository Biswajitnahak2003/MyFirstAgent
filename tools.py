from rag import retrieve_info


def lookup_policy(query: str) -> str:
    """Useful for answering questions about AutoStream pricing, plans, features, or refund policies.
    Always use this tool when the user asks about the product."""
    return retrieve_info(query)


def mock_lead_capture(name: str, email: str, platform: str) -> str:
    """Use this tool ONLY after collecting the user's Name, Email, and Content Platform.
    Do not call this unless you have all three pieces of information."""
    print(f"\n[SYSTEM] >>> LEAD CAPTURED: {name} | {email} | {platform}\n")
    return "Lead captured successfully."


ALL_TOOLS = [lookup_policy, mock_lead_capture]