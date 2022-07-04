# lane_simulator_study
판단팀 차선인식 미션 연습을 위한 레포지토리 입니다.

## 1. 자이트론 미션 설명

• 시뮬레이터상에서 자동차가 차선을 벗어나지 않고 주행하게 만드는 것이 목표입니다.  
• 카메라로부터 640x480 크기의 영상을 ROS 토픽으로 받을 수 있습니다.  
• 차량 속도와 조향각을 제어하는 ROS 토픽을 발행할 수 있습니다.  
• 속도 : 0 ~ 50 의 정수값으로 제어
• 조향각 : -50 ~ 50 의 정수값으로 제어

![image CCT0M1](https://user-images.githubusercontent.com/48710703/170824267-8b3ec4ae-9d99-412a-877c-8567e43e5af2.png)  

시뮬레이터가 제공하는 카메라 이미지를 영상처리하여 차선의 위치를 찾고,  
이를 계산해 차선을 벗어나지 않고 주행할 수 있는 조향각을 찾아내고,  
모터제어 토픽을 시뮬레이터로 보내 차량이 차선을 벗어나지 않도록 운전하면 됩니다.  

## 2. 개발환경 및 패키지 실행법
Tutorial을 확인해주세요! [Tutorial](https://github.com/choonghyun-park/lane_simulator_study/blob/main/Tutorial.md)
