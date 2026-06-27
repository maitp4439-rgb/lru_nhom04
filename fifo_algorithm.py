def calculate_fifo(pages, capacity):
    frames = [] 
    page_faults = 0
    steps = []
    replace_index = 0 

    for page in pages:
        status = ""

        # Case 1: Page Fault 
        if page not in frames:
            page_faults += 1
            status = "Fault"

            if len(frames) < capacity:
                frames.append(page)
            else:

                frames[replace_index] = page
                
                replace_index = (replace_index + 1) % capacity
                
        # Case 2: Page Hit
        else:
            status = "Hit"
        steps.append({
            "page": page,
            "frames": list(frames),
            "status": status
        })
    return steps, page_faults


if __name__ == '__main__':
    pages_input = input("Enter page reference string (comma-separated): ")
    capacity = int(input("Enter number of frames: "))

    pages = [int(p.strip()) for p in pages_input.split(',') if p.strip()]

    steps, page_faults = calculate_fifo(pages, capacity)

    print("\n" + "=" * 45)
    print("FIFO ALGORITHM (PHYSICAL LOCATION VIEW)")
    print("=" * 45)
    
    for step in steps:
        print(f"Page {step['page']:>2} | Frames: {str(step['frames']):<15} | Status: {step['status']}")

    print("-" * 45)
    print(f"Total Page Faults : {page_faults}")
    
    fault_rate = (page_faults / len(pages)) * 100 if len(pages) > 0 else 0
    print(f"Page Fault Rate   : {fault_rate:.2f}%")