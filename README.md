# TinyML-Benchmark

### Datasets (D1 - D10)

D1 [Iris Flowers](https://archive.ics.uci.edu/ml/datasets/iris): (4 features, 3 classes, 150 samples) <br/>
D2: [Wine](https://archive.ics.uci.edu/ml/datasets/wine): (13 features, 3 classes, 178) <br/>
D3: [Vowel](https://archive.ics.uci.edu/ml/datasets/Japanese+Vowels): (13 features, 11 classes, 989 samples) <br/>
D4: [Statlog Vehicle Silhouettes](https://archive.ics.uci.edu/ml/datasets/Statlog+%28Vehicle+Silhouettes%29): (18 features, 4 classes, 845 samples) <br/>
D5: [Anuran Calls](https://archive.ics.uci.edu/ml/datasets/Anuran+Calls+%28MFCCs%29): (64 features, 10 classes, 1797 samples)<br/>
D6: [Breast Cancer](https://www.kaggle.com/uciml/breast-cancer-wisconsin-data): (30 features, 2 classes, 569 samples)<br/>
D7: [Texture](https://www.robots.ox.ac.uk/~vgg/data/dtd/index.html): (40 features, 11 classes, 5000 samples)<br/>
D8: [Sensorless Drive Diagnosis](https://archive.ics.uci.edu/ml/datasets/dataset+for+sensorless+drive+diagnosis): (48 features, 11 classes, 999 samples)<br/>
D9: [MNIST Handwritten Digits](http://yann.lecun.com/exdb/mnist/): (64 features, 10 classes, 1797 samples)<br/>
D10: [Human Activity](https://archive.ics.uci.edu/ml/datasets/human+activity+recognition+using+smartphones): (74 features, 6 classes, 5000 samples)<br/>


### MCU Boards (B1 - B7)

B1: [Teensy 4.0](https://www.pjrc.com/teensy/) (Cortex-M7 @600 MHz, 2MB Flash, 1MB SRAM) <br/>
B2: [STM32 Nucleo H7](https://www.st.com/en/evaluation-tools/nucleo-h743zi.html) (Cortex-M7 @480 MHz, 2MB Flash, 1 MB SRAM) <br/>
B3: [Arduino Portenta](https://store.arduino.cc/portenta-h7) (Cortex-M7+M4 @480 MHz, 2MB Flash, 1MB SRAM) <br/>
B4: [Feather M4 Express](https://www.adafruit.com/product/3857)  (Cortex-M4 @120 MHz, 2MB Flash, 192KB SRAM) <br/>
B5: [Generic ESP32](https://esphome.io/devices/nodemcu_esp32.html) (Xtensa LX6 @240 MHz, 4MB Flash, 520KBSRAM) <br/>
B6: [Arduino Nano 33](https://store.arduino.cc/arduino-nano-33-iot) (Cortex-M4 @64 MHz, 1MB Flash, 256KB SRAM) <br/>
B7: [Raspberry Pi Pico](https://www.raspberrypi.org/products/raspberry-pi-pico/) (Cortex-M0+ @133 MHz, 16MB Flash, 264KB SRAM) <br/>

### Architecture of the networks executed on MCU boards 

**FC 1 x 10: 1 layer with 10 neurons**
![alt text](https://github.com/bharathsudharsan/TinyML-Benchmark/blob/main/TFLite_trained_models/FC%201%20x%2010_Breast%20cancer.png)

**FC 10 x 10:  10 layers, where each layer contains 10 neurons**
![alt text](https://github.com/bharathsudharsan/TinyML-Benchmark/blob/main/TFLite_trained_models/FC%2010%20x%2010_Breast%20cancer.png)

**FC 10 + 50: 2 layers, where 1st layer contains 10 neurons, and 2nd layer contains 50 neurons**
![alt text](https://github.com/bharathsudharsan/TinyML-Benchmark/blob/main/TFLite_trained_models/FC%2010%2B50_Breast%20cancer.png)


## NN inference performance on 7 MCU boards

The below Figure (y-axis in base-10 log scale) presents the average time taken by MCU boards B1 - B7 to infer using D1 - D10. 

1. For all 3 NN types, Teensy 4.0 (B1) is the fastest as it performed unit inference in 3.14 µs, 11.13 µs, 18.12 µs respectively. 
2. For the same data samples, Raspberry Pi Pico (B7) is the slowest (≈ 99 - 175 x times slower than B1), as it took 313.77 µs, 1953.96 µs, 2801.82 µs. 
3. Although B7 has a faster clock than Arduino Nano 33 (B6), it is still slow as Cortex M4 is superior to Cortex M0+. 
4. Although B1 - B4 has the same Cortex M7 processor, B1 still is significantly faster as it has the highest clock speed of 600 MHz. 

![alt text](https://github.com/bharathsudharsan/TinyML-Benchmark-NNs-on-MCUs/blob/main/Fig1_B1-B7_inference_time.png)

## Executing NNs on STM32 Nucleo H7 (B2): Inference time and memory used

The below Figure (y-axis in base-10 log scale) presents the complete inference time on the STM32 Nucleo H7 (B2) for each of the 30 models. 
1. When considering the *FC 1x10* network, for the 4 features Iris dataset (D1), it took 5.16 µs to infer, and for the highest 74 features Human Activity dataset (D10), it took 872.85 µs to infer. 
2. When considering *FC 10x10*, for the Iris dataset, it took 20.15 µs, and 3369.54 µs for the Human Activity dataset. 

![alt text](https://github.com/bharathsudharsan/TinyML-Benchmark-NNs-on-MCUs/blob/main/Fig2_Infer_time_on_B2_for_D1_to_D10.png)

The below Figure presents the time taken by Arduino IDE to compile each of the 30 models for STM32 Nucleo H7 (B2), along with the complete FLASH and SRAM requirements. The models trained using the datasets with more features, classes consumed higher compilation time, and higher fash memory.

![alt-text-1](https://github.com/bharathsudharsan/TinyML-Benchmark-NNs-on-MCUs/blob/main/Fig3_Flash_complie_time_SRAM_on_B2.png) 
