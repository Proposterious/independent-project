# Senior Independent Project ROADMAP

## Interactive Storytelling Robot

### Overview

In this project, we aim to develop an interactive storytelling robot that engages children by narrating stories  
and allowing them to interact with the narrative. The robot will utilize a combination of hardware and software  
technologies to deliver personalized and immersive storytelling experiences.

### Technologies Required

- **Robotics Platform**: Select a suitable robotics platform (e.g., Raspberry Pi with motor controllers) to build   The physical structure of the storytelling robot.
  
- **Speech Synthesis and Recognition**: Integrate speech synthesis for the robot to narrate stories and incorporate  
speech recognition to enable verbal interaction with children.
  
- **Programming Environment**: Develop a programming interface to create and customize interactive storylines  
for the robot, considering user-friendly design principles.
  
- **Machine Learning for Personalization**: Implement machine learning algorithms to personalize the storytelling  
experience based on the child's preferences and engagement levels.
  
- **Sensors for Interaction**: Equip the robot with sensors (e.g., touch sensors) to enable physical interaction  
with children and trigger story events.
  
- **Visual and Audio Elements**: Enhance the storytelling experience with visual and audio elements such as animated  
displays, LED lights, and sound effects.
  
- **Power Supply and Durability**: Ensure the robot has a reliable power supply and design it with durability  
to withstand interaction with children.
  
- **Safety Features**: Implement safety features to protect children from potential hazards associated with  
interacting with the robot.

### My Interpretation of Requirements

- **Robotics Platform**: Motor controllers and Micro controllers that serve different purposes
- [ ] [scripts folder](project/hardware/scripts/INDEX.md) will be updated to contain
  
- **Speech Synthesis**: Use [OpenAI's Whisper](https://github.com/openai/whisper) to interpret voices and  
then use a combination of scripts before coming up with a response.

- **Visual and Audio Elements**: Allow background music (that can be toggled on/off) and have adaptive LEDs

- **Power Supply and Durability**: Research the most reliable power supplies for portable devices and  
the prototype should be relatively sturdy while its materials are held together by strong glue or screws.

- **Safety Features**: After interpreting the speech of the subject, provide a warning that is relayed as follows  
'profanity, sensitive subjects, and material that aren't appropriate for the age provided will not be entertained'.
  - [ ] Therefore, the program must be able to store information related to age and must reference certain  
  dictionaries that contain disallowed vocabulary that will trigger the warning

### Specifics in Development

**Begin here...**

## Website for the Robot

### Purpose

The website should be decently animated with few interactive components.The user should be able to view the  
technologies used, understand my inspiration, and view the current state of the robot (as when it is initially  
released it will be in its *prototype* phase). This website should be in constant development until the completion  
or abandonment of said project.

### Progress in Development
