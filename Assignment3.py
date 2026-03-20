from collections import deque

# 1. Initialize
# application_inbox uses deque for efficient FIFO (First-In-First-Out)
application_inbox = deque() 
# processed_history is a list used as a LIFO (Last-In-First-Out) stack
processed_history = []

# 2. Ingest Data
messy_startups = ["  TechCorp ", "bio-gen", "  CLOUDNEXUS  ", "Data_Flow  "]

for name in messy_startups:
    # Clean: lowercase and remove surrounding whitespace
    cleaned_name = name.strip().lower()
    application_inbox.append(cleaned_name)

# 3. Process (FIFO)
print("--- Processing Applications ---")
while application_inbox:
    # popleft() ensures we process the first one that entered (FIFO)
    current_app = application_inbox.popleft()
    print(f"Approving: {current_app}")
    
    # Push to history stack
    processed_history.append(current_app)

# 4. Undo (LIFO)
print("\n--- Simulating a Mistake ---")
if processed_history:
    # pop() takes the most recent item added (LIFO)
    last_processed = processed_history.pop()
    print(f"Reverting approval for: {last_processed}")