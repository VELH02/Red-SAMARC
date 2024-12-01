# SMARC Network: Smart Monitoring, Alarming, and Reporting of Air Quality in Critical Areas

This project aims to develop a low-cost sensor network to monitor air quality in the areas surrounding Cerro Patacón, Panama. Conducted at the Technological University of Panama (UTP), the SMARC Network provides real-time data visualization in graphs for both government and private institutions, supporting enhanced environmental monitoring and rapid response.

This project utilizes LoRa technology.

## Parts Used

The following components are utilized in the SMARC MK1:

- **ESP32**: Microcontroller for processing and connectivity.
- **Laser-Based Particle Sensor SDS011**: Measures PM2.5 and PM10 particle concentration.
- **Pressure and Temperature Sensor AM2301 (DHT22)**: Provides temperature and humidity readings.
- **Battery and Solar Charger Controller**: Ensures efficient energy management.
- **LiFePO4 Battery**: Powers the system with stable and long-lasting energy storage.
- **Waterproof Sealed Project Box**: Protects the components from environmental factors.


## Schematic
![SMARC MK1 Schematic](https://github.com/VELH02/SMARC-Network/blob/main/Images/Schematic_SMARK.png?raw=true)

## Deployment

The initial deployment of the **SMARC Network** took place at a designated location within the **Technological University of Panama (UTP)**. This site provided reliable internet access and an optimal environment for experimenting with **LoRa communication**.
![Deployment](https://github.com/VELH02/SMARC-Network/blob/main/Images/Location.png?raw=true)
### Deployment Phases

1. **Initial Setup**:
   - The system was installed to test the **battery life** and evaluate the performance of the **solar charge controller**. 
   - It was determined that the initial charge controller was not functioning properly, and it was replaced with a generic **PWM solar charge controller** featuring a **5V USB output**. This output powers the **ESP32** and the connected sensors.

2. **Power System**:
   - A **10W solar panel** was utilized to charge a **LiFePO4 battery**, providing sustainable and stable energy for the system's operation.
   - The solar panel, in conjunction with the PWM charge controller, ensures continuous energy supply, even in outdoor conditions.

3. **Sensor Integration**:
   - After stabilizing the power system, the measurement systems were installed incrementally.
   - The **SDS011 Laser-Based Particle Sensor** was the last component to be integrated. This sensor includes a built-in fan to draw air for particulate measurement.

4. **Adaptations for Outdoor Deployment**:
   - To accommodate the particle sensor within the **hermetically sealed project box**:
     - A **tube** was connected to the sensor to allow external air intake. This tube is concealed beneath the solar panel to protect it from environmental elements like rain and dirt.
     - A **ventilation hole** was added beneath the box to regulate internal pressure and ensure adequate air circulation.
   - These modifications enable the sensor to draw fresh air while maintaining the weatherproof integrity of the enclosure.
![enter image description here](https://github.com/VELH02/SMARC-Network/blob/main/Images/SMARC%20MK1%201.jpg?raw=true)
---

This deployment phase validated the system's ability to operate reliably in outdoor environments, confirming the viability of its energy management, data collection, and communication systems.

You can Check all the Information collected by this deployment here: [ThingSpeak Channel](https://thingspeak.mathworks.com/channels/2760762)
