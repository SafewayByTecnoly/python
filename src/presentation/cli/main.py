from src.infra.repositories.in_memory import InMemoryEventRepository
from src.application.services.event import EventService

def main():
    print("Creating events...")
    event_payload = [{
        "name": "Test Event",
        "description": "Test Description",
        "level": 5,
    }, {
        "name": "Test Event 2",
        "description": "Test Description 2",
        "level": 3,
    }, {
        "name": "Test Event 3",
        "description": "Test Description 3",
        "level": 1,
    }]

    repository = InMemoryEventRepository()
    event_service = EventService(repository)
    for event in event_payload:
        event_service.create_event(event["name"], event["description"], event["level"])
    
    print("Events created successfully")
    print("Listing events...")
    events = event_service.list_events()
    for event in events:
        print(f"Event: {event.name}")
        print(f"Description: {event.description}")
        print(f"Level: {event.level}")
        print(f"Created at: {event.created_at}")
        print(f"Updated at: {event.updated_at}")

if __name__ == "__main__":
    main()