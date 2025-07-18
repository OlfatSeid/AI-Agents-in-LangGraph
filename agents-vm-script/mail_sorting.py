import json 
from typing import TypedDict, List, Dict, Any, Optional
from langgraph.graph import StateGraph, START, END
from langchain_core.messages import HumanMessage
from langchain_groq import ChatGroq 
from config import GROQ_API_KEY


model = ChatGroq(
    model_name="gemma2-9b-it",
    api_key=GROQ_API_KEY  
)

class InvitationState(TypedDict):
    email: Dict[str, Any]            
    event_type: Optional[str]        
    priority: Optional[str]           
    rsvp_draft: Optional[str]        
    sender_importance: Optional[str]  

# Workflow nodes
def process_invitation(state: InvitationState):
    email = state["email"]
    print(f"📩 Processing invitation: {email['subject']}")
    return state



def classify_event(state: InvitationState):
    email = state["email"]
    
    prompt = f"""Analyze event invitation for Bruce Wayne:
From: {email['sender']}
Subject: {email['subject']}
Body: {email['body']}

Classify:
1. Event Type: [gala, charity, private, spam]
2. Priority: [critical, high, medium, low]
3. Sender Importance: [VIP, known, unknown]

Return ONLY JSON without any formatting or additional text: {{
    "event_type": "...",
    "priority": "...",
    "sender_importance": "..."
}}"""
    
    response = model.invoke(prompt)
    
    # Clean and parse the JSON response
    try:
        # Remove Markdown code blocks and whitespace
        json_str = response.content.strip().replace('```json', '').replace('```', '')
        classification = json.loads(json_str)
    except json.JSONDecodeError:
        # Fallback if JSON parsing fails
        print("⚠️ Failed to parse JSON, using default classification")
        classification = {
            "event_type": "spam",
            "priority": "low",
            "sender_importance": "unknown"
        }
    
    return {
        "event_type": classification.get("event_type", "spam"),
        "priority": classification.get("priority", "medium"),
        "sender_importance": classification.get("sender_importance", "unknown")
    }
    
    response = model.invoke(prompt)
    classification = eval(response.content)
    return {
        "event_type": classification["event_type"],
        "priority": classification["priority"],
        "sender_importance": classification["sender_importance"]
    }

def draft_rsvp(state: InvitationState):
    email = state["email"]
    
    prompt = f"""Draft RSVP response for {state['event_type'].upper()} event:
Sender: {email['sender']}
Event: {email['subject']}
Importance: {state['sender_importance']} contact

Guidelines:
- Maintain Bruce Wayne's public persona
- Express interest but no commitment
- 2-3 sentences maximum"""
    
    response = model.invoke(prompt)
    return {"rsvp_draft": response.content}

def handle_spam(state: InvitationState):
    print(f"🚫 Marked as SPAM: {state['email']['subject']}")
    return state

def notify_bruce(state: InvitationState):
    email = state["email"]
    print("\n" + "="*50)
    print(f"Sir, you've received an invitation from {email['sender']}")
    print(f"Event Type: {state['event_type'].upper()} | Priority: {state['priority'].upper()}")
    print("\nDrafted Response:")
    print("-"*50)
    print(state["rsvp_draft"])
    print("="*50 + "\n")
    return state

# Routing logic
def route_invitation(state: InvitationState) -> str:
    return "draft" if state["event_type"] != "spam" else "spam"

# Build workflow
flow = StateGraph(InvitationState)
flow.add_node("process", process_invitation)
flow.add_node("classify", classify_event)
flow.add_node("draft", draft_rsvp)
flow.add_node("spam", handle_spam)
flow.add_node("notify", notify_bruce)

flow.set_entry_point("process")
flow.add_edge("process", "classify")
flow.add_conditional_edges("classify", route_invitation, {"draft": "draft", "spam": "spam"})
flow.add_edge("draft", "notify")
flow.add_edge("notify", END)
flow.add_edge("spam", END)

invitation_manager = flow.compile()

# Example emails
gala_invite = {
    "sender": "gotham_mayor@gov.org",
    "subject": "Annual Gotham City Gala - Honoring Bruce Wayne",
    "body": "Mr. Wayne, we request your presence at the 25th Annual Gotham Gala..."
}

charity_request = {
    "sender": "orphanage@gotham.org",
    "subject": "Fundraising Dinner for Gotham Orphans",
    "body": "Dear Mr. Wayne, we humbly request your support for our annual..."
}

spam_email = {
    "sender": "crypto_events@spam.io",
    "subject": "VIP Blockchain Party in Metropolis",
    "body": "Exclusive event for crypto whales! Free champagne for all attendees..."
}

# Process invitations
for name, email in [("Gala", gala_invite), ("Charity", charity_request), ("Spam", spam_email)]:
    print(f"\n{'#'*40}")
    print(f"PROCESSING {name.upper()} INVITATION")
    print(f"{'#'*40}")
    
    result = invitation_manager.invoke({
        "email": email,
        "event_type": None,
        "priority": None,
        "rsvp_draft": None,
        "sender_importance": None
    })

