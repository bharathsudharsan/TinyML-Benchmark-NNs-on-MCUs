Below Figure presents the complete inference time on the [STM32 Nucleo H7](https://www.st.com/en/evaluation-tools/nucleo-h743zi.html) (B2) for each of the 30 models. 
![alt text](https://github.com/bharathsudharsan/TinyML-Benchmark-NNs-on-MCUs/blob/main/Infer_time_flash_sram_on_B2/Fig.%201.%20b.%20Infer_time_on_B2_for_D1_to_D10.png)
1. When considering the *FC 1x10* network, for the 4 features Iris dataset, it took 5.16 µs to infer, and for the highest 74 features Human Activity dataset, it took 872.85 micro sec to infer. 
2. When considering *FC 10x10*, for Iris dataset, it took 20.15 micro sec, and 3369.54 micro sec for Human Activity dataset. 
