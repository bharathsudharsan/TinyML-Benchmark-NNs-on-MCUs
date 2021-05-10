## NN inference performance on 7 MCU boards

The beloe Figure (y-axis in base-10 log scale) presents the average time taken by MCU boards B1 - B7 to infer using D1 - D10. 

1. For all 3 NN types, Teensy 4.0 (B1) is the fastest as it performed unit inference in 3.14 µs, 11.13 µs, 18.12 µs respectively. 
2. For the same data samples, Raspberry Pi Pico (B7) is the slowest (≈ 99 - 175 x times slower than B1), as it took 313.77 µs, 1953.96 µs, 2801.82 µs. 
3. Although B7 has a faster clock than Arduino Nano 33 (B6), it is still slow as Cortex M4 is superior to Cortex M0+. 
4. Although B1 - B4 has the same Cortex M7 processor, B1 still is significantly faster as it has the highest clock speed of 600 MHz. 

![alt text](https://github.com/bharathsudharsan/TinyML-Benchmark-NNs-on-MCUs/blob/main/Infer_time_on_B1_to_B7/B1-B7_inference_time.png)
