# Virtual Memory Simulation Using Python (Tkinter GUI)

**Name:** P.G.P.M. Bandara  
**Registration Number:** 522512868  
**Student Number:** s22010356  

## Project Overview
This project is a GUI-based simulation of **Virtual Memory Address Translation** using **paging**.  
It demonstrates how logical addresses are translated into physical addresses using a **page table** and **fixed-size frames**.

The application is developed using **Python** and **Tkinter** and allows users to input multiple logical addresses to observe:
- Page number and offset calculation
- Page table lookup
- Page fault handling
- Frame allocation
- Final page table and frame status

## System Configuration
The simulation uses the following fixed parameters:

| Component | Value |
|---------|------|
| Page Size | 1024 bytes |
| Number of Pages | 8 |
| Number of Frames | 4 |
| Logical Address Range | 0 – 8191 |

## Features
- GUI-based user interface using Tkinter
- Accepts multiple logical addresses as comma-separated values
- Validates logical address range
- Calculates page number and offset
- Detects page faults
- Allocates pages to free frames
- Displays physical address translation
- Shows final page table and frame allocation

## Input Format
Users must enter logical addresses as comma-separated integers.

Example: 0, 1024, 2048, 3072


## Output Description
For each logical address, the simulation displays:
- Logical Address
- Page Number
- Offset
- Frame Number (if page is loaded)
- Physical Address
- Page Fault notification (if applicable)

At the end of the simulation:
- Final Page Table
- Frame Allocation Status

## Error Handling
- Displays an error if the input field is empty
- Displays an error for invalid input formats
- Detects logical addresses outside the valid range

## Technologies Used
- Python 3
- Tkinter (GUI)
- Tkinter ScrolledText widget

## How to Run
1. Ensure Python 3 is installed.
2. Save the Python file (`virtualMemorySimulation.py`).
3. Run the program using: `python virtualMemorySimulation.py`

4. Enter logical addresses and click **Simulate**.

## Limitations
- No page replacement algorithm is implemented.
- Pages cannot be loaded when all frames are occupied.
- Frame allocation follows a simple first-free-frame approach.

## Possible Enhancements
- Implement page replacement algorithms (FIFO, LRU)
- Visual representation of page table and frames
- Step-by-step execution mode
- Dark mode UI support

## Conclusion
This project successfully demonstrates the core concepts of **virtual memory management and paging** through a simple and interactive GUI. It is suitable for educational purposes and helps visualize address translation in operating systems.
