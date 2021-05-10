## Executing NNs on STM32 Nucleo H7: Inference time and memory used

The below Figure (y-axis in base-10 log scale) presents the complete inference time on the STM32 Nucleo H7 (B2) for each of the 30 models. 
1. When considering the *FC 1x10* network, for the 4 features Iris dataset (D1), it took 5.16 µs to infer, and for the highest 74 features Human Activity dataset (D10), it took 872.85 µs to infer. 
2. When considering *FC 10x10*, for the Iris dataset, it took 20.15 µs, and 3369.54 µs for the Human Activity dataset. 

![alt text](https://github.com/bharathsudharsan/TinyML-Benchmark-NNs-on-MCUs/blob/main/Infer_time_flash_sram_on_B2/Infer_time_on_B2_for_D1_to_D10.png)

The below Figure presents the time taken by Arduino IDE to compile each of the 30 models for STM32 Nucleo H7 (B2), along with the complete FLASH and SRAM requirements. The models trained using the datasets with more features, classes consumed higher compilation time, and higher fash memory.

![alt-text-1](https://github.com/bharathsudharsan/TinyML-Benchmark-NNs-on-MCUs/blob/main/Infer_time_flash_sram_on_B2/Flash_complie_time_SRAM_on_B2.png) 