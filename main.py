
from user_input import get_user_input
from route_calculator import shortest_path, graph
from traffic_predictor import predict_traffic
from road_condition_detector import detect_road_condition
from preprocess_idd import preprocess_idd

def main():
    # Step 1: Preprocess images
    preprocess_idd()

    # Step 2: Get user input
    start, end, time = get_user_input()

    # Step 2a: Validate locations
    if start not in graph or end not in graph:
        print("Invalid start or end location. Please choose from:", list(graph.keys()))
        return

    # Step 3: Calculate shortest path
    path, distance = shortest_path(start, end)
    if not path:
        print("No route found!")
        return

    print(f"\nSuggested Route: {' -> '.join(path)}")
    print(f"Estimated Distance: {distance} km")

    # Step 4: Predict traffic
    traffic = predict_traffic(start, end, int(time.split(":")[0]))
    print(f"Predicted Traffic Level: {traffic} / 5")

    # Step 5: Predict road condition
    road_condition = detect_road_condition()
    print(f"Road Condition: {road_condition}")

if __name__ == "__main__":
    main()
