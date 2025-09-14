# DFMP - Detection of Flaws in Machine Parts

DFMP (Detection of Flaws in Machine Parts) is an innovative device designed to automatically detect defects and flaws in machine components using infrared sensor technology and computer vision techniques. The system captures distance measurements to generate point cloud images, which are then processed to identify potential manufacturing defects or wear patterns.

## Project Overview

This is a government funded project which addresses the critical need for automated quality control in manufacturing environments. By leveraging IR sensor technology and advanced image processing algorithms, DFMP provides a non-destructive testing solution for detecting flaws in machine parts that might not be visible to the naked eye.

### Key Objectives

- Develop an automated flaw detection system for machine parts
- Utilize IR sensors for non-contact distance measurements
- Generate and process point cloud representations of parts
- Implement computer vision algorithms for defect identification
- Create a cost-effective alternative to traditional inspection methods

## Technology Stack

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![OpenCV](https://img.shields.io/badge/OpenCV-27338e?style=for-the-badge&logo=OpenCV&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white)
![Arduino](https://img.shields.io/badge/Arduino-00979D?style=for-the-badge&logo=Arduino&logoColor=white)

## System Architecture

### Hardware Components

- **Ultrasonic Sensor**: Primary sensing element for distance measurements
- **Microcontroller**: Data acquisition and sensor control
- **Processing Unit**: Computer vision and analysis processing

### Software Components

- **Sensor Interface**: Communication with IR sensors
- **Point Cloud Generation**: Converting distance data to 3D representations
- **Analysis Engine**: Defect classification and reporting
- **User Interface**: System control and results visualization

## How It Works

1. **Data Acquisition**: IR sensors measure distances at multiple points across the machine part surface
2. **Point Cloud Generation**: Distance measurements are converted into a 3D point cloud representation
3. **Flaw Detection**: Computer vision algorithms identify anomalies and potential defects
4. **Classification**: Detected flaws are classified by type and severity
5. **Reporting**: Results are presented through visual interfaces and reports

## Features

### Current Implementation

- Ultrasonic sensor-based distance measurement system
- Point cloud data generation from sensor readings
- Basic image processing pipeline for defect detection
- Automated scanning and data collection

### Planned Enhancements

- Machine learning models for improved defect classification
- Real-time processing capabilities
- Integration with manufacturing systems
- Advanced visualization tools
- Multiple sensor fusion for enhanced accuracy

## Installation and Setup

### Prerequisites

```bash
# Python packages
opencv-python>=4.5.0
numpy>=1.20.0
matplotlib>=3.3.0
scipy>=1.6.0
```

### Hardware Setup

1. Connect Ultrasonic sensors to the microcontroller
2. Set up mechanical scanning mechanism
3. Configure sensor positioning and calibration
4. Connect processing unit to sensor array

### Software Installation

```bash
# Clone the repository
git clone https://github.com/Devanshu2004/DFMP.git
cd DFMP

# Run the main application
python main.py
```

## Usage

### Basic Operation

1. **System Calibration**: Run calibration routine to set sensor baselines
2. **Part Positioning**: Place machine part in scanning area
3. **Scan Execution**: Initiate automated scanning process
4. **Results Analysis**: Review detected flaws and generate reports

### Configuration

```python
# Example configuration
config = {
    'sensor_resolution': 0.1,  # mm
    'scan_speed': 10,          # mm/s
    'detection_threshold': 0.5,
    'output_format': 'json'
}
```

## Results and Performance

### Detection Capabilities

- **Crack Detection**: Surface cracks and fractures
- **Dimensional Defects**: Incorrect measurements and tolerances
- **Surface Irregularities**: Scratches, dents, and wear patterns
- **Material Inconsistencies**: Density variations and voids

## Applications

### Manufacturing Quality Control

- Automotive parts inspection
- Aerospace component verification
- Electronic device testing
- Precision machinery validation

### Maintenance and Monitoring

- Predictive maintenance applications
- Wear pattern analysis
- Structural health monitoring
- Equipment lifecycle tracking

## Technical Challenges Addressed

1. **Sensor Noise**: Implementation of filtering algorithms for clean data
2. **Point Cloud Processing**: Efficient algorithms for large dataset handling
3. **Real-time Processing**: Optimization for manufacturing line speeds
4. **Environmental Factors**: Compensation for temperature and lighting variations

## Future Development

### Short-term Goals

- Implement machine learning classification models
- Develop web-based user interface
- Add support for multiple sensor types
- Integrate with industrial communication protocols

### Long-term Vision

- AI-powered defect prediction
- Integration with Industry 4.0 systems
- Mobile inspection units
- Cloud-based analysis platform

## Repository Structure

```
DFMP/
├── scannerCode/
|   └── scannerCode.ino
├── data.py
├── errored_farmer.txt
├── ideal_farmer.txt
├── plot.py
├── plot_point_cloud.py
└── README.md
```

## Contributing

Contributions to improve DFMP are welcome! Areas where contributions would be valuable:

- Algorithm optimization for faster processing
- Additional sensor integration
- Machine learning model improvements
- Hardware design enhancements
- Documentation and testing

## Project Status

**Current Phase**: Prototype Development  
**Status**: Active Development  
**Version**: 1.0.0

## Technical Documentation

For detailed technical documentation, including:
- Hardware specifications
- Software architecture
- API reference
- Calibration procedures

Please refer to the `/docs` directory in this repository.

## Contact

**Developer**: Devanshu  
- **GitHub**: [@Devanshu2004](https://github.com/Devanshu2004)
- **Kaggle**: [@devanshujoshi01](https://www.kaggle.com/devanshujoshi01)
- **LinkedIn**: [Devanshu Joshi](https://www.linkedin.com/in/devanshu-joshi-2614d/)
- **Email**: [Devanshu](devanshu1268@gmail.com)

## Acknowledgments

- Thanks to the open-source computer vision community
- Special recognition to contributors and collaborators
- Appreciation for hardware and sensor manufacturers

---

**Note**: This project represents ongoing research and development in automated quality control systems. The technology is designed for educational and research purposes, with potential for industrial application.

**Last Updated**: September 2025
