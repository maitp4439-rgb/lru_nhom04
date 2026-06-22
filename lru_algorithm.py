def lru_page_replacement(pages, capacity):
    memory = []  
    page_faults = 0
    print(f"Reference String: {pages}")
    print(f"Number of frames: {capacity}\n")
    print(f"{'Page':<10} | {'Memory State':<20} | {'Page Fault?'}")
    print("-" * 50)

    for page in pages:
        is_fault = False
        
        # Case 1: Page Hit (The page is already in memory)
        if page in memory:
            memory.remove(page)
            memory.append(page)
            
        # Case 2: Page Fault (The page is not in memory)
        else:
            is_fault = True
            page_faults += 1
                     
            if len(memory) == capacity:
                memory.pop(0)

            memory.append(page)

        fault_status = "Yes" if is_fault else "No"
        print(f"{page:<10} | {str(memory):<20} | {fault_status}")

    print("-" * 50)
    print(f"Total Page Faults: {page_faults}")
    fault_rate = (page_faults / len(pages)) * 100 if len(pages) > 0 else 0
    print(f"Page Fault Rate  : {fault_rate:.2f}%")
    
    return page_faults

# Example LRU     
if __name__ == '__main__':
    reference_string = [7, 0, 1, 2, 0, 3, 0, 4, 2, 3]
    frames = 3
    lru_page_replacement(reference_string, frames)