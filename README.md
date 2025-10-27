# Image Processing Using Sequential, Parallel, and Distributed Computing

This project demonstrates how image preprocessing tasks (resizing and watermarking) can be optimized using:

- **Sequential Processing**
- **Parallel Processing (Multiprocessing Pool)**
- **Simulated Distributed Processing (Multiple Processes acting as Nodes)**

---

## 📊 Performance Results

| Processing System        | Time (seconds) |
|-------------------------|----------------|
| Sequential Processing   | **0.31**       |
| Parallel (2 Workers)    | **0.42**       |
| Parallel (4 Workers)    | **0.38**       |
| Parallel (8 Workers)    | **0.53**       |
| Distributed (2 Nodes)   | **0.45**       |

---

## 🏁 Best Configuration (Conclusion)

The **best performance was observed at 4 workers**, because:

- The system has **4 CPU cores**.
- With 4 workers, each core gets one process → **maximum CPU utilization**.
- Increasing workers beyond core count (e.g., 8) causes **context switching overhead**, slowing performance.

---

## 🧠 Final Discussion

Parallel processing improved performance compared to sequential execution by allowing multiple images to be processed simultaneously. However, the speedup was limited because:

- The system only has **4 physical cores**, so using **more than 4 workers adds overhead**, reducing performance.
- Image I/O operations (reading/saving files) are relatively slow and become the **bottleneck**, reducing potential parallel gains.
- In distributed processing, communication and process setup time also affect performance.

Despite these limitations, the parallel approach still demonstrates better efficiency than sequential processing and highlights how computation scales with available hardware.

---

## ⭐ If this helped, consider giving the repo a star!


