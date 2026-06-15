def calculate_fifo(pages, capacity):
    frames = []
    page_faults = 0
    steps = []

    for page in pages:
        status = ""

        if page not in frames:
            page_faults += 1
            status = "Lỗi trang (Fault)"

            if len(frames) < capacity:
                frames.append(page)
            else:
                frames.pop(0)
                frames.append(page)
        else:
            status = "Trúng (Hit)"

        steps.append({
            "page": page,
            "frames": list(frames),
            "status": status
        })
    return steps, page_faults


if __name__ == '__main__':
    pages_input = input("Nhập dãy trang: ")
    capacity = int(input("Nhập số khung trang: "))

    pages = [int(p.strip()) for p in pages_input.split(',')]

    steps, page_faults = calculate_fifo(pages, capacity)

    print("\n--- FIFO ---")
    for step in steps:
        print(f"Trang {step['page']:>2} | Frames: {step['frames']} | {step['status']}")

    print("\nTổng số Page Faults (FIFO):", page_faults)