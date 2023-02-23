# Imports / Libraries
import random
import time
import matplotlib.pyplot as plt

# Define class section


class Vehicle:
    def __init__(self, manufacturer, model, vehicle_type, cost, current_mileage):
        self.manufacturer = manufacturer
        self.model = model
        self.type = vehicle_type
        self.cost = cost
        self.current_mileage = current_mileage

    def __lt__(self, other):
        return self.cost < other.cost

    def __str__(self):
        return f"{self.manufacturer} {self.model} ({self.type}), Cost: ${self.cost:,}, Mileage: {self.current_mileage} miles"


# Algo Section
def sort(lst, alg):
    return alg(lst.copy())


def sort_by_cost(lst):
    return sorted(lst, key=lambda x: x.cost)


# Sorting Algorithms

# Selection Sort
def selection_sort(lst):
    for i in range(len(lst)):
        min_index = i
        for j in range(i+1, len(lst)):
            if lst[j] < lst[min_index]:
                min_index = j
        lst[i], lst[min_index] = lst[min_index], lst[i]
    return lst


# Merge Sort
def merge_sort(lst):
    if len(lst) <= 1:
        return lst
    mid = len(lst) // 2
    left = merge_sort(lst[:mid])
    right = merge_sort(lst[mid:])
    return merge(left, right)


def merge(left, right):
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result += left[i:]
    result += right[j:]
    return result


# Bubble Sort
def bubble_sort(lst):
    for i in range(len(lst)):
        for j in range(len(lst)-i-1):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
    return lst


# # Main Program for question#1 before measuring performance
# def main():
#     # Create a list of random Vehicle objects
#     num_vehicles = 10
#     vehicles = [Vehicle(
#         manufacturer=f"Manufacturer {i+1}",
#         model=f"Model {i+1}",
#         vehicle_type=random.choice(["Sedan", "Coupe", "SUV", "Truck"]),
#         cost=random.randint(10000, 50000),
#         current_mileage=random.randint(0, 50000)
#     ) for i in range(num_vehicles)]

#     # Sort the list of vehicles using selection sort
#     sorted_vehicles = sort(vehicles, selection_sort)

#     # Print the sorted list of vehicles
#     print("Sorted vehicles:")
#     for vehicle in sorted_vehicles:
#         print(vehicle)


# if __name__ == "__main__":
#     main()


#Main Program for Question #1 but we are measuring performance using lists
# 
def measure_performance(algorithms, list_sizes):
    results = {}
    for algorithm_name, algorithm_func in algorithms.items():
        results[algorithm_name] = []
        for list_size in list_sizes:
            # Create a list of random Vehicle objects
            vehicles = [Vehicle(
                manufacturer=f"Manufacturer {i+1}",
                model=f"Model {i+1}",
                vehicle_type=random.choice(["Sedan", "Coupe", "SUV", "Truck"]),
                cost=random.randint(10000, 50000),
                current_mileage=random.randint(0, 50000)
            ) for i in range(list_size)]

            # Time the execution of the algorithm
            start_time = time.time()
            algorithm_func(vehicles)
            end_time = time.time()

            # Add the execution time to the results
            execution_time = end_time - start_time
            results[algorithm_name].append(execution_time)

    return results


# Main program
if __name__ == "__main__":
    # Define the algorithms to test
    algorithms = {
        "Selection Sort": selection_sort,
        "Merge Sort": merge_sort,
        "Bubble Sort": bubble_sort,
        "Python Built-in Sort": sort_by_cost,
    }

    # Define the list sizes to test
    list_sizes = [10, 100, 1000, 10000]

    # Measure the performance of the sorting algorithms
    results = measure_performance(algorithms, list_sizes)

    # Create a graph of the results
    for algorithm_name, execution_times in results.items():
        plt.plot(list_sizes, execution_times, label=algorithm_name)
    plt.title("Sorting Algorithm Performance")
    plt.xlabel("List Size")
    plt.ylabel("Execution Time (Seconds)")
    plt.legend()
    plt.show()
